


# Task:
#     warn_user:# weight > 50
#                 Generate random number: Hemogblobin level between 80-200, write out is the donor suitable or not (value is greather than 110)?
#                 last donation was more than 3 months ago
#                 age > 18 years
#                 How old is the donor in years based on date of birth?
#                 ID is not expired.
#
#     Name,
#                 Parse name, store it in a separated object

def validate_name(name_string: str):
    splitted_name = name_string.split(" ")
    return name_string.replace(" ", "").isalpha() and len(splitted_name) > 1

def input_name():
    valid_name = False
    fullname = ""
    while not valid_name:
        fullname = input("Kerem adja meg a teljes nevet szokozzel elvalasztva!: ")
        if validate_name(fullname):
            valid_name = True
        else:
            print("A megadott nev csak betuket es szokozt tartalmazhat!")

    return fullname


#
#     Weight,
#                 weight > 50
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
    while not valid_gender:
        data_gender = input("Kerem adja meg a nemet: ")

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
    data_email= False
    email_string = " "
    while not data_email:
        email_string = input("Kerem irja be az email cimet:  ")
        if email_is_valid(email_string):
            data_email = True
        else:
            print("Az email cimnek tartalmaznia kell  '@'-t  es .hu-ra vagy .com-ra kell vegzodnie")
    return email_string

get_email()