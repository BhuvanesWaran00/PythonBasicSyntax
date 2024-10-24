"""
    The term Recursion can be defined as the process of defining something in terms of itself.
    In simple words, it is a process in which a function calls itself directly or indirectly. 

 """


# print factorial of numbers
def fact(num):
    if (num == 1):
        return num
    else:
        return num*fact(num-1)

num=int(input())
x = fact(num)
print(x)
