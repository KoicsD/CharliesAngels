__author__ = 'ozsvarmarton'
from os import system
from time import sleep
import event_reg
import donor_reg
import sort_by_order
import delete_donor
import search_in_files
import csv
import modify_donor_data
import donor_csv_writer
# import menu


header = """
-----------------------------------------------------------------------
--- Welcome to the coolest donor and donation event managing system ---
-----------------------------------------------------------------------
"""


event_file = "DATA/donations.csv"


# list of donation events:
our_events = []


# data-reader and writer functions:
def read():
    with open(event_file, "r", newline='') as file_obj:
        new_events = []
        reader = csv.reader(file_obj)
        # assert header.index("id") == 0
        next(reader)
        for row in reader:
            data = row[1:]
            new_events.append(event_reg.Donation.from_lists(data))
    global our_events
    our_events.clear()
    our_events += new_events


def write():
    with open(event_file, "w", newline='') as file_obj:
        global our_events
        writer = csv.writer(file_obj)
        writer.writerow(["id"] + event_reg.Donation.header)
        for ind in range(len(our_events)):
            writer.writerow([str(ind + 1)] + our_events[ind].to_lists())


# adder functions:
def add_event():
    global our_events
    err_msg = "Adding donation event unsuccessful.\nReason:\n%s"
    try:
        new_event = event_reg.Donation.from_user()
        new_event.input_successful_donation()
        new_event.evaluate_event()
        our_events.append(new_event)
        write()
    except event_reg.UserInterrupt as interruption:
        print(err_msg % str(interruption))
        sleep(1.5)
    except FileNotFoundError:
        our_events.pop()
        print(err_msg % "File cannot be written.")
        sleep(1.5)


def add_donor():
    data = donor_reg.main()
    if data:
        donor_csv_writer.store_donor(data)


# remover functions:
def remove_event_at(index: int):
    global our_events
    clone_events = our_events.copy()
    our_events.pop(index)
    try:
        write()
    except FileNotFoundError as err:
        our_events = clone_events
        raise err


def remove_event():
    err_msg = "Deleting donation event unsuccessful.\nReason:\n%s"
    s_index = ""
    p_index = 0
    while True:
        system("cls")

        s_index = input("Which item would you like to remove? (type 'q' for returning to main menu) :")
        if s_index == 'q':
            return
        try:
            p_index = int(s_index) - 1
            remove_event_at(p_index)
            print("Deleting donation event successful.")
            sleep(1.5)
            break
        except ValueError:
            print(err_msg % "Input cannot be parsed as an integer!")
        except IndexError:
            print(err_msg % "No donation event with such an index in database.")
        except FileNotFoundError:
            print(err_msg % "Modifications cannot be saved to file.")
        sleep(1.5)


def remove_donor():
    delete_donor.delete()


# lister functions:
def list_events():
    global our_events
    err_msg = "Error while listing donors\n%s"
    try:
        sort_by_order.sorting_donation_by_order()
    except ValueError as lister_error:
        system("cls")
        print(err_msg % "ValueError\n%" % str(lister_error))
    except IndexError as lister_error:
        system("cls")
        print(err_msg % "IndexError" % str(lister_error))


def list_donors():
    err_msg = "Error while listing donors\n%s"
    try:
        sort_by_order.sorting_donor_by_order()
    except FileNotFoundError as lister_error:
        system("cls")
        print(err_msg % "File cannot be found\n%s" % str(lister_error))
    except ValueError as lister_error:
        system("cls")
        print(err_msg % "ValueError\n%" % str(lister_error))
    except IndexError as lister_error:
        system("cls")
        print(err_msg % "IndexError" % str(lister_error))
    finally:
        sleep(1.5)


# searcher functions:
def search_in_donors():
    err_msg = "Error while searching in donors\n%s"
    try:
        search_in_files.search_in_donors()
    except FileNotFoundError as searcher_error:
        system("cls")
        print(err_msg % "File cannot be found\n%s" % str(searcher_error))
    except ValueError as searcher_error:
        system("cls")
        print(err_msg % "ValueError\n%" % str(searcher_error))
    except IndexError as searcher_error:
        system("cls")
        print(err_msg % "IndexError" % str(searcher_error))
    finally:
        sleep(1.5)


def search_in_events():
    err_msg = "Error while searching in donors\n%s"
    try:
        search_in_files.search_in_events()
    except FileNotFoundError as searcher_error:
        system("cls")
        print(err_msg % "File cannot be found\n%s" % str(searcher_error))
    except ValueError as searcher_error:
        system("cls")
        print(err_msg % "ValueError\n%" % str(searcher_error))
    except IndexError as searcher_error:
        system("cls")
        print(err_msg % "IndexError" % str(searcher_error))
    finally:
        sleep(1.5)


# changer:
def modify_event(event):
    system('cls')
    print(header)
    print("Donation to modify:")
    print(event)
    event = event_reg.Donation.from_user()
    event.input_successful_donation()
    event.evaluate_event()
    return event


def modify():
    global our_events
    system('cls')
    print(header)
    inp = input("Please, enter the id of Donor or Donation you want to modify:")
    if inp.isdigit():
        i = int(inp) - 1
        if i in range(len(our_events)):
            try:
                events = our_events.copy()
                our_events[i] = modify_event(our_events[i])
                write()
                print("Donation event data successfully modified!")
                sleep(1.5)
            except event_reg.UserInterrupt:
                print("Input interrupted by user")
                sleep(1)
            except FileNotFoundError:
                our_events = events
                print("File cannot be written")
                sleep(2)
        else:
            print("Id number is not found in list of Donations!")
            sleep(1.5)
    elif donor_reg.validate_identifier(inp):
        if donor_reg.is_id_unique(inp):
            print("The given ID is not in data-base!")
        else:
            modify_donor_data.modify_donor(inp)
        sleep(1.5)
    else:
        print("Input cannot be parsed as an id of either a Donor or an Donation event.")
        sleep(1.5)


# initializer (on start-up we need to read the files):
def initialize():
    try:
        read()
    except FileNotFoundError:
        system("cls")
        print(header)
        print("Error: File cannot be read. Database stays empty in memory.")
        sleep(1)
    except ValueError:
        system("cls")
        print(header)
        print("Error: File cannot be read. Database stays empty in memory.")
        sleep(1)
    except IndexError:
        system("cls")
        print(header)
        print("Error: File cannot be read. Database stays empty in memory.")
        sleep(1)


# demo for stand-alone running:
def demo():
    # print("Adding 2 events:")
    # print("First...")
    # add_event()
    # print("Second...")
    # add_event()
    # print("Done.")
    # print("Removing 2nd element...")
    # remove_event()
    # print("Done.")
    # print("Adding another element...")
    # add_event()
    # print("Done.")

    # print("Listing donors...")
    # list_donors()
    # print("Adding new donor...")
    # donor_reg.main()
    # print("Done.")
    # print("Listing donors.")
    # list_donors()
    # print("Deleting one donor...")
    # remove_donor()
    # print("Done.")
    # print("Listing donors again.")
    # list_donors()
    # print("Demo terminates.")

    modify()


# in main mode running demo:
if __name__ == '__main__':
    demo()
