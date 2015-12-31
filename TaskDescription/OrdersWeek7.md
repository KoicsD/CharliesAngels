# Centralized data storage

As a user I want to store my saved data in a centralized storage. I have a MySQL server so I want to use it as a storage.

-------------

## Acceptance:

* I can configure in a config file that which way I want to store my data (See attachment)
* Mode can be (only one at a time):
  * csv
  * db
* I can connect to any available DB source by configuring the connection string
* The csv store is working as well by configuration
* All previous requirements still satisfied

------------

[app.config](app.config)  
This is a sample about the configuration file.

-------------------------------------------------------
-------------------------------------------------------

# What we have done

You can find our work under tag [Week7B](https://github.com/KoicsD/CharliesAngels/tree/Week7B) with date 12th Dec.
Eventually, we had to rebase our database from [*CSV*] to [*MySQL*] - (keeping the existing [*CSV*] functionallity as well).
It has turned out to be a difficult task for our course, and a lot of groups have not managed to deal with it.
Because of it, we have never presented our solution to mentors.  
However, we managed to implement what we undertook.
To tell the truth, we managed to implement the basic functions and you can see spectacular results in our repository.

Note:  
* To run this version of our application, you need to install [*MySQL connector for python*](https://dev.mysql.com/downloads/connector/python/).
* Our config file is named [*my_app.config*].
  * You have to copy it into directory *DATA/*, otherwise our application cannot run.
  * You also have to edit it and give correct parameters in it.
  * You can use the [SQL script-files] of [directory *SQL/*] to create database on server and to fill it with sample data. (see below)
  * If you want to use [*csv* files] instead of [*MySQL* server], please replace word *"db"* to *"csv"* in line *'"mode": "db"'*.

-------------------------

## What we undertook and implemented
* we can tell the software which mode to work in via *.config* file,  
  and our application can connect to the database server the parameters of which are given in the file  
  -- though, [our *.config* file](my_app.config) has a different syntax from [the given example](app.config)
* our application can add new *Donor* or *Donation* event into [*MySQL*] database
* our application can remove *Donor*s and *Donation* events from [*MySQL*] database
* our application can list (and even sort) *Donor*s and *Donation* events present in [*MySQL* database]

### What is missing:
* field-by-field modification in [*MySQL*] mode
* searching in [*MySQL*] mode

-------------------------

## Structural change of code

### New module for working with [*MySQL*]

Since module [*data_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/data_handler.py) was quite huge, we chose to add a new module, namely [*sql_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sql_handler.py) to allow our code to send [*MySQL*] codes to a given database server.
The new module uses almost the same modules as [*data_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/data_handler.py), but there are exceptions:
* instead of [*CSV* module], module [*mysql.connector*] is used,
* module [*donor_csv_writer*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_csv_writer.py) and [*delete_donor*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/delete_donor.py) is not used at all in this mode

Module [*sort_by_order*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sort_by_order.py) was refactored in order to make possible listing data in [*MySQL*] mode as well.
It got new functions that receive a [*cursor*] object, and prerform listing *Donor*s or *Donation* events from [*MySQL*] server.
The old functions, working on [*CSV*] files, became [staticmethods] of a class, and new functions was implemented as [staticmethods] of another class.

Both storing new data on server and deleting record from server is performed by [*sql_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sql_handler.py), that is why module [*donor_csv_writer*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_csv_writer.py) and [*delete_donor*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/delete_donor.py) is not necessary.
(We modifyed [*donor_reg*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_reg.py) to make it possible not to use [*donor_csv_writer*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_csv_writer.py).)

### Reading config file -- using [*json* module]

Reading config file is performed by *main* module when starting up the application.
Function *initialize* reads *DATA/[my_app.config]* and parses it using [*python*]'s built-in [*json* module].
It decides which mode to work in, and gives the appropriate module the alias *working_module* and invokes its own *initialize* function.
If *working_module* is [*sql_handler*], *[main](https://github.com/KoicsD/CharliesAngels/blob/Week7B/main.py).initialize* passes connection parameters to *[sql_handler](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sql_handler.py).initialize*, which invokes function [*connect*] from module [*mysql.connector*].
Finally, *[main](https://github.com/KoicsD/CharliesAngels/blob/Week7B/main.py).initialize* constructs the global variable *main_menu* using the alias *working_module*.

As mentioned above, we use different syntax from [sample](app.config) in config file.
The syntax of [our config file](my_app.config) reminds us of [dictionaries] in [*python*].
This syntax is used in [*.json*] files, and [*json* module] can parse it as a [dictionary].
Our application exploits this phenomenon.  
(What is more, parameters of connection is a *dictionary inside dictionary*.
In case of our syntax, the keys of it are equal to the names of arguments of function *connect*.
Because of it, if we pass it to function *connect* with [double-asterisk operator], we do not have to explicitely deal with its items in our code.
That's how our code works, and that is the reason why we changed syntax.)

-------------------------

## Summary of files and directories

### Directories and module-files:
* [*data_handler.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/data_handler.py)
* [*delete_donor.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/delete_donor.py)
* [*donor_csv_writer.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_csv_writer.py)
* [*donor_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_reg.py)
* [*event_reg.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/event_reg.py)
* [*main.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/main.py) -- This is the entry point.
* [*menu.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/menu.py)
* [*modify_donor_data.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/modify_donor_data.py)
* [*search_in_files.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/search_in_files.py)
* [*sort_by_order.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sort_by_order.py)
* [*SQL/*](https://github.com/KoicsD/CharliesAngels/tree/Week7B/SQL) -- directory of [SQL script-files], see below
* [*sql_handler.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sql_handler.py) -- new module
* [*UML/*](https://github.com/KoicsD/CharliesAngels/tree/Week7B/UML) -- directory of [UML] diagrams, inherited from [*Week6B*], see also [Description of Week6](OrdersWeek6.md)

### Unused files:
* [*List_donors*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/List_donors.py) -- inherited from [*Week5B*], see also [Description of Week5](OrdersWeek5.md)
* [*sort_the_list_by_order*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sort_the_list_by_order) -- inherited from [*Week5B*], see also [Description of Week5](OrdersWeek5.md)

-------------------------

## [SQL script-files](https://github.com/KoicsD/CharliesAngels/tree/Week7B/SQL)

We created two [SQL script-files], that you can find in [directory *SQL*](https://github.com/KoicsD/CharliesAngels/tree/Week7B/SQL):

* [*create.sql*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/SQL/create.sql)  
  This file creates the databese, named *BloodDonations*.
  It also creates the tables and constraints in database.  
* [*insert.sql*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/SQL/insert.sql)  
  Use this file to insert some sample data into database *BloodDonations*.

But note that these FILES CONTAIN NO INFORMATION ABOUT CONNECTION!

-------------------------

## What we have learnt

We have learnt that sometimes you only need to change a little thing and you can use preconstructed tools to reach your goals.
On the other hand, I think you should be careful when doing so: sometimes understanding someone else's thoughts takes longer than eg. creating your own parser.  
We managed to connect python and MySQL, which was useful to develop our hard-skills as well.

-------------------------------------------------------
-------------------------------------------------------

[Previous: Week6](OrdersWeek6.md)  
[Back to README](../README.md)
