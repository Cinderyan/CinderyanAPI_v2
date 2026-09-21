#歐睿安版權所有
#CinderyanAPI
#time_tracker_section
#
#
#

from src.services.time_tracker_service.time_tracker_service import TimeTrackerService

from datetime import date
import flet as ft

def create_time_tracker_section():
    today = date.today().isoformat()
    time_trackers = TimeTrackerService.get_time_tracker_entry(today)
    controls = [
        ft.Text(
            "時間紀錄",
            size = 20
        )
    ]
    if len(time_trackers) == 0:
        controls.append(
            ft.Text(
                "Study: 0 hr\nWork : 0 hr"
            )
        )
    else:
        for time_tracker in time_trackers:
            controls.append(
                ft.Text(
                    f"Study: {time_tracker[3]} hrs\nWork : {time_tracker[2]} hrs"
                )
            )
    return ft.Container(
        ft.Column(
            controls = controls
        ),
        padding = 20,
        border_radius = 12,
        bgcolor = ft.Colors.SURFACE_CONTAINER
    )
    