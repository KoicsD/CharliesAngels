from datetime import datetime, date
import random
import donor_csv_writer
date_format = "%Y.%m.%d."


class UserInterrupt(Exception):
    pass


def input_name():
    valid_name = False
    data_name = ""
    while not valid_name:
        data_name = input("Please enter the New Donor's full name separated with space!(Firstname Surname): ")
        if data_name.lower() == "\\quit":
            raise UserInterrupt("Inputting name interrupted by User.")
        if validate_name(data_name):
            valid_name = True
        else:
            print("Full name can only contain characters and space and can not be empty!")

    return data_name


def input_weight():
    data_weight = ""
    while not data_weight:
        data_weight = input("Please enter the Donor's weight!(kg): ")
        if data_weight.lower() == "\\quit":
            raise UserInterrupt("Inputting weight interrupted by User.")
        if not (str(data_weight).isdigit() and int(data_weight) > 0):
            print("Weight must be integer!")
            data_weight = ""

    return int(data_weight)


def input_gender():
    data_gender = ""
    valid_gender = False
    while not valid_gender:
        data_gender = input("Please enter the Donor's gender!(M/F): ")
        if data_gender.lower() == "\\quit":
            raise UserInterrupt("Inputting gender interrupted by User.")
        if data_gender.lower() == "m" or data_gender.lower() == "f":
            valid_gender = validate_gender(data_gender)
            return valid_gender
        print("Must type 'M' or 'F'!")


def input_birth_date():
    birth_date = ""
    while not birth_date:
        birth_date = input("Please enter the Donor's birth date (YYYY.MM.DD.)!: ")
        if birth_date.lower() == "\\quit":
            raise UserInterrupt("Inputting birth date interrupted by User.")
        try:
            bdate = datetime.strptime(birth_date, date_format).date()
        except ValueError:
            print("Wrong date format!")
            birth_date = ""

    return bdate


def input_last_donation_time():
    last_time = ""
    while not last_time:
        last_time = input("Please enter the Donor's last donation date (YYYY.MM.DD.) or leave empty!: ")
        if last_time.lower() == "\\quit":
            raise UserInterrupt("Inputting date of last donation interrupted by User.")
        if last_time == "":
            return datetime.now().date()
        try:
            ltime = datetime.strptime(last_time, date_format).date()
        except ValueError:
            print("Wrong date format!")
            last_time = ""

    return ltime


def input_sickness():
    sick = ""
    while True:
        sick = input("Was the Donor ill in the last 30 days? (y/n) ")
        l_sick = sick.lower()
        if l_sick == "\\quit":
            raise UserInterrupt("Inputting last month sickness interrupted by User.")
        if sick == "":
            print("You must enter 'y' or 'n'")
        elif l_sick == 'n':
            break
        elif l_sick == 'y':
            break
        else:
            print("You must enter 'y' or 'n'")
    return l_sick


def input_identifier():
    identifier = ""
    while identifier == '':
        identifier = input("Please enter the Donor's unique ID(identity card/passport)!")
        if identifier.lower() == "\\quit":
            raise UserInterrupt("Inputting identifier interrupted by User.")
        if identifier == "":
            print("Unique identifier cannot be empty")
        elif not validate_identifier(identifier):
            identifier = ""
    return identifier


def input_id_expiration():
    ID_expiration = ""
    while True:
        sdate = input("Please enter the Donor's date of ID expiration (YYYY.MM.DD.): ")
        if sdate.lower() == "\\quit":
            raise UserInterrupt("Inputting expiration time of ID interrupted by User.")
        try:
            pdate = datetime.strptime(sdate, date_format).date()
            msg = "OK"
            if msg == "OK":
                break
            else:
                print(msg)
        except ValueError:
            print("Wrong date format!")

    return pdate


def input_blood_type():
    valid_blood_type = False
    data_blood_type = ""
    blood_types = ("A+", "0+", "B+", "AB+", "A-", "0-", "B-", "AB-")

    while not valid_blood_type:
        data_blood_type = input("Please enter the Donor's blood type!: ")
        if data_blood_type.lower() == "\\quit":
            raise UserInterrupt("Inputting blood type interrupted by User.")
        if str(data_blood_type).upper() not in blood_types:
            print("Blood type must be: A+, 0+, B+, AB+, A-, 0-, B- or AB-")
        else:
            valid_blood_type = True

    return data_blood_type


def input_email():
    data_email = False
    email_string = " "
    while not data_email:
        email_string = input("Please enter the Donor's email address:  ")
        if email_string.lower() == "\\quit":
            raise UserInterrupt("Inputting email address interrupted by User.")
        if validate_email(email_string):
            data_email = True
        else:
            print("The email address should contain '@'-t and should end with '.hu' or '.com'")
    return email_string


def input_mobile_number():
    mobile_number = ""
    while mobile_number == "":
        mobile_number = input("Please enter the Donor's mobile number(like this:06201234567 or +36301234567):")
        if mobile_number.lower() == "\\quit":
            raise UserInterrupt("Inputting mobile number interrupted by User.")
        if mobile_number == "":
            print("Phone number is empty:")

        elif not validate_mobil_number(mobile_number):
            mobile_number = ""
    return mobile_number


def validate_name(name_string: str):
    splitted_name = name_string.split(" ")
    return name_string.replace(" ", "").isalpha() and len(splitted_name) > 1


def validate_weight(weight):
    return weight > 50


def validate_gender(string):
    if string.lower() == "m":
        string = "Male"
        return string
    elif string.lower() == "f":
        string = "Female"
        return string


def validate_age(age):
    return age >= 18


