#歐睿安版權所有
#CinderyanAPI
#calendar_section
#
#
#

import flet as ft

def create_calendar_section():
    return ft.Container(
        content = ft.Column(
            controls = [
                ft.Text(
                    "今日代辦事項",
                    size = 20
                ),
                ft.Text("目前沒有代辦事項")
            ]
        ),
        padding = 20,
        border_radius = 12,
        bgcolor = ft.Colors.SURFACE_CONTAINER
    )