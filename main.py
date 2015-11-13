import event_reg
import donor_reg
import List_donors
import search_in_files


def greetings():
    print("""
-----------------------------------------------------------------------
--- Welcome to the coolest donor and donation event managing system ---
-----------------------------------------------------------------------""")


if __name__ == '__main__':
    greetings()
    choice = ""
    while True:
            choice = input("""
Main menu
    1. Add new donor
    2. Add new donation event
    3. Delete a donor
    4. Delete a donation event
    5. List donors or donation events
    6. Search
    7. Exit

Please choose your action: """)
            if choice == "1":
                donor_reg.main()
            elif choice == "2":
                event_reg.main()
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                choice_list = input("""
Please choose if you want to list Donors or Donations:
    1. Donors
    2. Donations
    0. Return

Please choose your action: """)
                if choice_list == "1":
                    print("-" * 22)
                    print("----Listing Donors----")
                    List_donors.main()
                elif choice_list == "2":
                    pass
                elif choice_list == "0":
                    pass
            elif choice == "6":
                choice = input("""
Please choose if you want to search in Donors or Donations:
    1. Donors
    2. Donations
    0. Return

Please choose your action: """)
                if choice == "1":
                    search_in_files.search_in_donors()
                elif choice == "2":
                    pass
                elif choice == "0":
                    pass
            elif choice == "7":
                break