def validate_last_donation_time(date_of_donation):
    if date_of_donation == datetime.now().date():
        return date_of_donation
    else:
        return (datetime.now().date() - date_of_donation).days > 90


def validate_sickness(sick):
    return sick == "y"


def is_id_unique(identifier):
    with open("DATA/donors.csv", newline="") as donor_file:
        for row in donor_file:
            if identifier.lower() in row.lower():
                print("The given identifier already exists in database!")
                return False
    return True


def validate_identifier(identifier):
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


def validate_id_expiration(id_exp):
    return id_exp > datetime.now().date()


def validate_hemoglobin(hemo):
    return hemo > 110


def validate_email(email_string):
    return "@" in email_string and \
           email_string.index("@") > 0 and \
           (email_string.endswith(".hu") or email_string.endswith(".com"))


def validate_mobil_number(mobile_number):
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


def random_hemoglobin():
    return random.randint(80, 200)


def calculate_age_in_year(birth_date: date):
    return (datetime.now().date() - birth_date).days // 365


def print_donor(name, age, gender, birth_date, id, id_expiration,
                weight, blood_type, last_donation,
                mobile, email, hemoglobin, was_sick_in_last_month):
    print("Name: %s" % name)
    print("Date of Birth: %s - %d years old." % (birth_date.strftime(date_format), age))
    print("Gender: %s" % gender)
    print("Weight: %d kg" % weight)
    print("Identifier: %s" % id)
    print("Expiration Date of ID: %s" % id_expiration.strftime(date_format))
    print("Date of Last Donation: %s" % last_donation.strftime(date_format))
    print("Type of Blood: %s" % blood_type)
    print("Hemoglobin: %s" % hemoglobin)
    print("Email: %s" % email)
    print("Mobile: %s" % mobile)
    print("Was sick in last month: %s" % was_sick_in_last_month)

def main():
    try:
        name = input_name()
        weight = input_weight()
        if not validate_weight(weight):
            print("Sorry the New Donor is not suitable for donation! Too low weight!")
            return
        gender = input_gender()
        birth_date = input_birth_date()
        age = calculate_age_in_year(birth_date)
        if not validate_age(age):
            print("Sorry the New Donor is not suitable for donation! Too young!")
            return
        last_donation = input_last_donation_time()
        if not validate_last_donation_time(last_donation):
            print("Sorry the New Donor is not suitable for donation! Already donated blood in the past 90 days!")
            return
        was_sick_in_last_month = input_sickness()
        if validate_sickness(was_sick_in_last_month):
            print("Sorry the New Donor is not suitable for donation! \
            You can not donate blood if you were sick in the past 30 days!")
            return
        id = input_identifier()
        if not is_id_unique(id):
            return
        id_exp_date = input_id_expiration()
        if not validate_id_expiration(id_exp_date):
            print("Sorry the New Donor is not suitable for donation! ID expired or expiring today!!")
            return
        blood_type = input_blood_type()
        hemoglobin = random_hemoglobin()
        if not validate_hemoglobin(hemoglobin):
            print("Sorry the New Donor not suitable for donation! Too low hemoglobin count!")
            return
        email = input_email()
        mobile = input_mobile_number()
        print('-' * 10)
        print_donor(name, age, gender, birth_date, id, id_exp_date,
                weight, blood_type, last_donation,
                mobile, email, hemoglobin,was_sick_in_last_month)

        print("The New Donor is SUITABLE for donation.")
        donor_csv_writer.store_donor(name,weight,gender,birth_date.strftime(date_format),
                                     last_donation.strftime(date_format),was_sick_in_last_month,
                                     id,id.strftime(date_format),
                                     blood_type,hemoglobin,email,mobile)
    except UserInterrupt as interruption:
        print(str(interruption))
    print('-' * 10)


def input_and_store_data():
    name = input_name()
    weight = input_weight()
    if not validate_weight(weight):
        print("Sorry the New Donor is not suitable for donation! Too low weight!")
        return
    gender = input_gender()
    birth_date = input_birth_date()
    age = calculate_age_in_year(birth_date)
    if not validate_age(age):
        print("Sorry the New Donor is not suitable for donation! Too young!")
        return
    last_donation = input_last_donation_time()
    if not validate_last_donation_time(last_donation):
        print("Sorry the New Donor is not suitable for donation! Already donated blood in the past 90 days!")
        return
    was_sick_in_last_month = input_sickness()
    if validate_sickness(was_sick_in_last_month):
        print("Sorry the New Donor is not suitable for donation! \
        You can not donate blood if you were sick in the past 30 days!")
        return
    id = input_identifier()
    id_exp_date = input_id_expiration()
    if not validate_id_expiration(id_exp_date):
        print("Sorry the New Donor is not suitable for donation! ID expired or expiring today!!")
        return
    blood_type = input_blood_type()
    hemoglobin = random_hemoglobin()
    if not validate_hemoglobin(hemoglobin):
        print("Sorry the New Donor not suitable for donation! Too low hemoglobin count!")
        return
    email = input_email()
    mobile = input_mobile_number()
    print('-' * 10)
    list = [name,weight,gender,birth_date.strftime(date_format),
                                 last_donation.strftime(date_format),was_sick_in_last_month,
                                 id,id_exp_date.strftime(date_format),
                                 blood_type,hemoglobin,email,mobile]
    print_donor(name, age, gender, birth_date, id, id_exp_date,
            weight, blood_type, last_donation,
            mobile, email, hemoglobin, was_sick_in_last_month)
    print('-' * 10)
    return list


if __name__ == "__main__":
    main()
