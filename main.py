import data_handler
import menu
from sys import exit
from os import system


menu.header = """
-----------------------------------------------------------------------
--- Welcome to the coolest donor and donation event managing system ---
-----------------------------------------------------------------------
"""


main_menu = menu.Menu("Main menu", "Please, choose your action.")


def shutdown():
    system("cls")
    exit()


def initialize():
    global main_menu

    menu_1 = menu.MenuPoint("Add new donor", data_handler.add_donor)
    main_menu.add_item(menu_1)

    menu_2 = menu.MenuPoint("Add new donation event", data_handler.add_event)
    main_menu.add_item(menu_2)

    menu_3 = menu.MenuPoint("Delete donor", data_handler.remove_donor)
    main_menu.add_item(menu_3)

    menu_4 = menu.MenuPoint("Delete a donation event", data_handler.remove_event)
    main_menu.add_item(menu_4)

    menu_5 = menu.Menu("List donors or donations", "Please, choose if you want to list donors or donation events.")
    main_menu.add_item(menu_5)

    menu_5_1 = menu.MenuPoint("List donors", data_handler.list_donors)
    menu_5.add_item(menu_5_1)

    menu_5_2 = menu.MenuPoint("List donation events", data_handler.list_events)
    menu_5.add_item(menu_5_2)

    menu_6 = menu.Menu("Search in donors or donations",
                       "Please, choose if you want to search in donors or donation events.")
    main_menu.add_item(menu_6)

    menu_6_1 = menu.MenuPoint("Search in donors", data_handler.search_in_donors)
    menu_6.add_item(menu_6_1)
    
    menu_6_2 = menu.MenuPoint("Search in events", data_handler.search_in_events)
    menu_6.add_item(menu_6_2)

    menu_7 = menu.MenuPoint("Change Donor or Donation event", data_handler.modify)
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
