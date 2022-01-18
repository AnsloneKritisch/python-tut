# WAP to make a guess game 
# With some chances 

print(" Total 5 Chances will be given ")
print(" All The Best ")
a = 1
num = 56
while (a <= 5) :
    
    b = int (input(" Enter the number : "))
    if (b==num) :
        print("\n Yes you got the right choice ")
        print("\n You are too lucky ")
        print("\n : )  ")
        break

    elif(b > num) :
        print("\n Oops ! You choose a larger number ")
        print("\n You have " , 5-a , " chances left \n ")
        a = a + 1
        continue

    elif(b < num) :
        print("\n Oops ! You choose a smaller number ")
        print("\n You have " , 5-a , " chances left \n ")
        a = a + 1
        continue

    else :
        print(" Game Over \n")
        print(" You are unlucky today ")