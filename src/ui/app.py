#歐睿安版權所有
#CinderyanAPI
#app
#
#
#

import flet as ft

def run_app(page: ft.Page):
    page.title = "CinderyanAPI"
    title = ft.Text(
        "睿安，您好",
        size = 30
    )
    view_calendar_button = ft.Button(
        content = "檢視月曆"
    )
    header = ft.Row(
        controls = [
            title,
            view_calendar_button    
        ],
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    )
    calendar_section = ft.Container(
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
    deadline_section = ft.Container(
        content = ft.Column(
            controls = [
                ft.Text(
                    "即將到期事件",
                    size = 20
                ),
                ft.Text("目前沒有即將到期事件")
            ]
        ),
        padding = 20,
        border_radius = 12,
        bgcolor = ft.Colors.SURFACE_CONTAINER
    )
    time_tracker_section = ft.Container(
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
    home = ft.Column(
        controls = [
            header,
            calendar_section,
            deadline_section,
            time_tracker_section
        ]
    )
    page.add(home)

    

