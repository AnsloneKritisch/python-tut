# Make a faulty calculator where every calculation will be ok except
# 45*3 = 555 , 56+9 = 77 , 56/6 = 4 

print("Welcome to Anshu Calculator \n")
print("What do you want to calculate it ? ")
print(" Press >> 1 -> Addition \t 2 -> Substract \t 3 -> Muntiply \t 4 -> Division")

a = int(input("Enter the number : "))

if( a == 1 ) :
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    if (b == 56 and c == 9 ) :
        print("The sum of" , b , "+" , c , "=" , "77")
    else :
        print("The sum of" , b , "+" , c , "=" , b+c )

else :
    print("You choose wrong ")
