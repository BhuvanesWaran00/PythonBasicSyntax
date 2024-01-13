# Encapsulation
# Encapsulation is used to restrict access to methods and variables.



class Base:
	def __init__(self):

		# Protected member
		self.__a = "hai"                                        # --> now we use access modyfier (__) its restrict access variable
obj2 = Base()
print("Accessing protected member of obj1: ", obj2.__a)



# we use (__) in front of variable its called private var

# we use (_) in front of variable its called producted var

# Exception Handling
# it's mostly use under runtime error

# ex

try:
    a = int(input())
    b = int(input())
    print(a+b)
except ValueError as a:
    print("enter numbers only")

except Exception as a:
    print(a,"enter numbers only")

finally:
    print("done")