import mysql.connector as sql
import donor_reg, event_reg


connection_obj = None
cursor_obj = None


def initialize(connection_data: dict):
    global connection_obj, cursor_obj
    connection_obj = sql.connect(**connection_data)
    cursor_obj = connection_obj.cursor()
    print("connection established!!!")
