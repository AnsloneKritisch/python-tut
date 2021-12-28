# elif is same as if command 
# But we can't write if command more than once but we can write elif command as many times we want

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

if a>b :
    print(a,"is greater than ",b)

elif a==b :
    print(a,"is equal to",b)

else :
    print(b,"is greater than ",a)