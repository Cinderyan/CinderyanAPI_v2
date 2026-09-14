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
        ]
    )
    calendar_section = ft.Container(
        content = ft.Text("今日代辦事項"),
        padding = 20
    )
    deadline_section = ft.Container(
        content = ft.Text("將於今日截止的事件"),
        padding = 20
    )
    time_tracker_section = ft.Container(
        content = ft.Text("今日時間紀錄"),
        padding = 20
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

    

