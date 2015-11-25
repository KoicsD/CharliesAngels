__author__ = 'Zoltan'
from search_in_files import calculate_age_in_year
import csv

index = int(input('What will it get ordered by?'))
row_index= 1
with open('DATA/donors.csv',newline='') as donor_file:
        reader = csv.reader(donor_file)
        next(reader)
        lst=[]
        if index == 1 or index == 9:
            lst = sorted(reader, key=lambda donor: int(donor[index]))
        else:
            lst = ( sorted(reader, key=lambda donor: donor[index]))

        for row in lst:

            print("-"*35)
            print(str(row_index) + ".")
            row_index += 1
            print("\t" + row[0])
            print("\t" + row[1] + " kg")
            print("\t" + row[3] + " - " + str(calculate_age_in_year(row[3])) + " years old")
            print("\t" + row[10])
            print("-" * 35)
