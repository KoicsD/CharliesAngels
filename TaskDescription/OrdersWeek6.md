# Modify donor data

As a user I'd like to modify the saved data that belong to the donor.
I'd like to have the opportunity to change any data I want.

## Acceptance:

* The donor's data can be changed
* The changed data is saved permanently.
* The data is valid after the modification as well.
* The ID is changable but it is still unique
* This function is reachable from "Change" menü
* The change menu is ask an ID and detect if it a donor or donation
* The data to donor or donation is listed and new data is asked. I can see the old date to compare.
* If id is not found then inform the user.
* If it saved inform the user.
* Step back is possible when I press ESC. In this case data is not saved.

----------------------------------------------
----------------------------------------------

# Modify donation data

As a user I'd like to modify the saved data that belong to the donation.
I'd like to have the opportunity to change any data I want.

## Acceptance:

* The donation's data can be changed
* The changed data is saved permanently.
* The data is valid after the modification as well.
* This function is reachable from "Change" menü
* The change menu is ask an ID and detect if it a donor or donation
* The data to donor or donation is listed and new data is asked. I can see the old date to compare.
* If id is not found then inform the user.
* If it saved inform the user.
* Step back is possible when I press ESC. In this case data is not saved.

------------------------------------------------
------------------------------------------------

# What we have done

The last commit of this sprint is dated on 27th Nov under tag [Week6B](https://github.com/KoicsD/CharliesAngels/tree/Week6B).
Although it was a normal 5-days-long [sprint]-week, we managed to not only implement what we had not undertaken during the [previous sprint], but also managed to implement the new "user-requirements".
We have to mention, that mentors gave fewer new requirements, as they were aware of that a lot of [SCRUM]-group had not managed to fulfill [previous-sprint] requirements.

--------------------------

## What we undertook and what we implemented

### What we undertook:
* what we had not undertaken during the [previous sprint]:
  * making listers the same in case of *Donor*s and *Donation* events
  * implementing *Donation-searcher*
  * extending listers with sorters
* new "user-requirements":
  * making possible to change *Donor* and *Donation* data field-by-field
  * extending possibility of user-interruption from [*event-reg*] to [*donor_reg*],  
    and rebasing it from string "\quit" to key 'Esc'

### What we implemented:
* what we had not undertaken during the [previous sprint]:
  * making listers the same in case of *Donor*s and *Donation* events
  * implementing *Donation-searcher*
  * extending listers with sorters
* new "user-requirements":
  * making possible to change *Donor* and *Donation* data field-by-field
  * extending possibility of user-interruption from [*event-reg*] to [*donor_reg*],  
    (but not: rebasing it from string "\quit" to key 'Esc'
    -- at this point we managed to come to a compromise with mentors)
* bugfix:
  * there turned out to be a bug in checking the unity of new *Donor*'s *unique id*  
    and it had been possible to take two (or more) *Donor*s into the database with the same id  
    -- we managed to fix this bug

--------------------------

## Changes of code

### Listing and sorting
Module [List_donors] was replaced by [sortsort_by_order], in order to make possible sorted listing.
The new lister module can list not only *Donor*s but *Donation* events as well.
(*Donation*-lister was implemented in the [original module] as well, before disposing it)

### *Donation*-searcher
Module [search_in_files] got a new function, so it can search not only in *Donor*s but *Donation* events as well.

### Modifyable data
Field-by-field modification of *Donation* events is done by a new function in module [data_handler].  
In case of *Donor*s, function in [data_handler] is just for forwarding controll to a new module, named [modify_donor_data].
The new module asks user which field to modify and use module [donor_reg] to input and store new data.

### User-interruption
The possibility of exception-based user-interruption was spread from [event_reg] to [donor_reg].
It is still based on the string "\quit" rather than key 'Esc'.
Using key 'Esc' would have required overdefining built-in function *input*, which would have been quite a difficult task.
(However, [one of my friends] outside our group has managed to create a similar input-function within a class called 'MagicInput'...)
Fortunally, we managed to aggree with mentors that our interrupter is acceptable.

--------------------------

## Summary of files and directories

To summarize, here are our files and directories under tag [*Week6B*]:

### Directories and module-files:
* [*data_handler.py*]  
* [*delete_donor.py*]  
* [*donor_csv_writer.py*]  
* [*donor_reg.py*]  
* [*event_reg.py*]  
* [*main.py*]  
  This is the entry-point.  
* [*menu.py*]  
* [*modify_donor_data.py*]  
* [*search_in_files.py*] 
* [*sort_by_order.py*]  
* [*UML/*]  
  This is a directory containing UML diagrams for our projects. See details below.

### Unused files:
* [*List_donors.py*]  
  Functionally replaced by [*sort_by_order.py*] but physically not deleted.  
* [*sort_the_list_by_order.py*]  
  Inherited from tag [*Week5B*].

--------------------------

## [UML diagrams]
Before this sprint, we got acquainted with [UML]. For this reason, I created some diagrams, and stored them in a new directory, named [*UML/*]:
* [*all_components.dia*]:  
  This is a diagram about our files and their dependencies (import) on each other and built-in python modules.  
* [*inner_components.dia*]:  
  This diagram is similar to the former one, but it contains only our own files.  
* [*components_as_it_could_be.dia*]:  
  This diagram is also similar to the above two ones, but it shows my idea of general user-input function.
  -- The function that would ask user for a string repeatedly, until the user-given string is accepted by a given checker and validator function.
  This function is planned into a new module, named *user_input*.  
* [*class_donor_reg_components.dia*]:  
  This diagram shows my first (and quite silly) idea about methods of a *Donor* class in module [*donor_reg*].
  As you can see there are too many methods in one class, which is hardly readable and brings up code-arrangement questions.
  ([One of the mentors] called this phenomenon "god-object".)

--------------------------

## Branch [*classizing*]

[Zoltán Székely] undertook to make an expirement on classizing *Donor* data-handling, but he did not manage to do this refactoring during the time of our sprint.
You can find his results on branch [*classizing*].
His work is based on my outside-master branch named [*classize_donor*]. (see also [*OutsideMaster.md*])

--------------------------

## What we have learnt

As our code is relatively well-structured, we could see that it is very easy to add new features to a well-arranged application, even though, our code was based on two contradictory (an [object oriented] and a [procedure-oriented]) principle.
On the other hand, [Zoltán Székely]'s experience on unifying these points of view showed us: Having the right plan at the beginning of coding is much easier than refactoring after hundreds of lines of codes.

------------------------------------------------
------------------------------------------------

[Next: Week7](OrdersWeek7.md)  
[Previous: Week5](OrdersWeek5.md)  
[Back to README](../README.md)
