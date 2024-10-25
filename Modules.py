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

for i in list:
    print(i)


# main.py

import data


# __name__


import data

print(__name__)
print(data.display.__name__)

# output
{1: {'name': 'InNCG', 'age': 54}, 2: {'name': 'IWEbW', 'age': 75}, 3: {'name': 'YUdYL', 'age': 70}, 4: {'name': 'HNqaW', 'age': 38}, 5: {'name': 'RVQxu', 'age': 41}, 6: {'name': 'equgm', 'age': 43}, 7: {'name': 'wKnBf', 'age': 71}, 8: {'name': 'VRlqX', 'age': 73}, 9: {'name': 'nVyUI', 'age': 41}, 10: {'name': 'cBmYy', 'age': 51}}
__main__
display

# data.py

from print import display

data_list = {
    1:{'name': 'InNCG', 'age': 54},
    2:{'name': 'IWEbW', 'age': 75},
    3:{'name': 'YUdYL', 'age': 70},
    4:{'name': 'HNqaW', 'age': 38},
    5:{'name': 'RVQxu', 'age': 41},
    6:{'name': 'equgm', 'age': 43},
    7:{'name': 'wKnBf', 'age': 71},
    8:{'name': 'VRlqX', 'age': 73},
    9:{'name': 'nVyUI', 'age': 41},
    10:{'name': 'cBmYy', 'age': 51}
}

display(data_list)

# print.py

def display(x):

    for i in x:
        name =x[i]['name']
        age =x[i]['age']
        msg=f"name: {name} and age: {age}"
        print(msg)    


if __name__ == "__main__":
    display(x)






