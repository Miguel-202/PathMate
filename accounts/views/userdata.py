from django.shortcuts import render, redirect

def userdata(request):
     return render(request,"accounts/profile-creation.html")