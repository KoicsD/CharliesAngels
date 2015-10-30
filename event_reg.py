from datetime import datetime, time, timedelta


class Donation:
    preparation_time = 30
    donation_time = 30
    citylist = ["Miskolc", "Kazincbarcika", "Szerencs", "Sarospatak"]

    @staticmethod
    def calc_max_n_donors(duration, n_beds):
        return ((duration - Donation.preparation_time) / Donation.donation_time) * n_beds

    def __init__(self):
        print("You can escape any time by typing '\quit'.")
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

        if self.input_date():
            return
        if self.input_start_time():
            return
        if self.input_end_time():
            return
        if self.input_zipcode():
            return
        if self.input_n_beds():
            return
        if self.input_planned_n_donors():
            return
        if self.input_successful_donation():
            return
        if self.calc_succession_of_event():
            return

    def input_date(self):
        sdate = ""
        while True:
            sdate = input("Please enter date of event (YYYY.MM.DD): ")
            if sdate == "\\quit":
                return True
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
        return False

    def input_start_time(self):
        starttime = ""
        pstarttime = time()
        while True:
            starttime = input("Please enter the start time of event (HH:MM): ")
            if starttime == "\\quit":
                return True
            try:
                pstarttime = datetime.strptime(starttime, "%H:%M").time()
                break
            except ValueError:
                print("Wrong format for time!")
        self.start_time = pstarttime
        return False

    def input_end_time(self):
        endtime = ""
        pendtime = 0
        duration = 0
        while True:
            endtime = input("Please enter the end time of event (HH:MM): ")
            if endtime == "\\quit":
                return True
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
        return False

    def input_zipcode(self):
        zipcode = ""
        while True:
            zipcode = input("Please enter the zipcode (ex:1234): ")
            if zipcode == "\\quit":
                return True
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
        return False

    def input_city(self):
        city = ""
        while True:
            city = input("Please enter the city: ")
            if city == "\\quit":
                return True
            msg = "OK"
            if city.lower() not in Donation.citylist:
                msg = "You can not make a donation in " + city
                print("You must choose between:", Donation.citylist)
            if msg == "OK":
                break
            else:
                print(msg)
        self.city = city
        return False

    def input_address(self):
        address = ""
        while True:
            address = input("Please enter the address: ")
            if address == "\\quit":
                return True
            msg = "OK"
            if len(address) > 25:
                msg = "Address is too long! Can not be longer than 25 character!"
            if msg == "OK":
                break
            else:
                print(msg)
        self.address = address
        return False

    def input_successful_donation(self):
        successful_donation = 0
        while True:
            try:
                successful_donation = input("Please enter successful donation number: ")
                if successful_donation == "\\quit":
                    return True
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
        return False

    def input_n_beds(self):
        s_n_beds = ""
        p_n_beds = 0
        while True:
            s_n_beds = input("Please, enter the Number of Beds Available: ")
            if s_n_beds == "\\quit":
                return True
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
        return False

    def input_planned_n_donors(self):
        s_planned_n_donors = ""
        p_planned_n_donors = 0
        while True:
            s_planned_n_donors = input("Please, enter the Planned Number of Donors: ")
            if s_planned_n_donors == "\\quit":
                return True
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
        return False

    def calc_succession_of_event(self):
            if self.successful_donation < self.planned_n_donors * 0.2:
                print("Unsuccessful, not worths to organise there again")
            elif self.successful_donation < self.planned_n_donors * 0.75:
                print("Normal event")
            elif self.successful_donation < self.planned_n_donors * 1.1:
                print("Successful")
            else:
                print("Outstanding")
