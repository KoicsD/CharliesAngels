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


def donor_id_donor_data(list, id):
    return id == list[6]


def modify_donor():
    newrow = []
    our_donors = []
    new_donors = []
    our_donors = donor_data_to_list(our_donors)
    id = "123456AB"
    for row in our_donors:
        newrow = []
        if donor_id_donor_data(row, id):
            newrow = donor_reg.input_and_store_data(row)
        if not newrow:
            new_donors.append(row)
        else:
            new_donors.append(newrow)
    write_donors_modified_data_to_csv(new_donors)

modify_donor()

