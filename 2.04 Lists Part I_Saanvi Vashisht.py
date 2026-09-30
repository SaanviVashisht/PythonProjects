#Same Element?
list1=[2,4,6]
list2=[1,3,6]

if list1[0] == list2[0] or list1[-1]==list2[-1]:
    print('True')
else:
    print('False')



#Do the Shuffle
originalList=[23,41,67]

result=[]

l = len(originalList)

if l==3:
    for i in range(l):
        #result.append(originalList[(i+1)%l])
        print(i)
        print(l)
        print(i+1)
        print((i+1)%l)
        print(originalList[(i+1)%l])
else:
    print("Length of the list is not equal to 3")

print(result)




#Two Sum
list1=[2,4,6,8,0]
print(list1[0]+list1[1])




#Sheep
originalList=[23,41,67]

l = len(originalList)
largest = originalList[0]

for i in (1,l-1):

 if(originalList[i]>largest):

   largest = originalList[i]

result = [largest for num in originalList]

print(result)



#Game Show
prize1 = 'You win a Macbook!'
prize2 = 'You win $100,000!'
prize3 = 'You win Airpods!'
prize4 = 'You win a free ticket to DisneyLand!'
prize5 = 'You win a free giftcard to Starbucks!'
prize6 = 'You win a free giftcard to McDonalds!'
prize7= 'You win a free trip to Bali!'
prize8='You win a Chromebook!'
prize9='You win a TV!'
prize10='You win a back-to-school stationary kit!'
list1=[prize1,prize2,prize3,prize4,prize5,prize6,prize7,prize8,prize9,prize10]
user=int(input('Please enter a number ranging from 1-10: '))

if user==1:
    print(list1[0])
elif user==2:
    print(list1[1])
elif user==3:
    print(list1[2])
elif user==4:
    print(list1[3])
elif user==5:
    print(list1[4])
elif user==6:
    print(list1[5])
elif user==7:
    print(list1[6])
elif user==8:
    print(list1[7])
elif user==9:
    print(list1[8])
elif user==10:
    print(list1[9])
else:
    print("Your number is out of range.")
