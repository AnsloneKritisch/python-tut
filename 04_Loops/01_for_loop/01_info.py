# For - Loop  
# This is basic format of loop

a = int(input("Enter number of Loops : "))
for i in range (1 , a+1 ) :
    print(i)

# We can also use loop for printing all elements of list .

b = ["a","b","c"]
for i in b :
    print(i)

# We can also use loop for printing all the items present in dictonary.

c = {"Rohan" : "Maza" ,"Raj" : "Frooti" , "Rajan" : "Pepsi"}
for i in c.items() :
    print(i)