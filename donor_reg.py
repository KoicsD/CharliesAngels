__author__ = 'KoicsD'
from datetime import datetime



# Task:
#     warn_user:# weight > 50
#                 Generate random number: Hemogblobin level between 80-200, write out is the donor suitable or not (value is greather than 110)?
#                 last donation was more than 3 months ago
#                 age > 18 years
#                 How old is the donor in years based on date of birth?
#                 ID is not expired.

#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
#
#
#     Gender,
#
#     Date of Birth,
#                 age > 18 years
#                 How old is the donor in years based on date of birth?
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
ID_expired=""
def get_ID_expired():
    ID_expired=input ("When will ID be expired?(YYYY/MM/DD")

def check_ID_expiration(date):
    return ID_expired > today



identifier = ""

def check_identifier(identifier):
    if len(identifier) != 8:
        print ("It isn't an correct form for identifier, should be 8 character long.")
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
        print ("Please write again your unique ID!")
        return False


def validate_identifier(identifier):

    while identifier == '':
        identifier = input("Please write your unique ID(identity card/passport)!")

        if identifier == "":
            print("Unique identifier cannot be empty")
        elif not check_identifier(identifier):
            identifier = ""


#     Blood type
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


#-------------------------------------------------------------------------------
#     email address
#                 Email address validation (contains @-ot and ending with .hu/.com)
#     Mobil number
#                 Mobil number validation (starts with +36/06 + 2 digit(provider identifier - 20/30/70) ending with 7 digits)
#
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
