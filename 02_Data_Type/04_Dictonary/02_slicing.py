# We can print the whole dictionay by using the print function.
a = {"a":1 , "b": 2}
print(a)

# If we want to print the key value of a dictonay.
d2 = {"Rohan" : "fish" ,"Raj" : "Cold Drink"}
print(d2["Raj"])

# If we want to add new item and key then.
d2 = {"Rohan" : "fish" ,"Raj" : "Cold Drink"} 
d2["Rajan"] =  "Paneer"
print(d2)

# If we want to delete any item and key. 
d2 = {'Rohan': 'fish', 'Raj': 'Cold Drink', 'Rajan': 'Paneer'}
del d2["Rajan"]
print(d2)

# to know all the keys present in the dictonary.
print(d2.keys())

# to know all the items and keys present in the dictonary.
print(d2.items())

