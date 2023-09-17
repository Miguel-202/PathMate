from calendarapp.models import Event
from accounts.models import User

from datetime import datetime, timedelta
from django.utils.dateparse import parse_datetime
from django.db.models import Max
from PathMate.AI_MindsDB_Models import AIMindsDBModels

import re
from dateutil.parser import parse
#Q: What is the pip install for dateutil.parser? A: pip install python-dateutil

# This function can later be enhanced to use AI for event creation
def create_auto_events(_user_id):
    ai_db = AIMindsDBModels()
    last_event = Event.objects.all().aggregate(Max('id'))
    last_id = last_event['id__max'] or 0
    
    profile = ai_db.fetch_user_profile(_user_id)
    if profile is None:
        with open("logs.txt", "a") as f:
            f.write("USER NOT FOUND: ")
            f.write("\n\n")
        return
    
    query = ai_db.generate_query("mindsdb.roadmap_calendar_planner_model", profile)
    
    event_string = ai_db.execute_query(query)
    
    pattern  = re.compile(r'title = "(?P<title>.*?)"[,]?\n'
                      r'description = "(?P<description>.*?)"[,]?\n'
                      r'start_time = "(?P<start_time>.*?)"[,]?\n'
                      r'end_time = "(?P<end_time>.*?)"[,]?\n'
                      r'special_event_code = (?P<special_event_code>\d+)')

    
    matches = pattern.findall(event_string)
    with open("logs.txt", "a") as f:
            #log matches.size
            f.write("Matches found: " + str(len(matches)))
            f.write("\n\n")
    
    for match in matches:
        title, description, start_time, end_time, special_event_code = match
        start_time = parse(start_time)  # Convert to datetime object
        end_time = parse(end_time)  # Convert to datetime object
        special_event_code = int(special_event_code)  # Convert to integer

        # Create event
        Event.objects.create(
            user=User.objects.get(id=_user_id),
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            special_event_code=special_event_code
        )
        
    
    


def delete_event(_event):
    _event.delete()
