# A variable is only available from inside the region it is created. This is called scope.

# Local Scope

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

  def myfunc():
    x = 300        # Local variable      
    print(x)

  myfunc()




# Global Scope

# A variable created outside of a function is global and can be used by anyone

    x = 300              # Global variable        

    def myfunc():
        print(x)         # 300

    myfunc()

    print(x)            # 300

# If you operate with the same variable name inside and outside of a function,
# Python will treat them as two separate variables


x = 300                # Global variable    

def myfunc():
  x = 200              # Local variable
  print(x)             # 200

myfunc()

print(x)               #300



#  Global Keyword, Nonlocal Keyword



apple_count = 20
def scope():
    batch=1
    global apple_count
    try:
        apple_count += 1
        print("apples: ",apple_count,"Batch: ",batch)
        
    except:
        print("we can\'t edit globle variable without globle keyword")

    def scope1():
        global apple_count
        
        nonlocal batch
        try:
            apple_count += 1
            batch += 1
            print("apples: ",apple_count,"Batch: ",batch)
        except:
            print("we can\'t edit globle variable also nested function without globle keyword and we can\'t edit local variable without nonlocal keyword")
    
    scope1()




scope()
