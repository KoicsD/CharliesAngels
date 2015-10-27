__author__ = 'KoicsD'


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
        # ((event_duration_in_minutes - preparation_time) / donation_time) * number_of_bedsû
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
# ((event_duration_in_minutes - preparation_time) / donation_time) * number_of_bedsû
#
# preparation_time = 30
# donation_time = 30
# At the end of the event registration ask the user about how many successfull donation was on the event and store it as an integer!