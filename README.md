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

If virtualenv doesn't work for you, try just doing the third line:

```
pip install -r requirements.txt
```

This will install the requirements globally. There could be conflicts with other packages you have installed! But we are not expecting to have any outlandish requirements, so you should probably be ok.

