## General requirements:

In your solution use all the techniques what you have learnt before: Classes, Tests, Git repository
Your solution should be in a grithub repository
Your solution should contain enough unit tests which are validating the correct functionality. All the test should pass.
Try to think in object oriented way. So the closely linked data should be in classes.
Your application should contain a main file which is runnable
Code should be correctly commented
Take care of error handling. Program should be working as a stabalized one for any cases. (e.g. incorrect input)
So the task is create an application which suitable for handling blood donation (maybe it is familiar a bit ;)):

----------------------------------------------------------------------
----------------------------------------------------------------------

## Donor registration

### Getting data from user:

* Name,
* Weight,
* Gender,
* Date of Birth,
* Last donation date,
* Was he/she sick in the last month?
* Unique identifier
* Blood type
* Expiration of ID
* email address
* Mobil number

### Functions:

* Parse name, store it in a separated object
* Suitable for donation:  
  weight > 50
* last donation was more than 3 months ago  
  age > 18 years
* How old is the donor in years based on date of birth?
* ID is not expired.
* Define type of personal document based on its identifier:
  * 6digit + 2letter (123456AB) is identity card
  * 6letter + 2digit (ASDFGH12) is passport
* Email address validation (contains @ and ends with .hu/.com)
* Mobil number validation (starts with +36/06 + 2 digit(provider identifier - 20/30/70) ending with 7 digits)
* Write out data in a table form eg.:
```
  Attila, Molnár
  90kg [using of str function]
  1989.05.06 - 26 years old
  asd@test.hu
```
* Generate random number: Hemogblobin level between 80-200, write out is the donor suitable or not (value is greather than 110)?

----------------------------------------

## Donation event registration:

### Getting data from user:

* Date of event
* Start time of donation
* End time of donation
  (You can use [datetime.strptime](https://docs.python.org/3.4/library/datetime.html#strftime-and-strptime-behavior) to convert the string into datetime type.)
* Zip code (only 4 digit positive integers allowed)
* City (See below)
* Address
* How many bed will be available? (Only positive integers allowed)
* Planned donor number (Only positive integers allowed)

### Functions:

* Registration should occur before the event at least 10 days
* Datetime can be only on weekdays
* you can use [datetime.isoweekday](https://docs.python.org/3.4/library/datetime.html#datetime.date.isoweekday) function to determine it
* Address validation
* ZIP is valid only when it contains exactly 4 digit and the first one is not 0,
* Streetname maximum length is 25,
* City is in this list: Miskolc, Kazincbarcika, Szerencs, Sarospatak
* Calculate duration in minutes based on start and endtime
* You can use [datetime.strptime](https://docs.python.org/3.4/library/datetime.html#strftime-and-strptime-behavior) and [timedelta.total_seconds](https://docs.python.org/3.4/library/datetime.html#datetime.timedelta.total_seconds) functions  
  max_donor_number = ((event_duration_in_minutes - preparation_time) / donation_time) * number_of_beds  
  preparation_time = 30  
  donation_time = 30

At the end of the event registration ask the user about how many successfull donation was on the event and store it as an integer!

### How the donation was successfull? The realized donation number:

* is below 20% of planned: "Unsuccessfull, not worths to organise there again"
* is between 20-75% of planned: "Normal event"
* is between 75-110% of planned: "Successfull"
* is above 110% of planned: "Outstanding"

--------------------------------------------------------
--------------------------------------------------------

## What we have done

### [Tag *Week4B*](https://github.com/KoicsD/CharliesAngels/tree/Week4B):

What we have done and our Mentors have seen is under tag [*Week4B*](https://github.com/KoicsD/CharliesAngels/tree/Week4B). That commit was added on *30th Oct*.

There were 3 files:
* [*event_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/event_reg.py) -- This contained donation event data input functions.
* [*donor_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/donor_reg.py) -- This contained donor data input functions.
* [*main.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/main.py) -- This was the entry point, containing a menu to decide whether to input donor or event data.

[*Zsolt Bódi*](https://github.com/bodizsolt1992) and I myself worked on [*event_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/event_reg.py) while [*Zoltán Székely*](https://github.com/Szezol), [*Márton Ozsvár*](https://github.com/ozsvarmartoncc) and [*Gergely Viczmándi*]() worked on [*donor_reg*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/donor_reg.py).
This has had an effect on the structure of our code:
While [*event_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/event_reg.py) had a class-definition providing *Donation*-type objects, [*donor_reg*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/donor_reg.py) was a simple function-collection. In case of *Donation* function [*__ init __*](https://docs.python.org/3/reference/datamodel.html?highlight=__init__#object.__init__) invoked the input functions while *donor_reg* module had a *main* function for this reason.  
In addition [*donor_reg*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/donor_reg.py) was not user-safe (eg. it trumbled when user typed wrong date format) and none of the two mode was able to print inputted data in a table form.  
As a good point, I managed to allow user to quit when inputting data in [*event_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/event_reg.py). If user typed "\quit", control returned to [*main.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/main.py) -- meaning that an invalid *Donation* object was constructed.

### [Tag *Week4B_weekend*](https://github.com/KoicsD/CharliesAngels/tree/Week4B_weekend):

We were not satisfied with ourself on that friday, so we worked on the code all the weekend. You can find our result under tag [*Week4B_weekend*](https://github.com/KoicsD/CharliesAngels/tree/Week4B_weekend). The date of that commit is *1st Nov*.

We fixed and optimized [*donor_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/donor_reg.py) and I developed [*event_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/event_reg.py) further.

In case of [*donor_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/donor_reg.py):
* user-safety problems of [string-parsing *datetime*](https://docs.python.org/3/library/datetime.html?highlight=datetime.strptime#datetime.datetime.strptime) was fixed
* inner structure of module was refactored for optimization purpose
* a printer function was added to print data in a table-like form and it was invoked from function *main*

In case of [*event_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week4B/event_reg.py):
* function [*__ repr __*](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#object.__repr__) was overdefined to make *Donation* objects printable
* *main* function was added and printing was invoked from it after intantiating

In both module, function *main* was automatically invoked if module was run directly as [*__ main __*](https://docs.python.org/3/library/__main__.html?highlight=__main__#module-__main__).

Unfortunatelly, the difference between the point of view of the two modules still remained, demolishing the elegance of our code.

-----------------------

### What we have learnt:
Members should plan togather the whole project at the beginning of the sprint, if you want your code to have a unified structure.
Maybe on the first day a [SCRUM](https://en.wikipedia.org/wiki/Scrum_(software_development))-team should deal with nothing but planning.

--------------------------------------------------------
--------------------------------------------------------

tags:
[error handling](https://docs.python.org/3/tutorial/errors.html?highlight=error%20handling),
[git](https://git-scm.com),
[OOP](https://en.wikipedia.org/wiki/Object-oriented_programming),
[python](https://www.python.org),
[SCRUM](https://en.wikipedia.org/wiki/Scrum_(software_development))

[Next: Week5](OrdersWeek5.md)  
[Back to README](../README.md)
