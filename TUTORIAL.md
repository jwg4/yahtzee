Stage 1 - Running a basic program
=======
Commit: 74d73398bb9b6ff81704b7aa88af0e894cb4c7f1
File: https://github.com/jwg4/yahtzee/blob/74d73398bb9b6ff81704b7aa88af0e894cb4c7f1/yahtzee.py

This is a very basic version of the game yahtzee, in which 5 dice are rolled. The code uses a Web API to retrieve random values for the dice. (Of course, Python could generate the numbers itself. But I wanted to make the code a little more interesting.) The program gets a random value 5 times, and then prints out the 5 values.

To get started, do the stuff in README.md which gets you set up with Python. Make sure you can run the program:
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

If you type the first line above into the Python REPL, it will detect that there are more lines coming, and the following lines will start with `...` until you press Enter twice to complete the piece of code.

The function `range` returns a list of integers:

```
>>> range(5)
[1, 2, 3, 4, 5]
```

We are looping over this list, with the variable `i` being set to each value in the list in turn. In this loop, we don't use `i` anywhere, so we just do the same thing five times.

The function `requests.get` does a GET request of the URL. The requests library is very simple and intuitive and the first page of the docs at http://docs.python-requests.org/en/latest/ explains the most common ways to use it. We assign to the variable `r` the result of the GET.

```
>>> r = requests.get('https://www.cbix.ca/api/v1')
>>> r
<Response [200]>
>>> r.text
u'{"source":"Canadian Bitcoin Index History","source_link":"https:\\/\\/www.cbix.ca","success":true,"methods":{"index":"http:\\/\\/api.cbix.ca\\/v1\\/index","history":"http:\\/\\/api.cbix.ca\\/v1\\/history","convert":"http:\\/\\/api.cbix.ca\\/v1\\/convert","orderbook":"http:\\/\\/api.cbix.ca\\/v1\\/orderbook","summary":"http:\\/\\/api.cbix.ca\\/v1\\/summary","news":"http:\\/\\/api.cbix.ca\\/v1\\/news","notifications":"http:\\/\\/api.cbix.ca\\/v1\\/notifications","analysis":"http:\\/\\/api.cbix.ca\\/v1\\/analysis","sentiment":"http:\\/\\/api.cbix.ca\\/v1\\/sentiment","volatility":"http:\\/\\/api.cbix.ca\\/v1\\/volatility"}}'
>>> r.json()
{u'source': u'Canadian Bitcoin Index History', u'methods': {u'index': u'http://api.cbix.ca/v1/index', u'convert': u'http://api.cbix.ca/v1/convert', u'sentiment': u'http://api.cbix.ca/v1/sentiment', u'analysis': u'http://api.cbix.ca/v1/analysis', u'summary': u'http://api.cbix.ca/v1/summary', u'notifications': u'http://api.cbix.ca/v1/notifications', u'orderbook': u'http://api.cbix.ca/v1/orderbook', u'news': u'http://api.cbix.ca/v1/news', u'volatility': u'http://api.cbix.ca/v1/volatility', u'history': u'http://api.cbix.ca/v1/history'}, u'success': True, u'source_link': u'https://www.cbix.ca'}
```

`r` is an object of type `requests.Response`. Note that displaying `r` shows us that the status code was 200. `r.text` gives us the text of the response as a string. `r.json()` unpacks the JSON into a Python dict. If the text of the response isn't in JSON format, you would get an error here.

Now, each time we run the loop, the response text consists only of a single-character - the digit from 1 to 6. Each time we add the character to the list `l` using the method `l.append()`. At the end, `l` should look like this:

```
>>> l
[u'5', u'5', u'1', u'1', u'2']
```

This is a list of strings, not numbers. The `u` before the quotes means that the strings are Unicode, although this doesn't matter much to us at the moment.

The last thing we do is print out the list of dice values. We use `join`, which is a member method of the string class. Given a string `s`, `s.join(l)`, where l is a list (or something similar to a list), returns the string made by joining all the elements of `l` with one copy of `s` between each pair.

```
>>> "_".join(['a', 'b', 'c'])
'a_b_c'
>>> "foo".join(['hello', 'world', '!'])
'hellofooworldfoo!'
>>> "".join(['hello', 'world', '!'])
'helloworld!'
>>> " ".join(l)
u'5 5 1 1 2'
```

`print` of course prints out the resulting string. We don't need print in the REPL, where the last expression automatically gets printed out, but we do in a script.

