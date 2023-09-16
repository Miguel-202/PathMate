from django.shortcuts import render,redirect
from ..models.databaseuser import UserProfileTable


def userdata(request):
        if request.method == 'POST':

          user_name =request.POST.get("User_Name")
          user_country =request.POST.get("User_Country")
          Job = request.POST.get("Job")
          user_age = request.POST.get("User_Age")
          user_major = request.POST.get("User_Major")
          user_graduationdate = request.POST.get("User_GraduationDate")
          level_study = request.POST.get("Level_Study")
          location = request.POST.get("Location")
          goals = request.POST.get("Goals")
          goal_deadline = request.POST.get("Goal_Deadline")
          skill_set = request.POST.get("Skill_Set")
          needs_visa_sponsorship = request.POST.get("Needs_Visa_Sponsorship")
          user_availabilty = request.POST.get("User_Availabilty")

          UserProfileTable.objects.create(User_Major=user_major,
                                          User_Name=user_name,
                                          User_Country=user_country,
                                          Job=Job,
                                          User_Age=user_age,
                                          User_GraduationDate=user_graduationdate,
                                          Level_Study=level_study,
                                          Location=location,
                                          Goals=goals,
                                          Goal_Deadline=goal_deadline,
                                          Skill_Set=skill_set,
                                          Needs_Visa_Sponsorship=needs_visa_sponsorship,
                                          User_Availabilty=user_availabilty
                                          )
          return redirect("/accounts/signup")
        return render(request, "accounts/profile-creation.html")

      




