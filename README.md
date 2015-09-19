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

If you don't get an error message, you are good to go (type `exit()` to leave the Python shell). If you do, look at the troubleshooting section.

Useful Resources
----------------

 * The Requests HTTP library: http://docs.python-requests.org/en/latest/
 * The 'Roll the Dice' API: http://rollthedice.setgetgo.com/
 * The ProgrammableWeb directory of public APIs, where the above was found: http://www.programmableweb.com/apis/directory	

Troubleshooting
---------------

### I don't have Python on my machine!
Install it. Use Google.

### I don't have the virtualenv command!
Try doing `pip install virtualenv`. If you have pip installed properly, this should work. If you don't have pip, or it isn't installed correctly, you will need to figure this out anyway so that you can install the other packages needed. See the item below.

You can work without virtualenv, try just doing:

```
pip install -r requirements.txt
```

This will install the requirements globally. There could be conflicts with other packages you have installed! But we are not expecting to have any outlandish requirements, so you should probably be ok.

Virtualenv seemed like a huge hack and a solution looking for a problem the first time I used it. However, if you are ever going to work on more than one different Python project, and especially if you want to download someone else's code, it is actually incredible useful. It seems like everyone has Python on their computer already - but they can't use it because it is an old version, with a bunch of weird libraries they installed as a dependency for something else, and without a working version of pip. As soon as you get virtualenv working, you have solved these problems.

### I don't have the pip command!
You will need it. Recent versions of Python come with it included, so maybe you should just re-install Python or update it if it was installed with a package manager (eg brew or apt-get). If you think you have a recent version of Python, it could be that you have pip, but it isn't in your PATH, especially if you are on Windows. 

You can install pip by itself if you already have Python which doesn't include it, and for some reason you don't want to upgrade. On Ubuntu you would do `sudo apt-get install python-pip`. On Windows you would .. on Windows you should just install the newest version of Python. It will definitely, definitely, be easier.
