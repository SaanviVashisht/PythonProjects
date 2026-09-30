def getGreatestNumber(numbers):
    biggest = numbers[0]
    for x in numbers:
        if(x>=biggest):
            biggest=x
    return biggest

v1=int(input("Please enter a number: "))

v2=int(input("Please enter a number: "))

v3=int(input("Please enter a number: "))

numbers=v1,v2,v3
number=getGreatestNumber(numbers)
print(number)
