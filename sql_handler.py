import mysql.connector as sql
import donor_reg, event_reg
from os import system
from time import sleep


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
    global connection_obj, cursor_obj
    add_donor = ("INSERT INTO Donation.donors "
               "(name,weight,gender,date_of_birth,last_donation,last_month_sickness,unique_identifier,expiration_of_id,blood_type,hemoglobin,email,mobil) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)")
    donors_data = donor_reg.main()
    cursor_obj.execute(add_donor, donors_data)
    connection_obj.commit()
    cursor_obj.close()
    connection_obj.close()


def remove_event():
    pass


def remove_donor():
    global connection_obj, cursor_obj
    id = input("Enter the personal ID of the donor you want to delete")
    cursor_obj.execute("DELETE FROM donation.donors WHERE unique_identifier = '%s'" % id)
    connection_obj.commit()
    cursor_obj.close()
    connection_obj.close()




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
