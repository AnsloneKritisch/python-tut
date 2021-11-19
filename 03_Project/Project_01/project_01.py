# Create a dictonary and take input from the user and return the meaning of the word from the dictonary
# Maximum Four words

a = { "fish" : "It is an aquatic animal" ,
      "cold drink" : "It is a kind of drink made of soda" ,
      "piano" : "Instrument used for playing music" ,
      "bat" : "It is a kind of wooden instrument used wihile playing game name cricket"}

b = input(" Enter the word : ")
c  = b.lower()

print(" The meaning of the word",b,"is",a[c])
