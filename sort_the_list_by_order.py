from search_in_files import calculate_age_in_year
import csv

def sorting(lista):
    lst=[]
    for i in lista:

        lst.append(str(i).lower())

    if len(lst) == 1:
        good.append(min(lst))

        return
    alap = str(min(lst))

    lst.remove(alap)
    if len(good) == 0:
        good.append(alap)
    if alap > max(good):
        good.append(alap)
    sorting(lst)

def sorting_row(index,good_index):
    global donor_file, reader, row
    with open('DATA/donors.csv', newline='') as donor_file:
        reader = csv.reader(donor_file)
        for row in reader:
            if row[index].lower() == good[good_index]:
                if "name" in row:
                    continue
                print("-"*35)
                print(str(good_index) + ".")
                print("\t" + row[0])
                print("\t" + row[1] + " kg")
                print("\t" + row[3] + " - " + str(calculate_age_in_year(row[3])) + " years old")
                print("\t" + row[10])
                print("-" * 35)
        good_index += 1
        if good_index<len(good):
            sorting_row(index,good_index)




index = 0
with open('DATA/donors.csv', newline='') as donor_file:
    reader = csv.reader(donor_file)
    lista = []
    good = []

    for row in reader:

        lista.append(row[index])
    sorting(lista)

    good_index=0
    sorting_row(index,good_index)
