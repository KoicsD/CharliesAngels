from os import system
import csv
import data_handler
import donor_reg
import menu


def write_donors_modified_data_to_csv(list):
    with open("DATA/donors.csv", "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        for row in list:
            writer.writerow(row)


def donor_data_to_list(our_donors):
    our_donors = []
    with open('DATA/donors.csv', "r") as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            our_donors.append(row)
    return our_donors


def modify_donor(inp):
    newrow = []
    our_donors = []
    new_donors = []
    our_donors = donor_data_to_list(our_donors)
    id = inp
    if not any(e[6] == id for e in our_donors):
        print("ID not found!")
    for row in our_donors:
        newrow = []
        if id == row[6]:
            newrow = donor_reg.input_and_store_data(row)
        if not newrow:
            new_donors.append(row)
        else:
            new_donors.append(newrow)
            print("Donors data has been modified!")
        write_donors_modified_data_to_csv(new_donors)


modify_donor("123456AB")
