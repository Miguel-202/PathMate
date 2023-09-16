from calendarapp.models import Event
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db.models import Max
from PathMate.AI_MindsDB_Models import AIMindsDBModels

# This function can later be enhanced to use AI for event creation
def create_auto_events(_user):
    ai_db = AIMindsDBModels()
    start_time = datetime(2023, 9, 20, 14, 0)
    end_time = datetime(2023, 9, 20, 15, 0)
    
    last_event = Event.objects.all().aggregate(Max('id'))
    last_id = last_event['id__max'] or 0
    for i in range(2):
        new_id = last_id + i + 1
        unique_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        Event.objects.create(
            user=_user,
            title=f"Auto Event {i+1} {unique_id})",
            description=f"Description for auto event {new_id}",
            start_time=start_time,
            end_time=end_time
        )

        start_time += timedelta(hours=1)
        end_time += timedelta(hours=1)


def delete_event(_event):
    _event.delete()
