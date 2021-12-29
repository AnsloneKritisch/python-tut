# Make a faulty calculator where every calculation will be ok except
# 45*3 = 555 , 56+9 = 77 , 56/6 = 4 

print("Welcome to Anshu Calculator \n")
print("What do you want to calculate it ? ")
print(" Press >> 1 -> Addition  2 -> Substract  3 -> Muntiply  4 -> Division  ")

a = int(input("Enter the number : "))

if( a == 1 ) :
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    if (b == 56 and c == 9 ) :
        print("The sum of" , b , "+" , c , "=" , "77")
    else :
        print("The sum of" , b , "+" , c , "=" , b+c )

elif( a == 2 ) :
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    if (b > c ) :
        print(" The Difference of " , b , "-" , c , "=" , b-c )
    else :
        print("The Difference of" , c , "-" , b , "=" , c-b )
        

elif( a == 3 ) :
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    if ((b == 45 and c == 3 ) or (b == 3 and c == 45 )) :
        print(" The Product of " , b , "X" , c , "=" , "555")
    else :
        print("The Product of" , b , "X" , c , "=" , b*c )
        
elif( a == 4 ) :
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    if (b == 56 and c == 6 ):
        print(" The Division of " , b , "%" , c , "=" , "4")
    else :
        print("The Division of" , b , "%" , c , "=" , b/c )
        
else :
    print("You choose wrong ")
    print(" Press >> 1 -> Addition \n 2 -> Substract \n  3 -> Muntiply \n 4 -> Division  ")