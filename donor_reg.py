from datetime import datetime, date
import random


# PROBLEM: What if the New Donor has never donated blood???!!!
# Another thought: Why do we let User give unsuitable data if we have asked the most problematic questions in advance?


# global dictionary for variables:
data = dict()


# check-/validating and other assistant functions:                                      # check- and assistants
def validate_name(name_string: str):                                        # name
    splitted_name = name_string.split(" ")
    return name_string.replace(" ", "").isalpha() and len(splitted_name) > 1


def calculate_age_in_year(birth_date: date):                                # calculate_age_in_year
    return (datetime.now().date() - birth_date).days // 365


def last_donation_time_is_valid(date_of_donation: date):                    # date of last donation
    return (datetime.now().date() - date_of_donation).days > 90


def check_identifier(identifier: str):                                           # identifier
    if len(identifier) != 8:
        print("It isn't an correct form for identifier, should be 8 character long.")
        return False
    elif identifier[0:6].isdigit():
        if identifier[6:].isalpha():
            return True
        else:
            print("An identity card's last two character should be letter!")
            return False
    elif identifier[0:6].isalpha():
        if identifier[6:].isdigit():
            return True
        else:
            print("A passport's last two character should be number!")
            return False
    else:
        print("Please write again your unique ID!")
        return False


def check_mobil_number(mobile_number: str):                                      # mobile
    if mobile_number[0:2] != '06' and mobile_number[0:3] != "+36":
        print("Please play attention the correct form. First charecters should be 06 or +36")
        return False
    if mobile_number[0:2] == '06' and len(mobile_number) != 11 or mobile_number[0:3] == '+36' and len(
            mobile_number) != 12:
        print("It is not a correct form, because number length should be 11 or 12")
        return False
    if not mobile_number[-11:].isdigit():
        print('Phone number should be just digit')
        return False
    if mobile_number[-9:-7] != '20' and mobile_number[-9:-7] != "30" and mobile_number[-9:-7] != "70":
        print("Your telephone partner's number is not correct(Choose:20/30/70")
        return False
    else:
        return True


def gender_is_valid(string: str):                                                # gender
    return string.lower() == "n" or string.lower() == "f"


def email_is_valid(email_string: str):                                           # email
    return "@" in email_string and \
           email_string.index("@") > 0 and \
           (email_string.endswith(".hu") or email_string.endswith(".com"))
# end of check-/validating and other assistant functions                                # \ check- and assistants


