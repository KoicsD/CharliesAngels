from datetime import datetime, date
import random


# Task:
#     warn_user:# weight > 50
#                 Generate random number: Hemogblobin level between 80-200, write out is the donor suitable or not (value is greather than 110)?
#                 last donation was more than 3 months ago
#                 age > 18 years
#                 How old is the donor in years based on date of birth?
#                 ID is not expired.
def warn_user():
    inp = ""
    l_inp = ""
    while True:
        inp = input("Is the New Donor at least 18 years old? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'y':
            break
        elif l_inp == 'n':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True
    while True:
        inp = input("Are you sure the New Donor's ID has not expired yet? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'y':
            break
        elif l_inp == 'n':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True
    while True:
        inp = input("Does the New Donor weight at least 50 kg? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'y':
            break
        elif l_inp == 'n':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True
    while True:
        inp = input("Was the New Donor ill in the last 30 days? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'n':
            break
        elif l_inp == 'y':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True
    while True:
        inp = input("Has the New Donor donated blood in the last 90 days? (y/n) ")
        l_inp = inp.lower()
        if l_inp == 'n':
            break
        elif l_inp == 'y':
            print("The New Donor is surely UNSUITABLE for donation.")
            return True
    print("We can fill the form.")
    return False


def random_hemoglobin():
    return random.randint(80,200)

# -------------------------------------------------------------------------------
#
#     Name,
#                 Parse name, store it in a separated object
#

def validate_name(name_string: str):
    splitted_name = name_string.split(" ")
    return name_string.replace(" ", "").isalpha() and len(splitted_name) > 1


def input_name():
    valid_name = False
    data_name = ""
    while not valid_name:
        data_name = input("Please enter the New Donor's full name separated with space!(Firstname Surname): ")
        if validate_name(data_name):
            valid_name = True
        else:
            print("Full name can only contain characters and space and can not be empty!")

    return data_name


# -------------------------------------------------------------------------------
#
#     Weight,
#                 weight > 50
#

def input_weight():
    data_weight = ""
    while not data_weight:
        data_weight = input("Please enter the New Donor's weight!(kg): ")
        if not (str(data_weight).isdigit() and int(data_weight) > 0):
            print("Weight must be integer!")
            data_weight = ""

    return int(data_weight)


# -------------------------------------------------------------------------------
#
#
#     Gender,
#
#     Date of Birth,
#                 age > 18 years
#                 How old is the donor in years based on date of birth?


def get_birth_date():
    birth_date = ""
    while not birth_date:

        birth_date = input("Please enter birth date (YYYY.MM.DD)!: ")
        try:
            bdate = datetime.strptime(birth_date, "%Y.%m.%d").date()
        except ValueError:
            print("Wrong date format!")
            birth_date = ""

    return  bdate


def calculate_age_in_year(birth_date: date):
    return (datetime.now().date() - birth_date).days // 365

#
#     Last donation date,
#                 last donation was more than 3 months ago
#                 never is also possible


def get_last_donation_time():
    last_time = ""
    while not last_time:

        last_time = input("Please enter last donation date (YYYY.MM.DD)!: ")
        try:
            ltime = datetime.strptime(last_time, "%Y.%m.%d").date()
        except ValueError:
            print("Wrong date format!")
            last_time = ""

    return  ltime

def last_donation_time_is_valid(date_of_donation: date):
    return (datetime.now().date() - date_of_donation).days > 90
#
#     Unique identifier  &     Expiration of ID
#                 6digit + 2letter (123456AB) is identity card
#                 6letter + 2digit (ASDFGH12) is passport
#                 ID is not expired.
# ID_expired=""
# def get_ID_expired():
#     ID_expired=input ("When will ID be expired?(YYYY/MM/DD")
#
# def check_ID_expiration(date):
#     return ID_expired > today


def input_id_expiration():
    ID_expiration = ""
    while True:
        sdate = input("Please enter the New Donor's date of ID expiration (YYYY.MM.DD): ")
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

    return pdate


def check_identifier(identifier):
    if len(identifier) != 8:
        print("It isn't a correct form for identifier, should be 8 character long.")
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
        print("Please write again the unique ID!")
        return False


def validate_identifier():
    identifier = ""
    while identifier == '':
        identifier = input("Please enter the New Donor's unique ID(identity card/passport)!")

        if identifier == "":
            print("Unique identifier cannot be empty")
        elif not check_identifier(identifier):
            identifier = ""
    return identifier


# Blood type
#

def input_blood_type():
    valid_blood_type = False
    data_blood_type = ""
    blood_types = ("A+", "0+", "B+", "AB+", "A-", "0-", "B-", "AB-")

    while not valid_blood_type:
        data_blood_type = input("Please enter the New Donor's blood type!: ")
        if str(data_blood_type).upper() not in blood_types:
            print("Blood type must be: A+, 0+, B+, AB+, A-, 0-, B- or AB-")
        else:
            valid_blood_type = True

    return data_blood_type


# -------------------------------------------------------------------------------
#     email address
#                 Email address validation (contains @-ot and ending with .hu/.com)
#     Mobil number
#                 Mobil number validation (starts with +36/06 + 2 digit(provider identifier - 20/30/70) ending with 7 digits)

def check_mobil_number(mobile_number):
    if mobile_number[0:2] != '06' and mobile_number[0:3] != "+36":
        print("Please pay attention the correct form. First characters should be 06 or +36")
        return False
    if mobile_number[0:2] == '06' and len(mobile_number) != 11 or mobile_number[0:3] == '+36' and len(
            mobile_number) != 12:
        print("It is not a correct form, because number length should be 11 or 12")
        return False
    if not mobile_number[-11:].isdigit():
        print('Phone number should be just digit')
        return False
    if mobile_number[-9:-7] != '20' and mobile_number[-9:-7] != "30" and mobile_number[-9:-7] != "70":
        print("Telephone number is not correct(Choose:20/30/70")
        return False
    else:
        return True


def get_mobile_number():
    mobile_number = ""
    while mobile_number == "":
        mobile_number = input("Please enter the New Donor's mobile number(like this:06201234567 or +36301234567):")

        if mobile_number == "":
            print("Phone number is empty:")

        elif not check_mobil_number(mobile_number):
            mobile_number = ""
    return mobile_number


#     __repr__
#                 Write out data in a table form pl.:
#                 Attila, Molnar
#                 90kg [using of str function]
#                 1989.05.06 - 26 years old
#                 asd@test.hu,
#                 Generate random number: Hemogblobin level between 80-200, write out is the donor suitable or not (value is greather than 110)?
#
# Functions:
# Parse name, store it in a separated object                    used
# Suitable for donation:                                        used
# weight > 50
# last donation was more than 3 months ago
# age > 18 years
# How old is the donor in years based on date of birth?
# ID is not expired.                                            used
# Define type of personal document based on its identifier:
# 6digit + 2letter (123456AB) is identity card                  used
# 6letter + 2digit (ASDFGH12) is passport                       used
# Email address validation (contains @-ot and ending with .hu/.com)         used
# Mobil number validation (starts with +36/06 + 2 digit(provider identifier - 20/30/70) ending with 7 digits)   used
# Write out data in a table form pl.:
# Attila, Molnar
# 90kg [using of str function]
# 1989.05.06 - 26 years old
# asd@test.hu,
# Generate random number: Hemogblobin level between 80-200, write out is the donor suitable or not (value is greather than 110)?


def gender_is_valid(string):
    return string.lower() == "m" or string.lower() == "f"


def get_gender():
    data_gender = ""
    valid_gender = False
    while not valid_gender:
        data_gender = input("Please enter the New Donor's gender!(F/M): ")
        valid_gender = gender_is_valid(data_gender)
    return data_gender


def email_is_valid(email_string):
    return "@" in email_string and \
           email_string.index("@") > 0 and \
           (email_string.endswith(".hu") or email_string.endswith(".com"))


def get_email():
    data_email = False
    email_string = " "
    while not data_email:
        email_string = input("Please enter the New Donor's email address:  ")
        if email_is_valid(email_string):
            data_email = True
        else:
            print("The email address should contain '@'-t and should end with '.hu' or '.com'")
    return email_string


def donor_is_valid(age, weight, last_don, hemo, id_exp):
    return weight > 50 and \
           hemo > 110 and \
           last_donation_time_is_valid(last_don) and \
           age > 18 and \
           id_exp > datetime.now().date()


def print_donor(name, age, gender, birth_date, id, id_expiration,
                weight, blood_type, last_donation,
                mobile, email, suitable):
    print("Name: %s" % name)
    print("Age: %d" % age)
    if gender.lower() == 'n':
        print("Gender: female")
    else:
        print("Gender: male")
    print("Date of Birth: %s" % birth_date.strftime("%Y.%m.%d"))
    print("Identifier: %s" + id)
    print("Expiration Date of ID: %s" % id_expiration.strftime("%Y.%m.%d"))
    print("Weight: %d kg" % weight)
    print("Type of Blood: %s" % blood_type)
    print("Date of Last Donation: %s" % last_donation.strftime("%Y.%m.%d"))
    print("Mobile: %s" % mobile)
    print("Email: %s" % email)
    if suitable:
        print("The New Donor is SUITABLE for donation.")
    else:
        print("The New Donor is NOT SUITABLE for donation")


def main():
    if warn_user():
        return
    name = input_name()
    weight = input_weight()
    gender = get_gender()
    birth_date = get_birth_date()
    age = calculate_age_in_year(birth_date)
    last_donation = get_last_donation_time()
    blood_type = input_blood_type()
    id = validate_identifier()
    exp_date = input_id_expiration()
    email = get_email()
    mobile = get_mobile_number()
    hemoglobin = random_hemoglobin()

    suitable = donor_is_valid(age, weight, last_donation, hemoglobin, exp_date)
    print('-' * 10)
    print_donor(name, age, gender, birth_date, id, exp_date,
                weight, blood_type, last_donation,
                mobile, email, suitable)


if __name__ == "__main__":
    main()
