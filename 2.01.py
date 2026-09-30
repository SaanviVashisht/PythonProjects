#Part 4: Write Your Name
#A

s1='S'
s2 = bin(ord("S"))
s3 = ord('S')
print(s1,' ',s2,' ',s3)

a1 = 'A'
a2 = bin(65)
a3 = ord('A')
print(a1,' ',a2,' ',a3)
print(a1,' ',a2,' ',a3)

n1 = 'N'
n2 = bin(78)
n3 = ord('N')
print(n1,' ',n2,' ',n3)

v1 = 'V'
v2 = bin(86)
v3 = ord('V')
print(v1,' ',v2,' ',v3)

i1 = 'I'
i2 = bin(86)
i3 = ord('I')
print(i1,' ',i2,' ',i3)

#Part 4
#B

user=input("What letter would you like the binary and ASCII code for? ")
a=ord(user)
b=bin(a)
print("The binary representation is:",b,"\nThe ASCII representation is:",a)

#Part 5: Unicode

print("\U0001F440","\U0001F394","\U00002615","\U0001F634","and","\U0001F32F")


#Part 6: XOR(aka exclusive or)

print(bin(4))
print(bin(6))
print(bin(4^6))

print(bin(16))
print(bin(4))
print(bin(16^4))

print(bin(20))
print(bin(4))
print(bin(20^4))