# warning user before filling the form (checking most neurargic questions):             # warn_user
def warn_user():
    inp = ""
    l_inp = ""

    while True:                                                     # is at least 18?
        inp = input("Is the new donor at least 18 years old? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'y':
            break
        elif l_inp == 'n':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True

    while True:                                                     # ID surely still valid?
        inp = input("Are you sure the New Donor's ID has not expired yet? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'y':
            break
        elif l_inp == 'n':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True

    while True:                                                     # weights at least 50?
        inp = input("Does the New Donor weight at least 50 kg? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'y':
            break
        elif l_inp == 'n':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True

    while True:                                                     # was sick in the last month?
        inp = input("Was the New Donor ill in the last 30 days? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'n':
            break
        elif l_inp == 'y':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True

    while True:                                                     # donated in the last 3 months?
        inp = input("Has the New Donor donated blood in the last 90 days? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'n':
            break
        elif l_inp == 'y':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True

    print("We can fill the form.")
    return False
# end of warning user                                                                   # \ warn_user


# form-filling input functions:                                                         # input functions
def input_name():                                                           # name
    valid_name = False
    data_name = ""
    while not valid_name:
        data_name = input("Kerem adja meg a teljes nevet szokozzel elvalasztva!(Keresztnev Vezeteknev): ")
        if validate_name(data_name):
            valid_name = True
        else:
            print("A megadott nev csak betuket es szokozt tartalmazhat!")

    data["name"] = data_name


def input_weight():                                                         # weight
    data_weight = ""
    while not data_weight:
        data_weight = input("Adja meg a testsulyat!(kg): ")
        if not (str(data_weight).isdigit() and int(data_weight) > 0):
            print("A testsulynak 0tol nagyobb pozitiv szamnak kell lennie!")
            data_weight = ""

    data["weight"] = int(data_weight)


def get_birth_date():                                                       # birth date
    birth_date = ""
    while not birth_date:

        birth_date = input("Kerem adja meg a szuletesi datumat (YYYY.MM.DD) formatumban!: ")
        try:
            bdate = datetime.strptime(birth_date, "%Y.%m.%d").date()
        except ValueError:
            print("Hibas datumformatum!")
            birth_date = ""

    data["birth_date"] = bdate


def get_last_donation_time():                                               # date of last donation
    last_time = ""
    while not last_time:

        last_time = input("Kerem adja meg a legutobbi veradas datumat (YYYY.MM.DD) formatumban!: ")
        try:
            ltime = datetime.strptime(last_time, "%Y.%m.%d").date()
        except ValueError:
            print("Hibas datumformatum!")
            last_time = ""

    data["last_donation"] = ltime


def input_id_expiration():                                                  # id expiration
    ID_expiration = ""
    while True:
        sdate = input("Please enter date of ID expiration (YYYY.MM.DD): ")
        try:
            pdate = datetime.strptime(sdate, "%Y.%m.%d").date()
            time_until_expiration = pdate - datetime.now().date()
            msg = "OK"
            if time_until_expiration.days < 1:
                msg = "ID expiration should be later than today!"

            if msg == "OK":
                break
            else:
                print(msg)
        except ValueError:
            print("Wrong date format!")

    data["exp_date"] = pdate


def validate_identifier():                                                  # identifier
    identifier = ""
    while identifier == '':
        identifier = input("Please write your unique ID(identity card/passport)!")

        if identifier == "":
            print("Unique identifier cannot be empty")
        elif not check_identifier(identifier):
            identifier = ""
    data["id"] = identifier


def input_blood_type():                                                     # blood type
    valid_blood_type = False
    data_blood_type = ""
    blood_types = ("A+", "0+", "B+", "AB+", "A-", "0-", "B-", "AB-")

    while not valid_blood_type:
        data_blood_type = input("Adja meg a vercsoportjat!: ")
        if str(data_blood_type).upper() not in blood_types:
            print("Kerem helyes vercsoportot adjon meg! (A+, 0+, B+, AB+, A-, 0-, B-, AB-)")
        else:
            valid_blood_type = True

    data["blood_type"] = data_blood_type


def get_mobile_number():                                                    # mobile
    mobile_number = ""
    while mobile_number == "":
        mobile_number = input("Please write your mobile number(like this:06201234567 or +36301234567):")

        if mobile_number == "":
            print("Phone number is empty:")

        elif not check_mobil_number(mobile_number):
            mobile_number = ""
    data["mobile"] = mobile_number


def get_gender():                                                           # gender
    data_gender = ""
    valid_gender = False
    while not valid_gender:
        data_gender = input("Adja meg a nemet!(N/F): ")
        valid_gender = gender_is_valid(data_gender)
    data["gender"] = data_gender


def get_email():                                                            # email
    data_email = False
    email_string = ""
    while not data_email:
        email_string = input("Kerem irja be az email cimet:  ")
        if email_is_valid(email_string):
            data_email = True
        else:
            print("Az email cimnek tartalmaznia kell  '@'-t  es .hu-ra vagy .com-ra kell vegzodnie")
    data["email"] = email_string
# end of input functions                                                                # \ input functions


# hemoglobin random-generated instead of input:                                         # hemoglobin random
def random_hemoglobin():
    data["hemoglobin"] = random.randint(80, 200)


# checking if donor is suitable                                                         # is donor suitable?
def donor_is_valid():   # age, weight, last_don, hemo, id_exp
    data["suitable"] = data["weight"] > 50 and \
           data["hemoglobin"] > 110 and \
           last_donation_time_is_valid(data["last_donation"]) and \
           data["age"] > 18 and \
           data["exp_date"] > datetime.now().date()


# main entry point below    # main entry point below    # main entry point below    # main entry point below
# requesting for all the data and filling the form from this function:                  # fill_donor
def fill_donor():
    # enough to do initialization here, locally:
    data["name"] = ""
    data["weight"] = 0
    data["gender"] = "n"
    data["birth_date"] = datetime(1, 1, 1).date()
    data["age"] = 0
    data["last_donation"] = datetime(1, 1, 1).date()
    data["blood_type"] = "00"
    data["id"] = "--------"
    data["exp_date"] = datetime(1, 1, 1).date()
    data["email"] = "@.com"
    data["mobile"] = "+3600000000"
    data["hemoglobin"] = 0
    data["suitable"] = False

    if warn_user():
        return
    input_name()
    input_weight()
    get_gender()
    get_birth_date()
    data["age"] = calculate_age_in_year(data["birth_date"])
    get_last_donation_time()
    input_blood_type()
    validate_identifier()
    input_id_expiration()
    get_email()
    get_mobile_number()
    random_hemoglobin()

    donor_is_valid()


# printing as table                                                                     # print_donor
def print_donor():
    print("Name: %s" % data["name"])
    print("Age: %d" % data["age"])
    if data["gender"].lower() == 'n':
        print("Gender: female")
    else:
        print("Gender: male")
    print("Date of Birth: %s" % data["birth_date"].strftime("%Y.%m.%d"))
    print("Identifier: %s" + data["id"])
    print("Expiration Date of ID: %s" % data["exp_date"].strftime("%Y.%m.%d"))
    print("Weight: %d kg" % data["weight"])
    print("Type of Blood: %s" % data["blood_type"])
    print("Date of Last Donation: %s" % data["last_donation"].strftime("%Y.%m.%d"))
    print("Mobile: %s" % data["mobile"])
    print("Email: %s" % data["email"])
    if data["suitable"]:
        print("The Donor is SUITABLE for donation.")
    else:
        print("The Donor is NOT SUITABLE for donation")


# main function and dundername invoking it:
def main():
    # demo consists of 2 steps:
    fill_donor()  # filling the form
    print('-' * 10)
    print_donor()  # and printing the data


if __name__ == "__main__":
    main()
