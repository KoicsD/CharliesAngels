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
Eventually, we had to rebase our database from [*CSV*](https://en.wikipedia.org/wiki/Comma-separated_values) to [*MySQL*](https://www.mysql.com/) (keeping the existing [*CSV*](https://en.wikipedia.org/wiki/Comma-separated_values) functionallity as well).
It has turned out to be a difficult task for our course, and a lot of groups have not managed to deal with it.
Because of it, we have never presented our solution to mentors.  
However, we managed to implement what we undertook.
To tell the truth, we managed to implement all the basic functions and you can see spectacular results in our repository.

Note:  
* To run this version of our application, you need to install [*MySQL connector for python*](https://dev.mysql.com/downloads/connector/python/).
* Our config file is named [*my_app.config*](my_app.config).
  * You have to copy it into directory *DATA/*, otherwise our application cannot run.
  * You also have to edit it and give correct parameters in it.
  * You can use the [*SQL* script-files](https://www3.ntu.edu.sg/home/ehchua/programming/sql/MySQL_Intermediate.html) of [directory *SQL*](https://github.com/KoicsD/CharliesAngels/tree/Week7B/SQL) to create database on server and to fill it with sample data. (see below)
  * If you want to use [*csv* files](https://en.wikipedia.org/wiki/Comma-separated_values) instead of [*MySQL*](https://www.mysql.com/) server, please replace word *"db"* to *"csv"* in line *'"mode": "db"'*.

Tip: To easily install [*MySQL*](https://www.mysql.com/) software on Windows, please [download this](https://dev.mysql.com/downloads/windows/installer/5.7.html).

-------------------------

## What we undertook and implemented
* we can tell the software which mode to work in via *.config* file,  
  and our application can connect to the database server the parameters of which are given in the file  
  -- though, [our *.config* file](my_app.config) has a different syntax from [the given example](app.config)
* our application can add new *Donor* or *Donation* event into [*MySQL*](https://www.mysql.com/) database
* our application can remove *Donor*s and *Donation* events from [*MySQL*](https://www.mysql.com/) database
* our application can list (and even sort) *Donor*s and *Donation* events present in [*MySQL*](https://www.mysql.com/) database

### What is missing:
* field-by-field modification in [*MySQL*](https://www.mysql.com/) mode
* searching in [*MySQL*](https://www.mysql.com/) mode

-------------------------

## Structural change of code

### New module for working with [*MySQL*](https://www.mysql.com/)

Since module [*data_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/data_handler.py) was quite huge, we chose to add a new module, namely [*sql_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sql_handler.py) to allow our code to send [*MySQL*](https://www.mysql.com/) codes to a given database server.
The new module uses almost the same modules as [*data_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/data_handler.py), but there are exceptions:
* instead of [*CSV* module](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv),
  [module *mysql.connector*](https://dev.mysql.com/doc/connector-python/en/) is used,
* module [*donor_csv_writer*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_csv_writer.py) and
  [*delete_donor*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/delete_donor.py) is not used at all in this mode

Module [*sort_by_order*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sort_by_order.py) was refactored in order to make possible listing data in [*MySQL*](https://www.mysql.com/) mode as well.
It got new functions that receive a [*cursor* object](https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html), and prerform listing *Donor*s or *Donation* events from [*MySQL*](https://www.mysql.com/) server.
The old functions, working on [*CSV*](https://en.wikipedia.org/wiki/Comma-separated_values) files, became [staticmethods](https://docs.python.org/3/library/functions.html?highlight=staticmethod#staticmethod) of a class, and new functions was implemented as [staticmethods](https://docs.python.org/3/library/functions.html?highlight=staticmethod#staticmethod) of another class.

Both storing new data on server and deleting record from server is performed by [*sql_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sql_handler.py), that is why module [*donor_csv_writer*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_csv_writer.py) and [*delete_donor*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/delete_donor.py) is not necessary.
(We modifyed [*donor_reg*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_reg.py) to make it possible not to use [*donor_csv_writer*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/donor_csv_writer.py).)

### Reading config file -- using [*json* module](https://docs.python.org/3/library/json.html?highlight=json#module-json)

Reading config file is performed by *main* module when starting up the application.
Function *initialize* reads *DATA/[my_app.config](my_app.config)* and parses it using [*python*](https://www.python.org)'s built-in [*json* module](https://docs.python.org/3/library/json.html?highlight=json#module-json).
It decides which mode to work in, and gives the appropriate module the alias *working_module* and invokes its own *initialize* function.
If *working_module* is [*sql_handler*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/main.py), *[main](https://github.com/KoicsD/CharliesAngels/blob/Week7B/main.py).initialize* passes connection parameters to *[sql_handler](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sql_handler.py).initialize*, which invokes [function *connect* from module *mysql.connector*](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html).
Finally, *[main](https://github.com/KoicsD/CharliesAngels/blob/Week7B/main.py).initialize* constructs the global variable *main_menu* using the alias *working_module*.

As mentioned above, we use different syntax from [sample](app.config) in config file.
The syntax of [our config file](my_app.config) reminds us of [dictionaries](https://docs.python.org/3/library/stdtypes.html?highlight=dict#dict) in [*python*](https://www.python.org).
This syntax is used in [*.json* files](https://en.wikipedia.org/wiki/JSON), and [*json* module](https://docs.python.org/3/library/json.html?highlight=json#module-json) can parse it as a [dictionary](https://docs.python.org/3/library/stdtypes.html?highlight=dict#dict).
Our application exploits this phenomenon.  
(What is more, parameters of connection is a *dictionary inside dictionary*.
In case of our syntax, the keys of it are equal to the names of arguments of [function *connect*](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html).
Because of it, if we pass it to [function *connect*](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html) with [double-asterisk operator](http://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/), we do not have to explicitely deal with its items in our code.
That's how our code works, and that is the reason why we changed syntax.)

Note:  

Althogh [*python*](https://www.python.org) has a built-in module named [*configparser*](https://docs.python.org/3/library/configparser.html?highlight=config%20parser#module-configparser) for parsing [configuration files (eg. *.ini*)](https://en.wikipedia.org/wiki/Configuration_file),
it is not related to our config file.
Eventually, xtension *.config* is used for many kind of configuration files with non-official syntax.
What we actually did is a [*.json* file](https://en.wikipedia.org/wiki/JSON) with extension *.config*.

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
* [*SQL/*](https://github.com/KoicsD/CharliesAngels/tree/Week7B/SQL) -- directory of [*SQL* script-files](https://www3.ntu.edu.sg/home/ehchua/programming/sql/MySQL_Intermediate.html), see below
* [*sql_handler.py*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sql_handler.py) -- new module
* [*UML/*](https://github.com/KoicsD/CharliesAngels/tree/Week7B/UML) -- directory of [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language#Diagrams) diagrams, inherited from [*Week6B*](https://github.com/KoicsD/CharliesAngels/tree/Week6B), see also [Description of Week6](OrdersWeek6.md)

### Unused files:
* [*List_donors*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/List_donors.py) -- inherited from [*Week5B*](https://github.com/KoicsD/CharliesAngels/tree/Week5B), see also [Description of Week5](OrdersWeek5.md)
* [*sort_the_list_by_order*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/sort_the_list_by_order) -- inherited from [*Week5B*](https://github.com/KoicsD/CharliesAngels/tree/Week5B), see also [Description of Week5](OrdersWeek5.md)

-------------------------

## *SQL* script-files

We created two [SQL script-files](https://www3.ntu.edu.sg/home/ehchua/programming/sql/MySQL_Intermediate.html), that you can find in [directory *SQL*](https://github.com/KoicsD/CharliesAngels/tree/Week7B/SQL):

* [*create.sql*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/SQL/create.sql)  
  This file creates the databese, named *BloodDonations*.
  It also creates the tables and constraints in database.  
* [*insert.sql*](https://github.com/KoicsD/CharliesAngels/blob/Week7B/SQL/insert.sql)  
  Use this file to insert some sample data into database *BloodDonations*.

But note that these FILES CONTAIN NO INFORMATION ABOUT CONNECTION!

-------------------------

## What we have learnt

We have learnt that sometimes you only need to change a little thing (eg. the syntax of a file) and you can use preconstructed tools to reach your goals.
On the other hand, I think you should be careful when doing so: sometimes understanding someone else's thoughts takes longer than eg. creating your own parser.
(In addition, such a change like the syntax of a config file may require the complience of customer.)  
Anyway, we managed to connect [*python*](https://www.python.org/) and [*MySQL*](https://www.mysql.com/), which was useful to develop our hard-skills as well.

-------------------------------------------------------
-------------------------------------------------------

[Previous: Week6](OrdersWeek6.md)  
[Back to README](../README.md)
