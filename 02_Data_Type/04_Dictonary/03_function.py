
# Dictionay is a key value pair
#case sensetive
#KEY ARE IMMUTABLE

d1 = {}
print(type(d1))

a = {"a":1 , "b": 2}
print(a)

d2 = {"Rohan" : "fish" ,"Raj" : "Cold Drink"}
print(d2["Raj"])
print(d2)
#add 
d2["Rajan"] =  "Paneer"

d3 =  d2.copy()
del d2["Rajan"]
print(d2)

print(d3)

d2.update({"Raj" : "Coffee"})

print(d2.keys())

print(d2.items())

