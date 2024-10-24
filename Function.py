# Function

# functin without parameters
def cal():                   # define Function
    a=1
    b=2
    print(a+b)                  
cal()                        # calling function

# functin with parameters
# ex 1
def add(a,b):                   # define Function
    print(a+b)                  
add(5,8)                        # calling function

# ex 2
def sub(a,b):
    print(a-b)
x=1
y=8
sub(x,y)



# Pass multiple types if args

# pass single value via one argument
def num(numbers):
    print(numbers)

num(1)

# Pass multiple values via one argument
def num(numbers): 
    print(numbers)

try:
    num(1,2,3,4)
except:
    print("can't pass multiple values")

# pass multiple values via one argument using *args

def num(*numbers):
    print(numbers)

num(1,2,3,4)

# pass key value via one argument using **kwargs
def num(**numbers):
    print(numbers)

num(name ="zeo" , age =24)

