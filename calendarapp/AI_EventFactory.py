from calendarapp.models import Event
from accounts.models import User

from datetime import datetime, timedelta
from django.db.models import Max
from PathMate.AI_MindsDB_Models import AIMindsDBModels

# This function can later be enhanced to use AI for event creation
def create_auto_events(_user_id):
    ai_db = AIMindsDBModels()
    last_event = Event.objects.all().aggregate(Max('id'))
    last_id = last_event['id__max'] or 0
    
    profile = ai_db.fetch_user_profile(_user_id)
    if profile is None:
        Event.objects.create(
        user = User.objects.get(id=_user_id),
        title = "ERROR" + str(_user_id),
        description = "ERROR",
        start_time = datetime.now(),
        end_time = datetime.now() + timedelta(hours=1),
        special_event_code = 0
    )
        return
    query = ai_db.generate_query("mindsdb.roadmap_calendar_planner_modelcrop", profile)
    
    cursor = ai_db.execute_query(query)
    
    for row in cursor:
        output = row[0]  # Assuming the text is the first field in the result row
        sections = output.split("\n\n") #Splitting the text into sections
    print("LOADING...")
    description = ""
    for section in sections:
        description += f"\n{section}\n{'='*40}"  # A line of '=' to separate the sections
    
    
    last_id += 1
    Event.objects.create(
        user = User.objects.get(id=_user_id),
        title = "AI Event",
        description=description,
        start_time = datetime.now(),
        end_time = datetime.now() + timedelta(hours=1),
        special_event_code = 0
    )
    '''for event in events:
        last_id += 1
        event_title = event[0]
        event_description = event[1]
        event_start_time = event[2]
        event_end_time = event[3]
        event_special_event_code = event[4]
        Event.objects.create(
            id = last_id,
            user = User.objects.get(id=_user_id),
            title = event_title,
            description = event_description,
            start_time = event_start_time,
            end_time = event_end_time,
            special_event_code = event_special_event_code
        )'''


def delete_event(_event):
    _event.delete()
