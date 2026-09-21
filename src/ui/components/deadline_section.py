#歐睿安版權所有
#CinderyanAPI
#deadline_section
#
#
#

from src.services.deadline_service.deadline_service import DeadlineService

from datetime import date
import flet as ft

def create_deadline_section():
    today = date.today().isoformat()
    deadlines = DeadlineService.get_deadline(today)
    controls = [
        ft.Text(
            "今日即將到期事件",
            size = 20
        )
    ]
    if len(deadlines) == 0:
        controls.append(
            ft.Text("今日沒有即將到期事件")
        )
    else:
        for deadline in deadlines:
            controls.append(
                ft.Text(
                    deadline[2]
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