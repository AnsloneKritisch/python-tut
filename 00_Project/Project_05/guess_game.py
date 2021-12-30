# WAP to make a guess game 
# With some chances 

print(" Total 5 Chances will be given ")
print(" All The Best ")
a = 1
num = 56
while (a <= 5) :
    b = int (input(" Enter the number : "))
    if (b==num) :
        print(" Yes you got the right choice ")
        break
    elif(b > num) :
        print(" Oops ! You choose a larger number ")
        a = a + 1
        continue
    elif(b < num) :
        print(" Oops ! You choose a smaller number ")
        a = a + 1
        continue
    else :
        print(" You are unlucky today ")