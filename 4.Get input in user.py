# Get input in user

a = input("enter your value:")
print("given value: ",a,"and its type: ",type(a))

# input always take all string so now we use casting
# casting Is nothing change datatype one to another


try:
    a = int(a)
    print("given value: ",a,"and after casting its type: ",type(a))
except Exception as e:
    print ("given value is non convertable to int :",e)