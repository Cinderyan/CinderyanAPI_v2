#歐睿安版權所有
#CinderyanAPI
#time_tracker_section
#
#
#

import flet as ft

def create_time_tracker_section():
    return ft.Container(
        content = ft.Column(
            controls = [
                ft.Text(
                    "時間紀錄",
                    size = 20
                ),
                ft.Text(
                    "Study: 0 hr"
                ),
                ft.Text(
                    "Work: 0 hr"
                )
            ]
        ),
        padding = 20,
        border_radius = 12,
        bgcolor = ft.Colors.SURFACE_CONTAINER
    )

    