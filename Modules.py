# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

# use math module

import math                      # deffine Math module

print(int(math.pow(2,3)))        # Use power options in math module

x = dir(math)                    # dir() using for to find what are the operations we can do using this module

for i in x:
    print(i)





# Module alias

import math as m                 # use as keyword for alias name

print(int(m.pow(2,3)))






# Import From Module

# You can choose to import only parts from a module, by using the from keyword.

from math import pi

print(pi)

try:

    print(int(math.pow(2,3)))
except:
    print("NameError: name 'math' is not defined. Did you forget to import 'math'?")






# User Defined module

# Data.py


list = [{'name': 'InNCG', 'age': 54}, {'name': 'IWEbW', 'age': 75}, {'name': 'YUdYL', 'age': 70}, {'name': 'HNqaW', 'age': 38}, {'name': 'RVQxu', 'age': 41}, {'name': 'equgm', 'age': 43}, {'name': 'wKnBf', 'age': 71}, {'name': 'VRlqX', 'age': 73}, {'name': 'nVyUI', 'age': 41}, {'name': 'cBmYy', 'age': 51}]


# main.py

from data import list

for i in list:
    print(i)




