# OOPs  -->  Object-oriented programming

# Class and Object

# ex1
class data:                                     # define class
    name=""
    age= 0
    def print(self,name,age):                   # self is denoted by object
        print("name:",name,"age:",age)
a=data()                                        # create object
a.name = "lee"                                  # assigning value for veriable using object
a.age = 2
a.print(a.name,a.age)                           # Call functin using object
b=data()                                        
b.name = "bhuvi"                                  
b.age = 23
b.print(b.name,b.age)

# ex2
class data: 
    def __init__(self) -> None:                 # __init__ is constructor its biult in function in python and no need call this function
        self.name=input("enter name:")
        self.age= int(input("enter age:"))
    def print(self):
        print("name:",self.name,"age:",self.age)
a=data()                                                              
b=data()                                      
a.print()  
b.print()


# class veriable type
# Instance Variables 
#this type of ver are use keyword "self" it reffers Object
# Ex 1


class num:
    def __init__(self,num) -> None:                # self --> keyword it refers object one & two
        self.num=num
    def display(self):
        print (self.num)
    
one=num(1)
two=num(2)
one.display()
two.display()



# Class Variables
# this type of ver are use in dirctly in class
# EX


class num:
    printst = "number:"                            # define a class variable 1
    end = ","                                      # define a class variable 2
    def __init__(self,num) -> None:                # self --> keyword it refers object one & two
        self.num=num
    def display(self):
        print (self.printst,self.num,self.end)
num.end = "."                                       # change a value of var 2 (, to .)
one=num(1)
two=num(2)
one.display()
two.display()


# diffrent type of methods in class

# Instance Method 
# this type of method pass var useing keyword "self" it reffers Object
# Ex


class num:
    def __init__(self,num):
        self.num=num
    def display(self):
        print (self.num)
    
one=num(1)
two=num(2)
one.display()
two.display()



# Class Method
# this type of method dirctly using in class
# mostly we not use this method
# EX



class clss:       
    def disply(ACD):                                # define class method using arg
        print("Its class method 1")
    @classmethod                                    # define class method using decorators
    def dis(l1):
        print("Its class method 2")
clss.disply(clss)                                   # call class method using arg
clss.dis()                                          # call class method using decorators


# static Method
# this type of method we not use self keyword and not pass any arg
# EX

class clss: 
    @staticmethod                                
    def dis():
        print("Its static method")                        
clss.dis()  