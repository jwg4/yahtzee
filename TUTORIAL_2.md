Tutorial 2 - Defining a function
=======
Commit: a0a69100f73157028b32693c0b439309f7d55468
File: https://github.com/jwg4/yahtzee/blob/a0a69100f73157028b32693c0b439309f7d55468/yahtzee.py

We made one big change and a couple of small ones here. First we moved the code which rolls the dice into a function. This is done with `def` and `return`. `def` is followed by the name of the function, the arguments in brackets (we don't have any arguments here) and a colon ':'. Everything in the indented block which follows will be run when the function is called.

If the keyword `return` appears somewhere in the code, followed by an expression, the function will stop running and return that value. If the execution never gets to the word `return` before the end of the block, the function returns the special value `None`.

Here we define the list `l` as before, append the results of calling the dice roll API five times, and then return `l`. Note that the `for` loop is a now a doubly-indented block - because it's a block within a block.

