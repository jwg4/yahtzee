Tutorial 2 - Defining a function
=======
Commit: a0a69100f73157028b32693c0b439309f7d55468
File: https://github.com/jwg4/yahtzee/blob/a0a69100f73157028b32693c0b439309f7d55468/yahtzee.py

We made one big change and a couple of small ones here. First we moved the code which rolls the dice into a function. This is done with `def` and `return`. `def` is followed by the name of the function, the arguments in brackets (we don't have any arguments here) and a colon ':'. Everything in the indented block which follows will be run when the function is called.

If the keyword `return` appears somewhere in the code, followed by an expression, the function will stop running and return that value. If the execution never gets to the word `return` before the end of the block, the function returns the special value `None`.

Here we define the list `l` as before, append the results of calling the dice roll API five times, and then return `l`. Note that the `for` loop is a now a doubly-indented block - because it's a block within a block.

The 'return value' of the function is the value of the expression which calls the function. In other words, 

```
result = get_dice_rolls()
```

runs the function get_dice_rolls, and stores the return value in the variable `result`. If we just had the line 

```
get_dice_rolls()
```

this would mean that the function got called, but that the return value was ignored. This could be useful if the function `get_dice_rolls` had some side-effect, such as printing something to the screen.

Blocks and indentation
------

We have seen a couple of examples of 'blocks'. Usual examples are like these: the 'body' of a function, everything which gets done for an `if` conditional or a `for` loop, and all the code which makes up a `class`. We will see conditionals later and classes much later. Let us look at the two examples of blocks in the current code.

To do some actions again and again in a loop, we have to indicate to Python exactly what we want to be done. The indented block does this - everything below the line starting `for`, which is indented some compared to that line, is done at each repetition of the loop. Everything which comes further down and is no longer indented, is 'outside the block' and is only done once. The same applies to the function. The block following the line `def ...` is what will be run when the function is called. Everything else is just the continuation of the program. So to see what a block is 'about', you should look at the non-indented line which starts it. That line tells you whether the code in the block is the inside of a loop, a function or what.

You can indent a block by any amount, and as long as each line is indented by the same amount, and the lines outside the block go back to the same amount of indentation as before the block, it will be understood. However, it is usual to indent each block by 4 more spaces than the previous one. Doing anything else will make it harder for people to read your code, and is a bad idea unless you have some special reason for doing it.

