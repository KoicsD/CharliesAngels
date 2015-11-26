__author__ = 'Zoltan'
import csv
from datetime import datetime
date_format = "%Y.%m.%d."


def calculate_age_in_year(birth_date):
    bdate = datetime.strptime(str(birth_date), date_format).date()
    return (datetime.now().date() - bdate).days // 365


def search_in_donors():
    search_term = input("Search term: ")
    with open('DATA\donors.csv', newline='') as file:
        reader = csv.reader(file)
        index = 0
        next(reader)
        for row in reader:
            for i in row:
                if search_term in i:
                    index += 1
                    print("-"*35)
                    print(str(index) + ".")
                    print("\t" + row[0])
                    print("\t" + row[1] + " kg")
                    print("\t" + row[3] + " - " + str(calculate_age_in_year(row[3])) + " years old")
                    print("\t" + row[10])
                    print("-" * 35)
                    next_page = input("Press enter to next hit or enter 'exit' to return to the main menu.")
                    if next_page.lower() == "exit":
                        return
                    break
        print("Searching reached its end. Press Enter to return to main menu.")
        input("")


def search_in_events():
    search_term = input("Search term: ")
    with open('DATA\donations.csv', newline='') as file:
        reader = csv.reader(file)
        index = 0
        next(reader)
        for row in reader:
            for i in row:
                if search_term.lower() in i.lower():
                    index += 1
                    print("-"*35)
                    print(str(index) + ".")
                    print("\t" + row[1])
                    print("\t" + row[2] + "-" + row[3])
                    print("\t" + row[4] + " " + row[5])
                    print("\t" + row[6])
                    print("-" * 35)
                    next_page = input("Press enter to next hit or enter 'exit' to return to the main menu.")
                    if next_page.lower() == "exit":
                        return
                    break
        print("Searching reached its end. Press Enter to return to main menu.")
        input("")
