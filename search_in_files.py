__author__ = 'Zoltan'
import csv



word = input("What do you search?")

with open('DATA\donors.csv', newline='') as file:
    reader = csv.reader(file)
    warning = "Sorry, we can't find what you search"
    for row in reader:
        for i in row:
            if word in i:
                print(row)
                warning = ""
                break
    if warning != "":
        print(warning)

