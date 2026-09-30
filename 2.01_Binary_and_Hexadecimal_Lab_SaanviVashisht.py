#Part 4(A): Write Your Name

name = "Saanvi"
for char in name:
    asciiChar = ord(char)
    binaryChar = bin(asciiChar)
    print("{0} {1} {2}".format(char,binaryChar,asciiChar))
    

#Part 4 (B):

userInput=input("What letter would you like the binary and ASCII code for? ")
asciiChar=ord(userInput)
binaryChar=bin(asciiChar)
print("The binary representation is: {0}\nThe ASCII representation is: {1}".format(binaryChar,asciiChar))


#Part 5: Unicode:

print("\U0001F440","\U0001F394","\U00002615","\U0001F634","and","\U0001F32F")
