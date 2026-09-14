#歐睿安版權所有
#CinderyanAPI
#main
#
#
#

import database
from src.ui.app import run_app

import flet as ft

if __name__ == "__main__":
    database.calendar_init()
    database.time_tracker_init()
    database.deadline_init()
    ft.run(run_app)