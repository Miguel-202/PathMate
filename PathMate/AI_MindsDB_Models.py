import mysql.connector
import os
from accounts.models import UserProfileTable
from datetime import datetime

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
        '''
                host=os.environ.get("DB_HOST", "cloud.mindsdb.com"),
                user=os.environ.get("DB_USER", "your_user"),
                password=os.environ.get("DB_PASS", "your_password"),
                port=os.environ.get("DB_PORT", "3306")
                '''
    
class AIMindsDBModels(metaclass=SingletonMeta):
    def __init__(self):
        #%env:KEY_NAME=value
        if not hasattr(self, 'mydb'):
            self.mydb = mysql.connector.connect(
                host="cloud.mindsdb.com",
                user="pathmateai@gmail.com",
                password="PathMateAI",
                port=3306
            )
            self.cursor = self.mydb.cursor() 
          
    def fetch_user_profile(self, user_id):
        try:
            user_profile = UserProfileTable.objects.get(User_id=user_id)
            return user_profile
        except UserProfileTable.DoesNotExist:
            return None 
        
         
    def generate_query(self, model_name, user_profile):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        execute_query = "SELECT response from " + model_name + " WHERE "
        #execute_query += f"User_Name = '{user_profile.User_Name}'  AND "
        #execute_query += f"User_Country = '{user_profile.User_Country}'  AND "
        #execute_query += f"Job = '{user_profile.Job}'  AND "
        #execute_query += f"User_Age = '{user_profile.User_Age}'  AND "
        execute_query += f"User_Major = '{user_profile.User_Major}'  AND "
        execute_query += f"User_GraduationDate = '{user_profile.User_GraduationDate}'  AND "
        execute_query += f"Level_Study = '{user_profile.Level_Study}'  AND "
        execute_query += f"Start_Date = '{now}' AND " 
        #execute_query += f"Location = '{user_profile.Location}'  AND "
        execute_query += f"Goals = '{user_profile.Goals}'  AND "
        #execute_query += f"Goal_Deadline = '{user_profile.Goal_Deadline}'  AND "
        #execute_query += f"Needs_Visa_Sponsorship = '{user_profile.Needs_Visa_Sponsorship}'  AND "
        execute_query += f"Skill_Set = '{user_profile.Skill_Set}'"
        #execute_query += f"User_Availabilty = '{user_profile.User_Availabilty}' "
        return execute_query

        
    def execute_query(self, query):
        self.cursor.execute(query)
        for row in self.cursor:
            output = row[0]  # Assuming the text is the first field in the result row
            sections = output.split("\n\n") #Splitting the text into sections

        result_str = ""
        for section in sections:
            result_str += f"{section}\n\n"
        with open("logs.txt", "a") as f:
            f.write("Result String: ")
            f.write(result_str)
            f.write("\n\n")
        return result_str

    
    
    
    
    
    