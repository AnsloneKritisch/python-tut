# Important functions of string :-

# The len() function help to calculate the length of the function.
a = "The World is big but below my Feet"
b = len(a)
print("The length of the string a is -> " , b)

# Alpha numeric means no space(both number and character). string.isalnum() -> helps to determine a alpha numric string
a = "abcd123"
print(a.isalnum()) 

# Alpha numeric means no space(only character). string.isalnum() -> helps to determine a alpha numric string
a = "abcd"
print(a.isalpha()) #alpha numeric means no space

print(a.endswith("d")) #alpha numeric means no space
"""print(a.count("o")) #count number of charcter
print(a.capitalize()) #count number of charcter
print(a.find("am")) #count number of charcter
print(a.lower()) #count number of charcter
print(a.upper()) #count number of charcter
print(a.replace("am","is")) #count number of charcter
print(a.replace("am","is")) #count number of charcter
"""