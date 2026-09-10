#歐睿安版權所有
#CinderyanAPT
#calendar_event
#
#
#

class CalendarEvent:
    def __init__(self, date, title, description, status):
        self.date = date
        self.title = title
        self.description = description
        self.status = status

    def change_status(self, new_status):
        self.status = new_status

    