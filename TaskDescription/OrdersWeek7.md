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
Eventually, we had to rebase our database from [*CSV*] to [*MySQL*] - (keeping the existing [CSV] functionallity as well).
It has turned out to be a difficult task for our course, and a lot of groups have not managed to deal with it.
Because of it, we have never presented our solution to mentors.  
However, we managed to implement what we undertook.
To tell the truth, we managed to implement the basic functions and you can see spectacular results in our repository.

Note: To run this version of our application, you need to install [*MySQL connector for python*](https://dev.mysql.com/downloads/connector/python/).

-------------------------

## What we undertook and implemented
* we can tell the software which mode to work in via *.config* file,  
  and our application can connect to the database server the parameters of which are given in the file  
  -- though, our .config file has a different syntax from the given example
* our application can add new *Donor* or *Donation* event into [*MySQL*] database
* our application can remove *Donor*s and *Donation* events from [*MySQL*] database
* our application can list (and even sort) *Donor*s and *Donation* events present in [*MySQL*] database* 

### What is missing:
* field-by-field modification in [*MySQL*] mode
* searching in [*MySQL*] mode

-------------------------

## Structural change of code

### New module for working with [*MySQL*]

Since module [*data_handler*] was quite huge, we chose to add new module, namely [*sql_handler*] to allow our code to send [*MySQL*] codes to a given database server.
The new module uses almost the same modules as [*data_handler*], but there are exceptions:
* instead of [*CSV* module], module [*mysql.connector*] is used,
* module [*donor_csv_writer*] and [*delete_donor*] is not used at all in this mode

Module [*sort_by_order*] was refactored in order to make possible listing data in [*MySQL*] mode as well.
It got new functions that receive a *cursor* object, and prerform listing *Donor*s or *Donation* events from [*MySQL*] server.
The old functions, working on [*CSV*] files, became [staticmethods] of a class, and new functions was implemented as [staticmethods] of another class.

Both storing new data on server and deleting record from server is performed by [*sql_handler*], that is why module [*donor_csv_writer*] and [*delete_donor*] is not used.
(We modifyed [*donor_reg*] to make it possible not to use [*donor_csv_writer*].)

### Reading config file -- using [*json* module]

We use different syntax from sample in config file.

-------------------------

## Summary of files and directories

### Directories and module-files:
* bla

### Unused files:
* bla

-------------------------

## SQL script-files

bla

-------------------------

## What we have learnt

bla

-------------------------------------------------------
-------------------------------------------------------

[Previous: Week6](OrdersWeek6.md)  
[Back to README](../README.md)
