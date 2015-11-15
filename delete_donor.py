__author__ = 'KoicsD'
from os import system
from time import sleep
import csv


donors_file = "DATA/donors.csv"


def delete_at(id: str):
    with open(donors_file, newline='') as file_obj:
        csv_obj = csv.reader(file_obj)
        rows = list(csv_obj)
        ids = [row[6] for row in rows[1:]]  # az 1 indexu (masodik) sortol kezdve minden sor 6 indexu eleme
        index = ids.index(id) + 1  # a fajlban 1-el tobbedik sorban van, mint ahanyadik elem az ids listaban (a fejlec miatt)
        rows.pop(index)

    with open(donors_file, 'w', newline='') as file_obj:
        csv_obj = csv.writer(file_obj)
        for row in rows:
            csv_obj.writerow(row)


def delete():
    s_id = ""
    while True:
        system("cls")
        s_id = input("Enter the personal ID of the donor you want to delete (for escape type 'q'):")
        if s_id == "q":
            return
        try:
            delete_at(s_id)
            print("Deleting donor successful.")
            sleep(1.5)
            break
        except ValueError:
            print("The given ID is not in the list.")
            sleep(1.5)
        except FileNotFoundError:
            print("Deleting donor unsuccessful because of file handling problems.")
            sleep(1.5)
            return
