__author__ = 'Zoltan'
from search_in_files import calculate_age_in_year
import csv


def sorting_donor_by_order():
    with open('DATA/donors.csv', newline='') as donor_file:
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
        row_index = 1
        reader = csv.reader(donor_file)
        next(reader)
        lst = []
        if index == 1 or index == 9:
            lst = sorted(reader, key=lambda donor: int(donor[index]))
        else:
            lst = (sorted(reader, key=lambda donor: donor[index]))

        for row in lst:
            print("-" * 35)
            print(str(row_index) + ".")
            row_index += 1
            print("\t" + row[0])
            print("\t" + row[1] + " kg")
            print("\t" + row[3] + " - " + str(calculate_age_in_year(row[3])) + " years old")
            print("\t" + row[10])
            print("-" * 35)

def sorting_donation_by_order():
    with open('DATA/donations.csv', newline='') as donor_file:
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
        row_index = 1
        reader = csv.reader(donor_file)
        next(reader)
        lst = []
        if index == 0 or index == 7 or index == 8 or index ==9:
            lst = sorted(reader, key=lambda donor: int(donor[index]))
        else:
            lst = (sorted(reader, key=lambda donor: donor[index]))

        for row in lst:
            print("-" * 35)
            print(str(row_index) + ".")
            row_index += 1
            print("\t" + row[1])
            print("\t" + row[2] + "-" + row[3])
            print("\t" + row[4] + " " + row[5])
            print("\t" + row[6])
            print("-" * 35)

sorting_donation_by_order()