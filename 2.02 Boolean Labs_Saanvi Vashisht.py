#Part II: Can I be President?

#age=int(input("How old are you? "))
#print("You are old enough to be president: ",age>35)

#res=int(input("For how many years have you lived in the US? "))
#print("You have been a resident for at least 14 years: ",res>=14)

#born=input("Are you a natural born citizen of the US? Type 'yes' or 'no': ")
#print("You are a natural born citizen: ",born=='yes')

#print("You can be president: ",age>35 and res>=14 and born=='yes')



#Part III: Can I ride the roller coaster?

print("Give me your height by giving total feet and then on the next prompt total inches:")
height=int(input("How many feet tall are you? "))
height2=int(input("How many additional inches? "))
print("You are tall enough to ride the roller coaster: ",height>=4)

age=int(input("How old are you? "))
print("You are tall enough to ride the roller coaster regardless of your height: ",age>18)

quarters = int(input("How many quarters do you have? "))
print("You have enough money to ride without a pass: ",quarters>=4)

riderPass=input("Do you have a Frequent Rider Pass? Type 'yes' or 'no': ")
print("You only need two quarters to ride: ",riderPass=='yes')

print("You can ride the roller coaster: ",(height>=4 or age>18) and (quarters>=4 or riderPass=='yes' and quarters>=2))
