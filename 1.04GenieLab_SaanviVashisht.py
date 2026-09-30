#Part I: Genie Program 1

print("I am a genie. You have three wishes")
wish1= input("What would you like to wish for? ")
wish2= input("What would you like to wish for? ")
wish3= input("What would you like to wish for? ")
print("Your wishes are",wish1,wish2,"and",wish3)

#Part II: Genie Program 2

a="What would you like to wish for? "
print("I am a genie. You have three wishes")
wish1= input(a)
wish2= input(a)
wish3= input(a)
temp = wish3
wish3=wish1
wish1=wish2
wish2=temp

print("Your wishes are",wish1,wish2,"and",wish3)

#Challenge

a=2
b=3
a=a+b
b=a-b
a=a-b

