from calendarapp.models import Event
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# This function can later be enhanced to use AI for event creation
def create_auto_events(_user):
    #user = User.objects.get(username="testuser")
    start_time = datetime(2023, 9, 20, 14, 0)
    end_time = datetime(2023, 9, 20, 15, 0)

    for i in range(2):
        Event.objects.create(
            user=_user,
            title=f"Auto Event {i+1}",
            description=f"Description for auto event {i+1}",
            start_time=start_time,
            end_time=end_time
        )

        start_time += timedelta(hours=1)
        end_time += timedelta(hours=1)


def delete_event(_event):
    _event.is_deleted = 1
    print("---------EVENT DELETED: ", _event, "---------")
    _event.save()
