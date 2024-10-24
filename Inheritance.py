# Inheritance

 # Its one class accessing another class called inheritence
# Its type
# Single Inheritance:
 # one child class accessing one parent class called Single Inheritance

class parent():
    def Pa_fun(self):
        print("parent Function")
class child(parent):                            # inheritance had created
    def ch_fun(self):
        print("child function")
ch=child()
ch.Pa_fun()

# Multiple Inheritance: 
 # one child class accessing two or more parent class called Multiple Inheritance

class parent1():
    def Pa1_fun(self):
        print("parent 1 Function")
class parent2():
    def Pa2_fun(self):
        print("parent 2 Function")
class child(parent1,parent2):                            # inheritance had created
    def ch_fun(self):
        print("child function")
ch=child()
ch.Pa1_fun()
ch.Pa2_fun()


# Multilevel Inheritance :
    # one child class accessing one parent class and that parent class depand on another parent class called Multi leval Inheritance


class sr_parent():
    def Pa1_fun(self):
        print("SR parent Function")
class JR_parent(sr_parent):                        # inheritance had created c1 to c2
    def Pa2_fun(self):
        print("JR parent Function")
class child(JR_parent):                            # inheritance had created c2 to c3
    def ch_fun(self):
        print("child function")
ch=child()
jr=JR_parent()
jr.Pa1_fun()                                        # class 2 acc calss 1 fun
ch.Pa2_fun()                                        # class 3 acc calss 2 fun
ch.Pa1_fun()                                        # class 3 acc calss 1 fun


# Hierarchical Inheritance:
    # two or more child class accessing one parent class called Hierarchical Inheritance

class parent():
    def Pa_fun(self):
        print("parent Function")
class child(parent):                            # inheritance had created
    pass
class child1(parent):                            # inheritance had created
    pass
class child2(parent):                            # inheritance had created
    pass
ch=child()
ch1=child1()
ch2=child2()
ch.Pa_fun()
ch1.Pa_fun()
ch2.Pa_fun()


# Hybrid Inheritance:
    # Its a combination of above type of mixed inheritance


class parent1():
    def Pa1_fun(self):
        print("parent 1 Function")
class parent2():
    def Pa2_fun(self):
        print("parent 2 Function")
class child1(parent1,parent2):                            # inheritance had created
    def ch_fun(self):
        print("child function")
class child2(parent2):
    pass

ch=child1()
ch.Pa1_fun()
ch.Pa2_fun()











