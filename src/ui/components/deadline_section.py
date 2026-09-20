#歐睿安版權所有
#CinderyanAPI
#deadline_section
#
#
#

import flet as ft

def create_deadline_section():
    return ft.Container(
        content = ft.Column(
            controls = [
                ft.Text(
                    "即將到期事件",
                    size = 20
                ),
                ft.Text(
                    "目前沒有即將到期事件"
                )
            ]
        ),
        padding = 20,
        border_radius = 12,
        bgcolor = ft.Colors.SURFACE_CONTAINER
    )