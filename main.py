import event_reg
import donor_reg


def print_separator_line():
    print("-"*32)


def greetings():
    print("Welcome in the blood donor register application!!")
    print_separator_line()


if __name__ == '__main__':
    greetings()
    choice = ""
    while True:
            choice = input("""
Please choose, you want to run Donor register or Location register?
Donor register press: 1
Location register press: 2
Press 3 to exit \n >>>""")
            if choice == "1":
                donor_reg.main()
                break
            elif choice == "2":
                my_object = event_reg.Donation()
                break
            elif choice == "3":
                break
