from datetime import datetime, time, timedelta
import random


# Task:
#     warn_user:# weight > 50
#                 Generate random number: Hemogblobin level between 80-200, write out is the donor suitable or not (value is greather than 110)?
#                 last donation was more than 3 months ago
#                 age > 18 years
#                 How old is the donor in years based on date of birth?
#                 ID is not expired.


def random_hemoglobin():
    return random.randint(80,200)


def donor_is_valid():
    return input_weight() > 50 and \
           random_hemoglobin() > 110 and \
           last_donation_time() == True and \
           age_is_valid() == True and \
           input_date() > datetime.now()


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
        data_name = input("Kerem adja meg a teljes nevet szokozzel elvalasztva!(Keresztnev Vezeteknev): ")
        if validate_name(data_name):
            valid_name = True
        else:
            print("A megadott nev csak betuket es szokozt tartalmazhat!")

    return data_name


# -------------------------------------------------------------------------------
#
#     Weight,
#                 weight > 50
#

def input_weight():
    data_weight = ""
    while not data_weight:
        data_weight = input("Adja meg a testsulyat!(kg): ")
        if not (str(data_weight).isdigit() and int(data_weight) > 0):
            print("A testsulynak 0tol nagyobb pozitiv szamnak kell lennie!")
            data_weight = ""

    return data_weight


# -------------------------------------------------------------------------------
#
#
#     Gender,
#
#     Date of Birth,
#                 age > 18 years
#                 How old is the donor in years based on date of birth?

def calculate_age_in_year(birth_date: datetime):
    return (datetime.now() - birth_date).days // 365


def age_is_valid():
    return calculate_age_in_year() > 18


#
#     Last donation date,
#                 last donation was more than 3 months ago
#                 never is also possible

def last_donation_time(date_of_donation: datetime):
    return (datetime.now() - date_of_donation).days > 90


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

ID_expiration = ""


def input_date(ID_expiration):
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

    return pdate


identifier = ""


def check_identifier(identifier):
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


def validate_identifier(identifier):
    identifier = ""
    while identifier == '':
        identifier = input("Please write your unique ID(identity card/passport)!")

        if identifier == "":
            print("Unique identifier cannot be empty")
        elif not check_identifier(identifier):
            identifier = ""


# Blood type
#

def input_blood_type():
    valid_blood_type = False
    data_blood_type = ""
    blood_types = ("A+", "0+", "B+", "AB+", "A-", "0-", "B-", "AB-")

    while not valid_blood_type:
        data_blood_type = input("Adja meg a vercsoportjat!: ")
        if str(data_blood_type).lower() not in str(blood_types).lower():
            print("Kerem helyes vercsoportot adjon meg! (A+, 0+, B+, AB+, A-, 0-, B-, AB-)")
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


mobile_number = "20"


def validate_mobile_number(mobile_number):
    mobile_number = ""
    while mobile_number == "":
        mobile_number = input("Please write your mobile number(like this:06201234567 or +36301234567):")

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
    if string.lower() == "n" or string.lower() == "f":
        print("OK!")
        return True
    else:
        print("Nem megfelelo!")
    return False


def get_gender():
    data_gender = ""
    valid_gender = False
    if not valid_gender:
        data_gender = input("Adja meg a nemet!(N/F): ")
        if gender_is_valid(data_gender):
            valid_gender = True
        else:
            print("Adja meg a nemet!(N/F): ")
            data_gender = ("")
    return data_gender


get_gender()


def email_is_valid(email_string):
    return "@" in email_string and \
           email_string.index("@") > 0 and \
           (email_string.endswith(".hu") or email_string.endswith(".com"))


def get_email():
    data_email = False
    email_string = " "
    while not data_email:
        email_string = input("Kerem irja be az email cimet:  ")
        if email_is_valid(email_string):
            data_email = True
        else:
            print("Az email cimnek tartalmaznia kell  '@'-t  es .hu-ra vagy .com-ra kell vegzodnie")
    return email_string



