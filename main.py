#歐睿安版權所有
#CinderyanAPT
#main
#
#
#

from src.models.calendar_event.calendar_event import CalendarEvent
from src.models.time_tracker.time_tracker import TimeTracker
from src.services.calendar_service.calendar_service import CalendarService
from src.services.time_tracker_service.time_tracker_service import TimeTrackerService  
import database

database.calendar_init()
database.time_tracker_init()