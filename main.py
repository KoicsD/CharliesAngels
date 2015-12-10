import sql_handler
import data_handler
import menu
from sys import exit
from os import system
import json


config_file_path = "DATA/my_app.config"
menu.header = """
-----------------------------------------------------------------------
--- Welcome to the coolest donor and donation event managing system ---
-----------------------------------------------------------------------
"""


mode = "csv"
init_params = ()

main_menu = menu.Menu("Main menu", "Please, choose your action.")


def shutdown():
    system("cls")
    exit()


def read_config():
    global mode, init_params
    with open(config_file_path) as file_obj:
        data = json.loads(file_obj.read())
        mode = data["mode"]
        if mode == "db":
            init_params = (data["connection_params"],)


def initialize():
    global main_menu, mode, init_params
    read_config()
    if mode == "db":
        working_module = sql_handler
    else:
        working_module = data_handler
        init_params = ()
    working_module.initialize(*init_params)

    menu_1 = menu.MenuPoint("Add new donor", working_module.add_donor)
    main_menu.add_item(menu_1)

    menu_2 = menu.MenuPoint("Add new donation event", working_module.add_event)
    main_menu.add_item(menu_2)

    menu_3 = menu.MenuPoint("Delete donor", working_module.remove_donor)
    main_menu.add_item(menu_3)

    menu_4 = menu.MenuPoint("Delete a donation event", working_module.remove_event)
    main_menu.add_item(menu_4)

    menu_5 = menu.Menu("List donors or donations", "Please, choose if you want to list donors or donation events.")
    main_menu.add_item(menu_5)

    menu_5_1 = menu.MenuPoint("List donors", working_module.list_donors)
    menu_5.add_item(menu_5_1)

    menu_5_2 = menu.MenuPoint("List donation events", working_module.list_events)
    menu_5.add_item(menu_5_2)

    menu_6 = menu.Menu("Search in donors or donations",
                       "Please, choose if you want to search in donors or donation events.")
    main_menu.add_item(menu_6)

    menu_6_1 = menu.MenuPoint("Search in donors", working_module.search_in_donors)
    menu_6.add_item(menu_6_1)
    
    menu_6_2 = menu.MenuPoint("Search in events", working_module.search_in_events)
    menu_6.add_item(menu_6_2)

    menu_7 = menu.MenuPoint("Change Donor or Donation event", working_module.modify)
    main_menu.add_item(menu_7)

    menu_8 = menu.MenuPoint("Exit", shutdown)
    main_menu.add_item(menu_8)


def main():
    global main_menu
    while True:
        main_menu.load()


initialize()


if __name__ == '__main__':
    main()
