Yahtzee
=======

Setup
-----

To get started, do:

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

These three steps:
 * Setup a 'virtualenv' in a directory called 'venv'. This is a Python tool which allows you to install packages and run your code in an isolated context. 
 * Activate the virtualenv. After you do this, everytime you run 'pip', you will install Python packages only into the virtual environment. Every time you run 'python', a special version of python will run, which sees only the packages installed in the virtual environment.
 * Install all the packages in the file called 'requirements.txt'.

To test that everything is working, type `python` on the command line, and then in the python terminal, do 

```
Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
```

If you don't get an error message, you are good to go. If you do, look at the troubleshooting section.

Useful Resources
----------------

 * The Requests HTTP library: http://docs.python-requests.org/en/latest/
 * The 'Roll the Dice' API: http://rollthedice.setgetgo.com/
 * The ProgrammableWeb directory of public APIs, where the above was found: http://www.programmableweb.com/apis/directory	


