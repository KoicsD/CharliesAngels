__author__ = 'viczmandi'
import csv

def store_donor(name, age, gender, birth_date, id, id_expiration,
                weight, blood_type, hemoglobin, last_donation,
                mobile, email):

    with open("DATA\donors.csv", "a", newline="") as csv_file:
        csv_file_writer = csv.writer(csv_file)
        csv_file_writer.writerow([name, age, gender, birth_date, id, id_expiration,
                weight, blood_type, hemoglobin, last_donation,
                mobile, email])