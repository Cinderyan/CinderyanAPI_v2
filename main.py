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
database.time_tracker_init()