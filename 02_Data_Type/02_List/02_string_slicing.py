# String Slicing

# We can print the single element from the list.
vowel = [ "a","e","i","o","u"]
print(vowel)
print(vowel[2])

no = [1,2,3,4,5]
print(no)
print(no[3])

no = [2,6,9,7,5,8]
# The third bracket and the semicolumn both determines the range of the elements that must be printed from the list.
print(no[0:5])
# If we don't give any range then the range has been set by default full line .
print(no[:])
# If we want to skip any element then we have set it by adding semicolon and input no of character you want to skip .
print(no[::2])