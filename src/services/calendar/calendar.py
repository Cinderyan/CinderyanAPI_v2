#歐睿安版權所有
#CinderyanAPT
#calender
#
#
#

from src.models.calendar_event.calendar_event import CalendarEvent
from src.models.time_tracker.time_tracker import TimeTracker
from datetime import date
import sqlite3

calendar_db_path = "data/calendar_data.db"
calendar = sqlite3.connect(calendar_db_path)
calendar.close()
