#歐睿安版權所有
#CinderyanAPT
#calender
#
#
#

from src.models.calendar_event.calendar_event import CalendarEvent
from src.models.time_tracker.time_tracker import TimeTracker
import database

class Calendar:
    def add_calendar_event(event):
        conn = database.calendar_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO calendar(
                date, 
                title, 
                description, 
                status)
            VALUES(?, ?, ?, ?)
        """, (
            event.date, 
            event.title, 
            event.description, 
            event.status
        ))
        conn.commit()
        cursor.close()
        conn.close()



