Stage 1
=======
Commit: 74d73398bb9b6ff81704b7aa88af0e894cb4c7f1
File: https://github.com/jwg4/yahtzee/blob/74d73398bb9b6ff81704b7aa88af0e894cb4c7f1/yahtzee.py

This is a very basic version of the game yahtzee, in which 5 dice are rolled. The code uses a Web API to retrieve random values for the dice. (Of course, Python could generate the numbers itself. But I wanted to make the code a little more interesting.) The program gets a random value 5 times, and then prints out the 5 values.

To get started, make sure you can run the program:
```
python yahtzee.py
4 4 5 1 6
```

Of course, you will probably get different values. Next you should check that you can run python in interactive mode, so that you can experiment with code from this program. If you run `python` without any filename in a terminal, you should see a bunch of version information, followed by a prompt that looks like this:

```
>>>
```

This is the *REPL*, the read-evaluate-print loop. Python *reads* what you type, *evaluates* it (runs the line you typed, and determines what the output value is), and *prints* the result. You can type each line of the file `yahtzee.py` into the REPL, and the code should have the same effect as when you ran it all in one go from the command line. Let's try doing that, to make sure we understand everything that is going on.

```
>>> import requests
```

This loads the Python HTTP library, **requests**. If you haven't installed this properly, you will get an error message here. The README will help you fix this. If not, you are good to go.

Empty lines are of course only there to make the code more readable, and don't do anything.

```
>>> l = []
```

This creates a variable called `l`, and gives it the value of `[]`, the empty list. Lists are one of the fundamental data types in Python. They are written as square brackets, containing the items of the list separated by commas. So `[1, 2, 3]` would be a list containing the numbers 1, 2 and 3 in that order. `[1, 1, 3, 4]` is another list of numbers. `["asdf", 0.15, 0, "Hello world"]` is a list which contains two strings and two numbers.

The first two lines didn't have any output, so nothing was printed after they were evaluated. However, in both cases invisible things happened in the background. `import requests` loaded the library, so that we can now use the functions defined in it. `l = []` set the value of `l`. You can check this by typing

```
>>> l
[]
```

The value of `l` is output. This is the empty list, exactly what we wrote when we initialized `l`.

```
>>> for i in range(5):
...     r = requests.get('http://rollthedice.setgetgo.com/get.php')
...     l.append(r.text)
... 
```

If you type the first line above into the Python REPL, it will detect that there are more lines comming, and the following lines will start with `...` until you press Enter twice to complete the piece of code.

