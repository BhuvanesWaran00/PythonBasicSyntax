"""
    The term Recursion can be defined as the process of defining something in terms of itself.
    In simple words, it is a process in which a function calls itself directly or indirectly. 

 """


# Print a factorial of numbers
def fact(num):
    if (num == 1):
        return num
    else:
        return num*fact(num-1)

num=int(input())

if num < 0 :
    print("Enter Valid input")
elif num == 0: 
    print("factorial of 0 is 1")
else:
    x = fact(num)
    print(x)
