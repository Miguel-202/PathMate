import mysql.connector
import os

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    
    
class AIMindsDBModels(metaclass=SingletonMeta):
    def __init__(self):
        #%env:KEY_NAME=value
        if not hasattr(self, 'mydb'):
            self.mydb = mysql.connector.connect(
                host=os.environ.get("DB_HOST", "cloud.mindsdb.com"),
                user=os.environ.get("DB_USER", "your_user"),
                password=os.environ.get("DB_PASS", "your_password"),
                port=os.environ.get("DB_PORT", "3306")
            )
            self.cursor = self.mydb.cursor() 
            
    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_events(cursor):
        query = "SELECT user, title, description, start_time, end_time, special_event_code FROM your_event_table"
        cursor.execute(query)
        events = []
        for row in cursor:
            event = {
                "user": row[0],
                "title": row[1],
                "description": row[2],
                "start_time": row[3],
                "end_time": row[4],
                "special_event_code": row[5]
            }
            events.append(event)
        return events
    
    
    
    
    
    