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
print(a.isalpha()) 

# string.endswith("character") -> helps to find out that the string ends with the given character or not.
a = "abcd"
print(a.endswith("d"))

# string.count("character") -> helps to count number of the same charcters are present at the string.
a = "aaaaaaaaaaaabcd"
print(a.count("a"))

# string.capitalize() -> helps to convert the first letter of the string into capital.
a = "anshu"
print(a.capitalize()) 

# string.find("character") -> helps to check wheather is character is present or not and give its location.
a = "anshu"
print(a.find("h")) 

# string.lower() -> convert the all letters of the string into small.
a = "ANSHU"
print(a.lower()) 

# string.upper() -> convert the all letters of the string into capital.
a = "anshu"
print(a.upper()) 


# string.replace("word_string","Word_you_want_to_add") -> helps to replace word.
a = " He am good."
print(a.replace("am","is")) 