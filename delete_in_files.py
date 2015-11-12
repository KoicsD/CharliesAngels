__author__ = 'Zoltan'
import csv

word = input("What do you want to delete?")

with open('proba.csv') as donor_file:
    with open('proba2.csv') as f:
        f = csv.writer(open("proba2.csv", "w" , newline=""))
        reader = csv.reader(donor_file)
        warning = "Sorry, we can't find what you want to delete"
        for row in reader:
            if word != row[5]:
                print(row)
                f.writerow(row)
            else:
                warning = "Your delete is successful"
        if warning != "":
            print(warning)

with open('proba2.csv') as donor_file:
    with open('proba.csv') as f:
        f = csv.writer(open("proba.csv", "w" , newline=""))
        reader = csv.reader(donor_file)

        for row in reader:
            for i in row[0]:
                f.writerow(row)
