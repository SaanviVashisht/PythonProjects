def getSmallestNumber(numbers):
    smallest = numbers[0]
    for x in numbers:
        if(x<=smallest):
            smallest=x
    return smallest

v1=int(input("Please enter a number: "))

v2=int(input("Please enter a number: "))

v3=int(input("Please enter a number: "))

numbers=v1,v2,v3
number=getSmallestNumber(numbers)
print(number)