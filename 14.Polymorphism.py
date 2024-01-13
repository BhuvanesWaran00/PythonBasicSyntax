# Polymorphism
    # The word polymorphism means having many forms
    # polymorphism means the same function name (but different signatures) being used for different types. 
    # The key difference is the data types and number of arguments used in function.
# EX 1


def add(a,b,c=0):               # in this method c have value 0
    return a+b+c
print(add(5,4))                 # in this calling method this function add only 2 numbers
print(add(7,7,8))               # But in this calling method this function add 3 numbers c had overraid value

# EX 2

 
# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))