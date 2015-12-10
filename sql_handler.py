import mysql.connector as sql
import donor_reg, event_reg


connection_obj = None
cursor_obj = None


def add_event():
    pass


def add_donor():
    pass


def remove_event():
    pass


def remove_donor():
    pass


def list_events():
    pass


def list_donors():
    pass


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
