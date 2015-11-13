__author__ = 'ozsvarmarton'
import event_reg
import donor_reg
import List_donors
import search_in_files
import csv
from os import system
from time import sleep


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
    donor_reg.main()


# remover functions:
def remove_event_at(index: int):
    global our_events
    clone_events = our_events.copy()
    our_events.pop(index)
    write()
    our_events = clone_events


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


# lister functions:
def list_events():
    pass


def list_donors():
    List_donors.main()


# searcher functions:
def search_in_donors():
    search_in_files.search_in_donors()


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
    print("Adding 2 events:")
    print("First...")
    add_event()
    print("Second...")
    add_event()
    print("Done.")
    print("Removing 2nd element...")
    remove_event()
    print("Done.")
    print("Adding another element...")
    add_event()
    print("Done.")
    print("Demo terminates.")


# on start-up calling initializer:
initialize()


# in main mode running demo:
if __name__ == '__main__':
    demo()
