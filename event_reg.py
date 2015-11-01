__author__ = ['KoicsD', 'BodiZs']
from datetime import datetime, date, time, timedelta


class UserInterrupt(Exception):
    pass


class Donation:
    preparation_time = 30
    donation_time = 30
    citylist = ["Miskolc", "Kazincbarcika", "Szerencs", "Sarospatak"]

    @staticmethod
    def calc_max_n_donors(duration, n_beds):
        return ((duration - Donation.preparation_time) / Donation.donation_time) * n_beds

    def __init__(self, test_mode=False):
        self.valid = False
        self.test_mode = test_mode

        print("You can escape any time by typing '\quit'.")
        self.date = date(1, 1, 1)
        self.start_time = time()
        self.end_time = time()
        self.duration = 0
        self.zipcode = ""
        self.address = ""
        self.city = ""
        self.n_beds = 0
        self.max_n_donors = 0
        self.planned_n_donors = 0
        self.successful_donation = 0

        self.input_date()
        self.input_start_time()
        self.input_end_time()
        self.input_zipcode()
        self.input_city()
        self.input_address()
        self.input_n_beds()
        self.input_planned_n_donors()
        self.input_successful_donation()
        self.calc_succession_of_event()

        self.valid = True

    def __repr__(self):
        text = ""
        if self.test_mode:
            text += "valid: " + str(self.valid) + "\n"
        elif not self.valid:
            return "<Invalid Donation Object.>"
        text += "Date of Donation: " + self.date.strftime("%Y.%m.%d") + "\n"
        text += "Start-Time: " + self.start_time.strftime("%H:%M") + "\n"
        text += "End-Time: " + self.end_time.strftime("%H:%M") + "\n"
        if self.test_mode:
            text += "Duration: " + str(self.duration) + "\n"
        text += "Zip-code: " + self.zipcode + "\n"
        text += "City: " + self.city + "\n"
        text += "Address: " + self.address + "\n"
        text += "Number of Beds Available: " + str(self.n_beds) + "\n"
        if self.test_mode:
            text += "Maximum Number of Donors: " + str(self.max_n_donors) + "\n"
        text += "Planned Number of Donors: " + str(self.planned_n_donors) + "\n"
        text += "Number of Successful Donation: " + str(self.successful_donation) + "\n"
        return text

    def input_date(self):
        sdate = ""
        pdate = date(1, 1, 1)
        while True:
            sdate = input("Please enter date of event (YYYY.MM.DD): ")
            if sdate == "\\quit":
                raise UserInterrupt("input_date")
            try:
                pdate = datetime.strptime(sdate, "%Y.%m.%d").date()
                time_until_event = pdate - datetime.now().date()
                msg = "OK"
                if time_until_event.days < 10:
                    msg = "Date must be at least 10 days before the event!"
                elif not 1 <= pdate.isoweekday() <= 5:
                    msg = "Date must be on weekday!"
                if msg == "OK":
                    break
                else:
                    print(msg)
            except ValueError:
                print("Wrong date format!")
        self.date = pdate

    def input_start_time(self):
        starttime = ""
        pstarttime = time()
        while True:
            starttime = input("Please enter the start time of event (HH:MM): ")
            if starttime == "\\quit":
                raise UserInterrupt("input_start_time")
            try:
                pstarttime = datetime.strptime(starttime, "%H:%M").time()
                break
            except ValueError:
                print("Wrong format for time!")
        self.start_time = pstarttime

    def input_end_time(self):
        endtime = ""
        pendtime = 0
        duration = 0
        while True:
            endtime = input("Please enter the end time of event (HH:MM): ")
            if endtime == "\\quit":
                raise UserInterrupt("input_end_time")
            try:
                pendtime = datetime.combine(self.date, datetime.strptime(endtime, "%H:%M").time())
                pstarttime = datetime.combine(self.date, self.start_time)
                duration = (pendtime - pstarttime).total_seconds() // 60
                msg = "OK"
                if duration < Donation.preparation_time:
                    msg = "Preparation Time exceeds Duration or Negative Duration!"
                if msg == "OK":
                    break
                else:
                    print(msg)
            except ValueError:
                print("Wrong format for time!")
        self.end_time = pendtime.time()
        self.duration = duration

    def input_zipcode(self):
        zipcode = ""
        while True:
            zipcode = input("Please enter the zipcode (ex:1234): ")
            if zipcode == "\\quit":
                raise UserInterrupt("input_zipcode")
            try:
                msg = "OK"
                zero = "0"
                if not zipcode.isdigit():
                    msg = "Your zipcode must be numbers!"
                elif not len(zipcode) == 4:
                    msg = "Your zipcode too long!"
                elif zipcode.startswith(zero):
                    msg = "Your zipcode can not starts with zero!"
                if msg == "OK":
                    break
                else:
                    print(msg)
            except ValueError:
                print("Your zipcode not valid!")
        self.zipcode = zipcode

    def input_city(self):
        city = ""
        while True:
            city = input("Please enter the city: ")
            if city == "\\quit":
                raise UserInterrupt("input_city")
            msg = "OK"
            if city.capitalize() not in Donation.citylist:
                msg = "You can not make a donation in " + city
                print("You must choose between:", Donation.citylist)
            if msg == "OK":
                break
            else:
                print(msg)
        self.city = city

    def input_address(self):
        address = ""
        while True:
            address = input("Please enter the address: ")
            if address == "\\quit":
                raise UserInterrupt("input_address")
            msg = "OK"
            if len(address) > 25:
                msg = "Address is too long! Can not be longer than 25 character!"
            if msg == "OK":
                break
            else:
                print(msg)
        self.address = address

    def input_successful_donation(self):
        successful_donation = ""
        int_successful_donation = 0
        while True:
            successful_donation = input("Please enter successful donation number: ")
            if successful_donation == "\\quit":
                raise UserInterrupt("input_successful_donation")
            try:
                int_successful_donation = int(successful_donation)
                msg = "OK"
                if int_successful_donation <= 0:
                    msg = "Successful donation must be integer!"
                if msg == "OK":
                    break
                else:
                    print(msg)
            except ValueError:
                print("Successful donation must be integer!")
        self.successful_donation = int_successful_donation

    def input_n_beds(self):
        s_n_beds = ""
        p_n_beds = 0
        while True:
            s_n_beds = input("Please, enter the Number of Beds Available: ")
            if s_n_beds == "\\quit":
                raise UserInterrupt("input_n_beds")
            try:
                p_n_beds = int(s_n_beds)
                msg = "OK"
                if p_n_beds <= 0:
                    msg = "Number of Beds must be a positive integer!"
                if msg == "OK":
                    break
                else:
                    print(msg)
            except ValueError:
                print("Input cannot be parsed as an integer!")
        self.n_beds = p_n_beds
        self.max_n_donors = Donation.calc_max_n_donors(self.duration, p_n_beds)

    def input_planned_n_donors(self):
        s_planned_n_donors = ""
        p_planned_n_donors = 0
        while True:
            s_planned_n_donors = input("Please, enter the Planned Number of Donors: ")
            if s_planned_n_donors == "\\quit":
                raise UserInterrupt("input_planned_n_donors")
            try:
                p_planned_n_donors = int(s_planned_n_donors)
                msg = "OK"
                if p_planned_n_donors <= 0:
                    msg = "Planned Number of Donors must be a positive integer!"
                elif p_planned_n_donors > self.max_n_donors:
                    msg = "Planned Number of Donors exceeds Maximum Number of Donors!"
                if msg == "OK":
                    break
                else:
                    print(msg)
            except ValueError:
                print("Input cannot be parsed as an integer!")
        self.planned_n_donors = p_planned_n_donors

    def calc_succession_of_event(self):
            if self.successful_donation < self.planned_n_donors * 0.2:
                print("Unsuccessful, not worths to organise there again")
            elif self.successful_donation < self.planned_n_donors * 0.75:
                print("Normal event")
            elif self.successful_donation < self.planned_n_donors * 1.1:
                print("Successful")
            else:
                print("Outstanding")
