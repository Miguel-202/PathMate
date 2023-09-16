from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#@login_required
def user_data(request):
    # you can replicate the logic you use in GetUserDataView here
    context = {
        'user_name': 'Not Logged In',
        'user_designation': ''
    }
    if request.user.is_authenticated:
        context = {
        'user_name': 'Miguel Martinez',
        'user_designation': 'Game Programmer'
    }
    
    return context
