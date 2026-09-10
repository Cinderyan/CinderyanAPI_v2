#歐睿安版權所有
#CinderyanAPT
#main
#
#
#

from src.models.calendar_event.calendar_event import CalendarEvent
from src.models.time_tracker.time_tracker import TimeTracker
from src.services.calendar.calendar import Calendar
import database

database.calendar_init()
event1 = CalendarEvent("2024-06-01", "Meeting with Team", "Discuss project updates", "scheduled")
Calendar.add_calendar_event(event1)

