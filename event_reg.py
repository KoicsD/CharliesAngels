__author__ = 'KoicsD'
from datetime import datetime, time, timedelta

        # Date of event and start and end time
                # Registration should occur before the event at least 10 days
                # Datetime can be only on weekdays
                # you can use datetime.isoweekday() function to determine it
                # Start time of donation
                # End time of donation
                # (You can use datetime.strptime to convert the string into datetime type.)
        # Address
                # Zip code (only 4 digit positive integers allowed)
                # City (See below)
                # ZIP is valid only when it contains exactly 4 digit and the first one is not 0,
                # Streetname maximum length is 25,
                # City is in this list: Miskolc, Kazincbarcika, Szerencs, Sarospatak
# Planning
        # How many bed will be available? (Only positive integers allowed)
        # Planned donor number (Only positive integers allowed)
        # max_donor_number =
        # ((event_duration_in_minutes - preparation_time) / donation_time) * number_of_beds
#
        # preparation_time = 30
        # donation_time = 30
        # At the end of the event registration ask the user about how many successfull donation was on the event and store it as an integer!
#
#
# Functions:
#           Registration should occur before the event at least 10 days
#           Datetime can be only on weekdays
#           you can use datetime.isoweekday() function to determine it
#           Address validation
#           ZIP is valid only when it contains exactly 4 digit and the first one is not 0,
#           Streetname maximum length is 25,
#           City is in this list: Miskolc, Kazincbarcika, Szerencs, Sarospatak
# Calculate duration in minutes based on start and endtime
# You can use datetime.strptime and  timedelta.total_seconds functions
# max_donor_number =
# ((event_duration_in_minutes - preparation_time) / donation_time) * number_of_beds
#
# preparation_time = 30
# donation_time = 30
# At the end of the event registration ask the user about how many successfull donation was on the event and store it as an integer!


class Donation:
    preparation_time = 30
    donation_time = 30
    citylist = ["Miskolc", "Kazincbarcika", "Szerencs", "Sarospatak"]

    @staticmethod
    def calc_max_n_donors(duration, n_beds):
        return ((duration - Donation.preparation_time) / Donation.donation_time) * n_beds

    def __init__(self):
        self.date = datetime(1, 1, 1).date()
        self.start_time = time()
        self.end_time = time()
        self.valid = False
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
        self.input_n_beds()
        self.input_planned_n_donors()
        self.input_successful_donation()
        self.calc_succession_of_event()

    def input_date(self):
        sdate = ""
        while True:
            sdate = input("Please enter date of event (YYYY.MM.DD): ")
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
            msg = "OK"
            if city.lower() not in Donation.citylist:
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
            msg = "OK"
            if len(address) > 25:
                msg = "Address is too long! Can not be longer than 25 character!"
            if msg == "OK":
                break
            else:
                print(msg)
        self.address = address

    def input_successful_donation(self):
        successful_donation = 0
        while True:
            try:
                successful_donation = input("Please enter successful donation number: ")
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
                print("Unsuccessfull, not worths to organise there again")
            elif self.successful_donation < self.planned_n_donors * 0.75:
                print("Normal event")
            elif self.successful_donation < self.planned_n_donors * 1.1:
                print("Successfull")
            else:
                print("Outstanding")