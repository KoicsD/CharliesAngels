__author__ = 'viczmandi'
import csv


def store_donor(data):
    name,weight,gender,birth_date,last_donation,was_sick_in_last_month,\
    id,id_expiration,blood_type,hemoglobin,email,mobile = data
    with open("DATA/donors.csv", "a", newline="") as csv_file:
        csv_file_writer = csv.writer(csv_file)
        csv_file_writer.writerow([name,weight,gender,birth_date,
                                 last_donation,was_sick_in_last_month,
                                 id,id_expiration,
                                 blood_type,hemoglobin,email,mobile])