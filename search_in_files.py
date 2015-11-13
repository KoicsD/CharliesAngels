__author__ = 'Zoltan'
import csv
from datetime import datetime, date

def calculate_age_in_year(birth_date):
    bdate = datetime.strptime(str(birth_date), "%Y.%m.%d").date()
    return (datetime.now().date() - bdate).days // 365

def search_in_donors():
    search_term = input("Search term: ")
    with open('DATA\donors.csv', newline='') as file:
        reader = csv.reader(file)
        index = 0
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

# print(search_in_donors())