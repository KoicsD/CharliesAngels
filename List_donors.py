import csv
from datetime import datetime
date_format = "%Y.%m.%d."


def listing():
    with open('DATA\donors.csv', newline='') as file:
        reader = csv.reader(file)
        index = 1
        next_page = ""
        for row in reader:
            if "name" in row:
                continue
            next_page = input("""
--------------------------------------------------------------------
Press enter to next page or enter 'exit' to return to the main menu.
--------------------------------------------------------------------""")
            print(str(index) + ". page")
            index += 1
            result = []
            if next_page.lower() == "exit":
                return
            for item in row:
                result.append(item)
            print_donors_data(index, result)
        print("-" * 39)
        exit = input("Press enter to return to the main menu.")
        print("-" * 39)


def print_donors_data(index, result):
        print(result[0])
        print(result[1] + "kg")
        print(result[3] + " - " + str(calculate_age_in_year(result[3])) + " years old")
        print(result[10])


def calculate_age_in_year(birth_date):
    bdate = datetime.strptime(str(birth_date), date_format).date()
    return (datetime.now().date() - bdate).days // 365


def check_if_donors_list_empty():
    file = open('DATA\donors.csv', "r", )
    reader = csv.reader(file)
    if len(list(reader)) == 1:
        print("List of Donors empty!")
        return
    file.close()


def list_events(our_events):
    if len(our_events) == 0:
        print("The list of donation event is empty!")
        return
    index = 1
    next_page = ""
    for event in our_events:
        next_page = input("""
--------------------------------------------------------------------
Press enter to next page or enter 'exit' to return to the main menu.
--------------------------------------------------------------------""")
        print(str(index) + ". page")
        index += 1
        if next_page.lower() == "exit":
            return
        print_event(event)
    print("-" * 39)
    exit = input("Press enter to return to the main menu.")
    print("-" * 39)

def print_event(event):
    data = event.to_lists()
    print(data[0])
    print(data[1] + " - " + data[2])
    print(data[3] + " " + data[4])
    print(data[5])


def main():
    check_if_donors_list_empty()
    listing()

if __name__ == "__main__":
    main()