import csv
from datetime import datetime, date


def listing():
    with open('DATA\donors.csv', newline='') as file:
        reader = csv.reader(file)
        list = reader
        index = 0
        next_page = ""
        for rows in list:
            if index > 0:
                print("-" * 68)
                next_page = input("Press enter to next page or enter 'exit' to return to the main menu.")
                print("-" * 68)
                print(str(index) + ". page")
            index += 1
            result = []
            if next_page.lower() == "exit":
                return
            for row in rows:
                if row not in exceptions:
                    for item in row:
                        result.append(row)
                        break
            try:
                print_donors_data(index, result)
            except IndexError:
                continue
        print("-" * 39)
        exit = input("Press enter to return to the main menu.")
        print("-" * 39)


def print_donors_data(index, result):
        print(result[0])
        print(result[1] + "kg")
        print(result[3] + " - " + str((datetime.now().date() - datetime.strptime(result[3], "%Y-%m-%d").date()).days // 365) + " years old")
        print(result[10])

exceptions = ["name","weight","gender","date_of_birth","last_donation","last_month_sickness","unique_identifier","expiration_of_id","blood_type","hemoglobin","email","mobil"]


def main():
    listing()

if __name__ == "__main__":
    main()