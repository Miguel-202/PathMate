from django.db import models


#Table creation for the User Data
class UserProfileTable(models.Model):

    #Generate fields for user data table 

    User_Name = models.CharField(max_length=300)

    User_Country=models.CharField(max_length=300)

    Job = models.CharField(max_length=300)

    User_Age = models.CharField(max_length=100)

    User_Major =  models.CharField(max_length=300)

    #Dates must be in this format
    User_GraduationDate = models.DateField()

    Level_Study = models.CharField(max_length=300)

    Location =  models.CharField(max_length=300)

    Goals = models.CharField(max_length=300)

    Goal_DeathLine = models.DateField()

    Skill_set = models.CharField(max_length=300)

    Needs_Visa_Sponsorship = models.BooleanField()



    

   
    def __str__(self):
        return self.name
    