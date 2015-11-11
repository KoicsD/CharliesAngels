import csv


def listing():
    with open('DATA\donors.csv', newline='') as file:
        reader = csv.reader(file)
        reader = sorted(reader)
        index = 1
        for rows in reader:
            print("-" * 22)
            next_page = input("Press enter to next page or enter 'exit' to return to the main menu.")
            print("-" * 22)
            print(str(index) + ".")
            index += 1
            result = []
            if next_page.lower() == "exit":
                return
            for row in rows:
                for item in row:
                    result.append(row)
                    break
            print(result[0])
            print(result[6] + "kg")
            print(result[3] + " - " + result[1] + " years old")
            print(result[10])

def main():
    listing()

if __name__ == "__main__":
    main()