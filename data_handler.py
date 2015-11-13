__author__ = 'ozsvarmarton'
import event_reg
import csv


our_events = []


def read():
    with open("DATA/donations.csv", "r", newline='') as file_obj:
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
    with open("DATA/donations.csv", "w", newline='') as file_obj:
        global our_events
        writer = csv.writer(file_obj)
        writer.writerow(["id"] + event_reg.Donation.header)
        for ind in range(len(our_events)):
            writer.writerow([str(ind + 1)] + our_events[ind].to_lists())


def add_event():
    err_msg = "Adding donation event unsuccessful.\nReason:\n%s"
    try:
        new_event = event_reg.Donation.from_user()
        our_events.append(new_event)
        write()
    except event_reg.UserInterrupt as interruption:
        print(err_msg % str(interruption))
    except FileNotFoundError:
        our_events.pop()
        print(err_msg % "File cannot be written.")

def remove_event(index: int):
    global our_events
    our_events.pop(index - 1)
    write()


def demo():
    print("Adding 2 events:")
    print("First...")
    add_event()
    print("Second...")
    add_event()
    print("Done.")
    print("Removing 2nd element...")
    remove_event(2)
    print("Done.")
    print("Adding another element...")
    add_event()
    print("Done.")
    print("Demo terminates.")


try:
    read()
except FileNotFoundError:
    print("Error: File cannot be read. Database stays empty in memory.")


if __name__ == '__main__':
    demo()
