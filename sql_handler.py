from os import system
from time import sleep
import mysql.connector as sql
from mysql.connector import errorcode, cursor, connection
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
        cursor_obj.execute("INSERT INTO Donations (" +
                           ", ".join(event_reg.Donation.header) +
                           ") VALUES (" +
                           ", ".join(["%s"] * len(event_reg.Donation.header)) +
                           ")",
                           new_event.to_lists())
        connection_obj.commit()
        print("New event stored successfully")
    except event_reg.UserInterrupt as interruption:
        print(interruption)
    except sql.Error as err:
        print(err)
    sleep(3)


def add_donor():
    global connection_obj, cursor_obj
    add_donor = ("INSERT INTO Donors "
               "(name,weight,gender,date_of_birth,last_donation,last_month_sickness,unique_identifier,expiration_of_id,blood_type,hemoglobin,email,mobil) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)")
    donors_data = donor_reg.main()
    if donors_data is not None:
        try:
            cursor_obj.execute(add_donor, donors_data)
            connection_obj.commit()
            print("New donor stored successfully")
        except sql.Error as err:
            print(err)
        sleep(3)


def remove_event_at(index: int):
    global connection_obj, cursor_obj
    cursor_obj.execute("SELECT COUNT(*) FROM Donations WHERE id = %s", (index,))
    ans = cursor_obj.fetchall()
    if ans[0][0]:
        cursor_obj.execute("DELETE FROM Donations WHERE id = %s", (index,))
        connection_obj.commit()
    else:
        raise KeyError("Key '%d' not in database!" % index)


def remove_event():
    while True:
        s_id = input("Please enter the id of donation event: ")
        if s_id == 'q':
            print("Operation interrupted by User")
            break
        try:
            p_id = int(s_id)
            remove_event_at(p_id)
            print("Donation deleted successfully")
            break
        except KeyError as err:
            print(err)
        except ValueError:
            print("input cannot be parsed as integer!")
        except sql.Error as err:
            print(err)
            print("Error code: %d" % err.errno)
        finally:
            sleep(3)
    sleep(3)


def remove_donor():
    global connection_obj, cursor_obj
    while True:
        id = input("Enter the personal ID of the donor you want to delete")
        if id == 'q':
            print("Operation interrupted by User")
            break
        try:
            cursor_obj.execute("SELECT COUNT(*) FROM Donations WHERE id = %s", (id,))
            ans = cursor_obj.fetchall()
            if ans[0][0]:
                cursor_obj.execute("DELETE FROM Donors WHERE unique_identifier = '%s'" % id)
                connection_obj.commit()
                print("Donor object removed successfully")
                break
            else:
                print("Key '%s' not in database!" % id)
                sleep(3)
        except sql.Error as err:
            print(err)
            sleep(3)
    sleep(3)


def list_events():
    try:
        sort_by_order.sorting_donation_by_order(cursor_obj=cursor_obj)
    except sql.Error as err:
        print(err)
        sleep(3)


def list_donors():
    try:
        sort_by_order.sorting_donor_by_order(cursor_obj=cursor_obj)
    except sql.Error as err:
        print(err)
        sleep(3)


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
