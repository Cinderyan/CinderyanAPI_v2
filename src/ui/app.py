#歐睿安版權所有
#CinderyanAPI
#app
#
#
#

from src.ui.pages.home_page import create_home_page
from src.ui.pages.calendar_page import create_calendar_page

import flet as ft

def run_app(page: ft.Page):
    page.title = "CinderyanAPI"
    def show_home(e = None):
        page.clean()
        page.add(
            create_home_page(show_calendar)
        )
    def show_calendar(e = None):
        page.clean()
        page.add(
            create_calendar_page(show_home)
        )
    show_home()

