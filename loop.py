# For loop

for vg in [1,2,3,4,5] : 
    print(vg)
else:
    print("it\'s over")        # print the statement after loop over


# Range

for i in range(5) :        #range value is 0 to i-1 by default 
    print(i)
for n in range(10,15):     # now range value is 10 to 15-1 by default 
    print(n)   

for n in range(10,101,5):     # now range value is 10 to 100 and increase +5 ex 10,15,20 by default 
    print(n)    

# nested for

for i in range(0,10):
    for j in range(i):
        print ("*",end="")
    print("")

# while loop

# ex 1 : pascal triangle.
j =0
for i in range(0,10):
    while (j<=i):
        print ("*",end="")
        j += 1
    print("")
    j=0

# ex2 : print 10 series upto 200
i=0
while(i<200):
    i+=10
    print(i)

# ex3: factorial
num = int(input("Number: "))
temp =1
while(num>0):
    temp = num*temp
    num-=1
print (num,"! = ",temp)
