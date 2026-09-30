# Part 2: Game Show:

prize1 = 'You win a Macbook!'
prize2 = 'You win $100,000!'
prize3 = 'You win Airpods!'
prize4 = 'You win a free ticket to DisneyLand!'
prize5 = 'You win a free giftcard of $20 to Starbucks!'
prize6 = 'You win a free Duo(of Duolingo) plushie! And an exclusive day out with Duo!'

print('Welcome to the game show. Pick a door number 1-6 and win a prize.')
user=int(input("Which door do you pick(1-6)? "))

if user==1:
    print(prize1)
elif user==2:
    print(prize2)
elif user==3:
    print(prize3)
elif user==4:
    print(prize4)
elif user==5:
    print(prize5)
elif user==6:
    print(prize6)
else:
    print("You didn't pick a valid door. No prize for you.")


# Part 3: Triangle Tester:

x=int(input('Enter a value: '))
y=int(input('Enter a value: '))
z=int(input('Enter a value: '))

if x+y>z and x+z>y and y+z>x:
    if x == y and x == z and y==z:
        print('Valid traingle! The perimeter is',x+y+z,'and this is an Equilateral triangle.')
    elif ((x**2+y**2==z**2 or x**2+z**2==y**2 or y**2+z**2==x**2) and x!=y!=z):
        print('Valid traingle! The perimeter is',x+y+z,'and this is a Right Scalene triangle.')
    elif ((x**2+y**2==z**2 or x**2+z**2==y**2 or y**2+z**2==x**2) and (x==y or y==x or z==x)):
        print('Valid traingle! The perimeter is',x+y+z,'and this a Right Isosceles triangle.')
    elif (x==y or y==x or z==x):
        print('Valid triangle! The perimeter is',x+y+z,'and this is an Isosceles triangle.')
else:
    print('Invalid triangle!')
