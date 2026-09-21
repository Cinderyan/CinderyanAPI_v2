#歐睿安版權所有
#CinderyanAPI
#calendar_section
#
#
#


from src.services.calendar_service.calendar_service import CalendarService

from datetime import date
import flet as ft

def create_calendar_section():
    today = date.today().isoformat()
    events = CalendarService.get_calendar_event(today)
    edit_button = ft.Button(
         content = "編輯",
         icon = ft.Icons.EDIT
    )
    header = ft.Row(
         controls = [
              ft.Text(
                   "今日代辦事項",
                   size = 20    
              ),
              edit_button
         ],
         alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    )
    controls = [
        header
    ]
    if len(events) == 0:
        controls.append(
            ft.Text("今日沒有代辦事項")
        )
    else:
        for event in events:
                controls.append(
                     ft.Text(
                          event[2]
                     )
                )
    return ft.Container(
         content = ft.Column(
              controls = controls
         ),
         padding = 20,
         border_radius = 12,
         bgcolor = ft.Colors.SURFACE_CONTAINER
    )
