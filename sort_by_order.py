__author__ = 'Zoltan'
from datetime import date, time
import csv
import mysql.connector as sql
from search_in_files import calculate_age_in_year


date_format = "%Y.%m.%d."


class SortingAsker:
    donor_header = ["name", "weight", "gender", "date_of_birth", "last_donation", "last_month_sickness",
                    "unique_identifier", "expiration_of_id", "blood_type", "hemoglobin", "email", "mobil"]

    donation_header = ["id", "date_of_event", "start_time", "end_time", "zip_code", "city", "address",
                       "number_of_available_beds", "planned_donor_number", "final_donor_number"]


    @staticmethod
    def ask_donor_question():
        index = input('What will donors get ordered by?'+'\n'
                          'name:0,'+'\n'
                          'weight:1'+'\n'
                          'gender:2'+'\n'
                          'date_of_birth:3'+'\n'
                          'last_donation:4'+'\n'
                          'last_month_sickness:5'+'\n'
                          'unique_identifier:6'+'\n'
                          'expiration_of_id:7'+'\n'
                          'blood_type:8'+'\n'
                          'hemoglobin:9'+'\n'
                          'email:10'+'\n'
                          'mobil:11')
        list_of_index = ['0','1','2','3','4','5','6','7','8','9','10','11']
        if index not in list_of_index:
            index=0
        else:
            index=int(index)
        return index

    @staticmethod
    def ask_donation_question():
        index = input('What will donations get ordered by?' + '\n'
                      'id:0'+ '\n'
                      'date_of_event:1'+ '\n'
                      'start_time:2'+ '\n'
                      'end_time:3'+ '\n'
                      'zip_code:4'+ '\n'
                      'city:5'+ '\n'
                      'address:6'+ '\n'
                      'number_of_available_beds:7'+ '\n'
                      'planned_donor_number:8'+ '\n'
                      'final_donor_number:9')
        list_of_index = ['0','1','2','3','4','5','6','7','8','9','10','11']
        if index not in list_of_index:
            index=0
        else:
            index=int(index)
        return index


class CsvLister:
    @staticmethod
    def list_donors(ord_index, path='DATA/donors.csv'):
        with open(path, newline='') as donor_file:
            row_index = 1
            reader = csv.reader(donor_file)
            next(reader)
            lst = []
            if ord_index == 1 or ord_index == 9:
                lst = sorted(reader, key=lambda donor: int(donor[ord_index]))
            else:
                lst = (sorted(reader, key=lambda donor: donor[ord_index].lower()))

            for row in lst:
                print("-" * 35)
                print(str(row_index) + ".")
                row_index += 1
                print("\t" + row[0])
                print("\t" + row[1] + " kg")
                print("\t" + row[3] + " - " + str(calculate_age_in_year(row[3])) + " years old")
                print("\t" + row[10])
                print("-" * 35)
                if row_index > len(lst):
                    input("Press enter to return to main menu.")
                elif row_index % 4 == 0:
                    input("Press enter to list more donors.")
            if len(lst) == 0:
                input("Empty list! Press enter to return to main menu.")

    @staticmethod
    def list_donations(ord_index, path='DATA/donations.csv'):
        with open(path, newline='') as donor_file:
            row_index = 1
            reader = csv.reader(donor_file)
            next(reader)
            lst = []
            if ord_index == 0 or ord_index == 7 or ord_index == 8 or ord_index ==9:
                lst = sorted(reader, key=lambda donor: int(donor[ord_index]))
            else:
                lst = (sorted(reader, key=lambda donor: donor[ord_index].lower()))

            for row in lst:
                print("-" * 35)
                print(str(row_index) + ".")
                row_index += 1
                print("\t" + row[1])
                print("\t" + row[2] + "-" + row[3])
                print("\t" + row[4] + " " + row[5])
                print("\t" + row[6])
                print("-" * 35)
                if row_index > len(lst):
                    input("Press enter to return to main menu.")
                elif row_index % 4 == 0:
                    input("Press enter to list more donation events.")
            if len(lst) == 0:
                input("Empty list! Press enter to return to main menu.")


class SqlLister:
    @staticmethod
    def type_equalizer(inp_list: list):
        ret_list = []
        for item in inp_list:
            if type(item) == str:
                ret_list.append(item)
            elif type(item) == int:
                ret_list.append(str(item))
            elif type(item) == date:
                ret_list.append(item.strftime(date_format))
            elif type(item) == time:
                ret_list.append(item.strftime("%H:%M"))
        return ret_list

    @staticmethod
    def list_donors(ord_index, cursor):
        cursor.execute("SELECT * FROM Donors ORDER BY " + SortingAsker.donor_header[ord_index] + " ASC")
        ans = cursor.fetchall()
        row_index = 1
        for record in ans:
            row = SqlLister.type_equalizer(record)
            print("-" * 35)
            print(str(row_index) + ".")
            row_index += 1
            print("\t" + row[0])
            print("\t" + row[1] + " kg")
            print("\t" + row[3] + " - " + str(calculate_age_in_year(row[3])) + " years old")
            print("\t" + row[10])
            print("-" * 35)
            if row_index > len(ans):
                input("Press enter to return to main menu.")
            elif row_index % 4 == 0:
                input("Press enter to list more donors.")
            if len(ans) == 0:
                input("Empty list! Press enter to return to main menu.")

    @staticmethod
    def list_donations(ord_index, cursor):
        cursor.execute("SELECT * FROM Donations ORDER BY " + SortingAsker.donation_header[ord_index] + " ASC")
        ans = cursor.fetchall()
        row_index = 1
        for record in ans:
            row = SqlLister.type_equalizer(record)
            print("-" * 35)
            print(str(row_index) + ".")
            row_index += 1
            print("\t" + row[1])
            print("\t" + row[2] + "-" + row[3])
            print("\t" + row[4] + " " + row[5])
            print("\t" + row[6])
            print("-" * 35)
            if row_index > len(ans):
                input("Press enter to return to main menu.")
            elif row_index % 4 == 0:
                input("Press enter to list more donors.")
            if len(ans) == 0:
                input("Empty list! Press enter to return to main menu.")


def sorting_donor_by_order(file_path='DATA/donors.csv', cursor_obj=None):
    if cursor_obj is None:
        CsvLister.list_donors(SortingAsker.ask_donor_question(), file_path)
    else:
        SqlLister.list_donors(SortingAsker.ask_donor_question(), cursor_obj)


def sorting_donation_by_order(file_path='DATA/donations.csv', cursor_obj=None):
    if cursor_obj is None:
        CsvLister.list_donations(SortingAsker.ask_donation_question(), file_path)
    else:
        SqlLister.list_donations(SortingAsker.ask_donation_question(), cursor_obj)


if __name__ == '__main__':
    sorting_donor_by_order()
    sorting_donation_by_order()
