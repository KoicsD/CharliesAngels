from os import system
from time import sleep
import mysql.connector as sql
import donor_reg, event_reg
import sort_by_order


connection_obj = None
cursor_obj = None


def add_event():
    global connection_obj, cursor_obj
    try:
        new_event = event_reg.Donation.from_user()
        new_event.input_successful_donation()
        new_event.evaluate_event()
        cursor_obj.execute("INSERT INTO donations (" +
                           ", ".join(event_reg.Donation.header) +
                           ") VALUES (" +
                           ", ".join(["%s"] * len(event_reg.Donation.header)) +
                           ")",
                           new_event.to_lists())
        connection_obj.commit()
    except event_reg.UserInterrupt as interruption:
        print(interruption)
        sleep(1.5)


def add_donor():
    pass


def remove_event():
    pass


def remove_donor():
    pass


def list_events():
    sort_by_order.sorting_donation_by_order(cursor_obj=cursor_obj)


def list_donors():
    sort_by_order.sorting_donor_by_order(cursor_obj=cursor_obj)


def search_in_donors():
    pass


def search_in_events():
    pass


def modify():
    pass


def initialize(connection_data: dict):
    global connection_obj, cursor_obj
    connection_obj = sql.connect(**connection_data)
    cursor_obj = connection_obj.cursor()
    print("connection established!!!")


def shutdown():
    cursor_obj.close()
    connection_obj.close()
