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
# Registration should occur before the event at least 10 days
# Datetime can be only on weekdays
# you can use datetime.isoweekday() function to determine it
# Address validation
# ZIP is valid only when it contains exactly 4 digit and the first one is not 0,
# Streetname maximum length is 25,
# City is in this list: Miskolc, Kazincbarcika, Szerencs, Sarospatak
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
    citylist = ["Miskolc", "Kazincbarcika", "Szerencs", "Sarospatak"]

    def __init__(self):
        self.date = datetime(1,1,1).time()
        self.start_time = time()
        self.end_time = time()
        self.duration_time = 0
        self.valid = False
        self.duration = 0
        self.zipcode = ""
        self.streetname = ""
        self.city = ""

        self.input_date()
        self.input_start_time()
        self.input_end_time()

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
                if not zipcode.isdigit() and len(zipcode) == 4:
                    msg = "Your zipcode not valid!"
                msg = "OK"
                if msg == "OK":
                    break
            except:
                print("Your zipcode not valid!")


