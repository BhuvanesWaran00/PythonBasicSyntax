# If Eles Statments

a = input("Enter value True or false: ")
if a == "True" or a == "true" :                 # if works for st 1 is true
    b = input("you want to go nested if yes or no: ")
    if b == "yes"or"Yes" or 1 or "s" :          # nested if consider as if statment inside of another if statment
        print("now your nested if")                 
elif a =="False" or a =="false" :               # elif works for next statment of if is true
    print("you enter value is False")           # we use N number of elif
else:                                           # else use for all statmentes are false
    print("you enter value is wrong") 

