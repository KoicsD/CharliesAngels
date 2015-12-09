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


def print_current_data(list):
    print("Name: %s" % list[0])
    print("Weight: %s kg" % list[1])
    print("Gender: %s" % list[2])
    print("Date of Birth: %s" % list[3])
    print("Date of Last Donation: %s" % list[4])
    print("Last month sickness: %s" % list[5])
    print("Identifier: %s" % list[6])
    print("Expiration Date of ID: %s" % list[7])
    print("Type of Blood: %s" % list[8])
    print("Hemoglobin: %s" % list[9])
    print("Email: %s" % list[10])
    print("Mobile: %s" % list[11])


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
    if not any(e[6].lower() == id.lower() for e in our_donors):
        print("ID not found!")
    else:
        for row in our_donors:
            newrow = []
            if id.lower() == row[6].lower():
                print_current_data(row)
                try:
                    newrow = donor_reg.input_and_store_data()
                except donor_reg.UserInterrupt as interruption:
                    newrow = []
                    print(str(interruption))
            if not newrow:
                new_donors.append(row)
            else:
                new_donors.append(newrow)
                print("Donors data has been modified!")
    if new_donors == our_donors or len(new_donors) < len(our_donors):
        write_donors_modified_data_to_csv(our_donors)
    else:
        write_donors_modified_data_to_csv(new_donors)

if __name__ == '__main__':
    modify_donor("123654AS")
