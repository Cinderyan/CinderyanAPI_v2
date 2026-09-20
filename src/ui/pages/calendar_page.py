#歐睿安版權所有
#CinderyanAPI
#calendar_page
#
#
#

import flet as ft

def create_calendar_page(show_home):
    back_today_button = ft.Button(
        content = ft.Text("回到今天"),
        on_click = show_home
    )
    title = ft.Text(
        "月曆",
        size = 30
    )
    calendar_page = ft.Column(
        controls =  [
            ft.Row(
                controls = [
                    back_today_button,
                    title
                ]
            ),
            ft.Text(
                "這裡之後會顯示整個月曆的CalendarEvent跟Deadline"
            )
        ]
    )
    return calendar_page