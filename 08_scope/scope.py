x = 25 
def fun():
    x =50
    return x
# when we indivisually check x we get the value as assigned
print(x)
print(fun())

#  after we use the function then check the value of x the funtion is overwritten

fun()
print(x)

# local variable
lambda x: x**2

# Enclosing function global variable

name = " this is a global variable"

def greet():
    # if we comment out the name local variable then it will take name written above and print it
    # just comment the name and check the output 
    name = "anshu"

    def hello():
        print("hello", name)
        # name here is local  variable if it is removed it will take global varaible name

    hello()

greet()



