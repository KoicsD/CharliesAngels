
import csv

def sorting(lista):
    lst=[]
    for i in lista:

        lst.append(str(i).lower())

    if len(lst)==1:
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
    with open('proba.csv', newline='') as donor_file:
        reader = csv.reader(donor_file)
        for row in reader:
            if row[index].lower()==good[good_index]:
                print (row)
        good_index += 1
        if good_index<len(good):
            sorting_row(index,good_index)
        print (good_index)


word = input("What do you search?")
index = input("What is the key?")
with open('proba.csv', newline='') as donor_file:
    reader = csv.reader(donor_file)
    lista = []
    good = []

    for row in reader:
        print(row[index])
        lista.append(row[index])
    sorting(lista)
    print(good)
    good_index=0
    sorting_row(index,good_index)
