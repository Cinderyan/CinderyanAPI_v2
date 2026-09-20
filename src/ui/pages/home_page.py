#歐睿安版權所有
#CinderyanAPI
#home_page
#
#
#

from src.ui.components.calendar_section import create_calendar_section
from src.ui.components.time_tracker_section import create_time_tracker_section
from src.ui.components.deadline_section import create_deadline_section


import flet as ft

def create_home_page(show_calendar):
    title = ft.Text(
        "睿安，您好",
        size = 30
    )
    view_calendar_button = ft.Button(
        content = ft.Text("檢視月曆"),
        on_click = show_calendar
    )
    header = ft.Row(
        controls = [
            title, 
            view_calendar_button
        ],
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    )
    calendar_section = create_calendar_section()
    deadline_section = create_deadline_section()
    time_tracker_section = create_time_tracker_section()
    home = ft.Column(
        controls = [
            header, 
            calendar_section,
            deadline_section,
            time_tracker_section
        ]
    )
    return home