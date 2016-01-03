# Outside master

I had a lot of idea about managing and refactoring our code, and for this reason I created some branches outside [*master*](https://github.com/KoicsD/CharliesAngels/tree/master).
Outside-master branches were also used to implement some features without disturbing the workfow of branch [*master*](https://github.com/KoicsD/CharliesAngels/tree/master).
In this case, as soon as the feature had been implemented, it was merged into [*master*](https://github.com/KoicsD/CharliesAngels/tree/master).

In this file you can read about these branches.

## [*refactor_event*](https://github.com/KoicsD/CharliesAngels/tree/refactor_event)

This branch was created by [me] after the demo of [sprint Week4B](InitalOrders.md).
The purpose was to refactor validator and checker logic into separate parser functions in [*event_reg.py*] and to implement the engine of user-input functions in a separate user-input module, [*user_input.py*].
This engine would have been the only function in our code that invokes builtin *input* function when adding a new *Donation* event (or *Donor*).

The function itself was named *user_input*.
It contained a while loop that should have invoked *input* repeatedly until user gave acceptable data.
It took 4 input arguments:
* *inp_prompt*:  
  input prompt to show to user
* *parser_fcn*:  
  function delegate of the parser function
* *inp_args*:  
  list of additional input arguments for parser function
* *parse_err_msg* (optional):  
  a message to show when parser fails (ie. *ValueError* is raised)

With this refactoring unit-testing of module [*event_reg*] would have became achieveable. Although a unit-test file was added by [me], this branch is not complete and it has never been used by branch [*master*] because of lack of time.

## [*classize_donor*](https://github.com/KoicsD/CharliesAngels/tree/classize_donor)

This is my another side-branch between [sprint *Week4*] and [sprint *Week5*].
It shows step-by-step (commit-by-commit) how data of [*donor_reg*] can be arranged into a class.
It's worth to watch all the deltas on it.

## [*data_handler_module*](https://github.com/KoicsD/CharliesAngels/tree/data_handler_module)

This branch was created during [sprint *Week5B*]
and it formed an integral part of the sprint.
There were 2 changes made on it:
* module [donor_reg] was refactored
* module [data_handler] was created

## [*classizing*](https://github.com/KoicsD/CharliesAngels/tree/classizing)

This branch was created by [Zoltán Székely].
His purpose was to apply the classizing of branch [classize_donor] to the current state of our code.
