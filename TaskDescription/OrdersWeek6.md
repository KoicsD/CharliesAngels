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

## Structure of code

bla
 
--------------------------

## What we have learnt

bla

------------------------------------------------
------------------------------------------------

[Next: Week7](OrdersWeek7.md)  
[Previous: Week5](OrdersWeek5.md)  
[Back to README](../README.md)
