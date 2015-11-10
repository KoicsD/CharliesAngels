__author__ = 'ozsvarmarton'
import event_reg
import donor_reg
from random import randint


our_events = {}
our_donors = {}


def read():
    with open("DATA/event.csv", "r") as file_obj:
        data = file_obj.readlines()
        for item in data:
            pass

def write():
    with open("DATA/event.csv", "w") as file_obj:
        for key, event in our_events.items():
            file_obj.write(key + "," + event.to_csv() + "\n")

def add_event():
    new_event = event_reg.Donation()
    while True:
        new_key = hex(randint(0, 16 ** 4 - 1))
        if new_key not in our_events.keys():
            break
    our_events[new_key] = new_event
