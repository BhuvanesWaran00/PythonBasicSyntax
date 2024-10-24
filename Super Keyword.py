# Super Keyword 
    # used to call a method from a parent or superclass within a subclass


class parent1():
    def __init__(self):
        print("parent 1 pre defind Function")
    def Pa1_fun(self):
        print("parent 1 Function")
class parent2():
    def __init__(self):
        print("parent 2 pre defind Function")    
    def Pa2_fun(self):
        super().__init__()
        print("parent 2 Function")
class child(parent2,parent1):                            # inheritance had created
    def ch_fun(self):
        print("child function")
ch=child()
ch.Pa1_fun()
ch.Pa2_fun()
