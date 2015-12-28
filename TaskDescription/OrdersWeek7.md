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
Eventually, we had to rebase our database from [CSV] to [MySQL] (keeping the existing [CSV] functionallity as well).
It has turned out to be a difficult task for our course, and a lot of groups have not managed to deal with it.
Because of it, we have never presented our solution to mentors.
However, we managed to implement what we undertook.
To tell the truth, we managed to implement the basic functions and you can see spectacular results in our repository.

-------------------------

## What we undertook implemented
* we can tell the software which mode to work in via the .config file,  
  and our application can connect to the database server the parameters of which are given in the file
  -- though, our .config file has a different syntax from the given example
* we can add new *Donor* or *Donation* event into [SQL] database
* we can remove *Donor*s and *Donation* events from [SQL] database
* we can list *Donor*s and *Donation* events present in [SQL] database

-------------------------

## What we have learnt

bla

-------------------------------------------------------
-------------------------------------------------------

[Previous: Week6](OrdersWeek6.md)  
[Back to README](../README.md)
