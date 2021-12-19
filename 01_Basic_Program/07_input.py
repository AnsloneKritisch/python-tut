# To take input from the user we have to use input function
# After taking the input we need to store it somewhere , so we will store it in variable

#Let "x" be a variable

x = input("Enter What you want to store : ")

print(x) # we will print and check that what have been stored

#If you want to a specific type of data then you can mention it or else it will store all your data as string 

x = int(input("Enter an integer :"))
print(x)
print(type(x))