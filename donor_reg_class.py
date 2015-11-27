from datetime import datetime, date
import random


# PROBLEM: What if the New Donor has never donated blood???!!!
# Another thought: Why do we let User give unsuitable data if we have asked the most problematic questions in advance?


class Donor:
    # check-/validating and other assistant functions:                                      # check- and assistants
    @staticmethod
    def validate_name(name_string: str):                                        # name
        splitted_name = name_string.split(" ")
        return name_string.replace(" ", "").isalpha() and len(splitted_name) > 1

    @staticmethod
    def calculate_age_in_year(birth_date: date):                                # calculate_age_in_year
        return (datetime.now().date() - birth_date).days // 365

    @staticmethod
    def last_donation_time_is_valid(date_of_donation: date):                    # date of last donation
        return (datetime.now().date() - date_of_donation).days > 90

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def gender_is_valid(string: str):                                                # gender
        return string.lower() == "n" or string.lower() == "f"

    @staticmethod
    def email_is_valid(email_string: str):                                           # email
        return "@" in email_string and \
               email_string.index("@") > 0 and \
               (email_string.endswith(".hu") or email_string.endswith(".com"))
    # end of check-/validating and other assistant functions                                # \ check- and assistants

    # warning user before filling the form (checking most neurargic questions):             # warn_user
    @staticmethod
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
    def input_name(self):                                                           # name
        valid_name = False
        data_name = ""
        while not valid_name:
            data_name = input("Kerem adja meg a teljes nevet szokozzel elvalasztva!(Keresztnev Vezeteknev): ")
            if Donor.validate_name(data_name):
                valid_name = True
            else:
                print("A megadott nev csak betuket es szokozt tartalmazhat!")

        self.name = data_name

    def input_weight(self):                                                         # weight
        data_weight = ""
        while not data_weight:
            data_weight = input("Adja meg a testsulyat!(kg): ")
            if not (str(data_weight).isdigit() and int(data_weight) > 0):
                print("A testsulynak 0tol nagyobb pozitiv szamnak kell lennie!")
                data_weight = ""

        self.weight = int(data_weight)

    def get_birth_date(self):                                                       # birth date
        birth_date = ""
        while not birth_date:

            birth_date = input("Kerem adja meg a szuletesi datumat (YYYY.MM.DD) formatumban!: ")
            try:
                bdate = datetime.strptime(birth_date, "%Y.%m.%d").date()
            except ValueError:
                print("Hibas datumformatum!")
                birth_date = ""

        self.birth_date = bdate

    def get_last_donation_time(self):                                               # date of last donation
        last_time = ""
        while not last_time:

            last_time = input("Kerem adja meg a legutobbi veradas datumat (YYYY.MM.DD) formatumban!: ")
            try:
                ltime = datetime.strptime(last_time, "%Y.%m.%d").date()
            except ValueError:
                print("Hibas datumformatum!")
                last_time = ""

        self.last_donation = ltime

    def input_id_expiration(self):                                                  # id expiration
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

        self.exp_date = pdate

    def validate_identifier(self):                                                  # identifier
        identifier = ""
        while identifier == '':
            identifier = input("Please write your unique ID(identity card/passport)!")

            if identifier == "":
                print("Unique identifier cannot be empty")
            elif not Donor.check_identifier(identifier):
                identifier = ""
        self.id = identifier

    def input_blood_type(self):                                                     # blood type
        valid_blood_type = False
        data_blood_type = ""
        blood_types = ("A+", "0+", "B+", "AB+", "A-", "0-", "B-", "AB-")

        while not valid_blood_type:
            data_blood_type = input("Adja meg a vercsoportjat!: ")
            if str(data_blood_type).upper() not in blood_types:
                print("Kerem helyes vercsoportot adjon meg! (A+, 0+, B+, AB+, A-, 0-, B-, AB-)")
            else:
                valid_blood_type = True

        self.blood_type = data_blood_type

    def get_mobile_number(self):                                                    # mobile
        mobile_number = ""
        while mobile_number == "":
            mobile_number = input("Please write your mobile number(like this:06201234567 or +36301234567):")

            if mobile_number == "":
                print("Phone number is empty:")

            elif not Donor.check_mobil_number(mobile_number):
                mobile_number = ""
        self.mobile = mobile_number

    def get_gender(self):                                                           # gender
        data_gender = ""
        valid_gender = False
        while not valid_gender:
            data_gender = input("Adja meg a nemet!(N/F): ")
            valid_gender = Donor.gender_is_valid(data_gender)
        self.gender = data_gender

    def get_email(self):                                                            # email
        data_email = False
        email_string = ""
        while not data_email:
            email_string = input("Kerem irja be az email cimet:  ")
            if Donor.email_is_valid(email_string):
                data_email = True
            else:
                print("Az email cimnek tartalmaznia kell  '@'-t  es .hu-ra vagy .com-ra kell vegzodnie")
        self.email = email_string
    # end of input functions                                                                # \ input functions

    # hemoglobin random-generated instead of input:                                         # hemoglobin random
    def random_hemoglobin(self):
        self.hemoglobin = random.randint(80, 200)

    # checking if donor is suitable                                                         # is donor suitable?
    def donor_is_valid(self):
        self.suitable = self.weight > 50 and \
               self.hemoglobin > 110 and \
               Donor.last_donation_time_is_valid(self.last_donation) and \
               self.age > 18 and \
               self.exp_date > datetime.now().date()


    # main entry point below    # main entry point below    # main entry point below    # main entry point below
    # requesting for all the data and filling the form from this function:                  # __init__
    def __init__(self):
        # enough to do initialization here, locally:
        self.name = ""
        self.weight = 0
        self.gender = "n"
        self.birth_date = datetime(1, 1, 1).date()
        self.age = 0
        self.last_donation = datetime(1, 1, 1).date()
        self.blood_type = "00"
        self.id = "--------"
        self.exp_date = datetime(1, 1, 1).date()
        self.email = "@.com"
        self.mobile = "+3600000000"
        self.hemoglobin = 0
        self.suitable = False

        if Donor.warn_user():
            return
        self.input_name()
        self.input_weight()
        self.get_gender()
        self.get_birth_date()
        self.age = Donor.calculate_age_in_year(self.birth_date)
        self.get_last_donation_time()
        self.input_blood_type()
        self.validate_identifier()
        self.input_id_expiration()
        self.get_email()
        self.get_mobile_number()
        self.random_hemoglobin()

        self.donor_is_valid()

    # stringizing to print as table                                                         # __repr__
    def __repr__(self):
        text = ""
        text += "Name: %s" % self.name + "\n"
        text += "Age: %d" % self.age + "\n"
        if self.gender.lower() == 'n':
            text += "Gender: female\n"
        else:
            text += "Gender: male\n"
        text += "Date of Birth: %s" % self.birth_date.strftime("%Y.%m.%d") + "\n"
        text += "Identifier: %s" % self.id + "\n"
        text += "Expiration Date of ID: %s" % self.exp_date.strftime("%Y.%m.%d") + "\n"
        text += "Weight: %d kg" % self.weight + "\n"
        text += "Type of Blood: %s" % self.blood_type + "\n"
        text += "Date of Last Donation: %s" % self.last_donation.strftime("%Y.%m.%d") + "\n"
        text += "Mobile: %s" % self.mobile + "\n"
        text += "Email: %s" % self.email + "\n"
        if self.suitable:
            text += "The Donor is SUITABLE for donation.\n"
        else:
            text += "The Donor is NOT SUITABLE for donation\n"
        return text


# main function and dundername invoking it:
def main():
    # demo consists of 2 steps:
    my_donor = Donor()  # filling the form
    print('-' * 10)
    print(my_donor)  # and printing the data


if __name__ == "__main__":
    main()
