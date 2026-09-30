from Functions3LabPart2_Saanvi import find_longer_list, find_shorter_list, find_common_elements


#Name: getPersistence()
#Purpose: This function checks what the multiplicative persistence of a number is
#Input(s): n(int)
#Return(s): One of two: if a number does not have a multiplicative persistence then the program returns 0
#Otherwise, the program returns the value of the multiplicative persistence of the number


def getPersistence(n):
    if not isValid(n):
       return 0

    multiplier = 1

    while(n > 0):
        multiplier = getRemainder(n) * multiplier
        n = getQuotient(n)
    return getPersistence(multiplier) + 1
getPersistence()

#Name: isValid()
#Purpose: This function checks if a number has a multiplicative persistence of either 0 or greater than 0
#Input(s): n(int)
#Return(s): True or False

def isValid(n):
  if n<10:
    return False
  else:
    return True
isValid()

#Name: getRemainder()
#Purpose: This function checks what the remainder of a number is when it's divided by 10 using modulus
#Input: n(int)
#Return(s): The value of the remainder


def getRemainder(n):
  return (n % 10)


getRemainder()

#Name: getQuotient()
#Purpose: This function checks what the quotient of a number is when it's divided by 10 using integer division
#Input(s): n(int)
#Return(s): The value of the quotient (rounded to the nearest integer)

def getQuotient(n):
   return n // 10

getQuotient()

#Name: getSmallestNumberWithLargestMultiplicativePersistence()
#Purpose: This function checks for (from a range of numbers) the value of the smallest number with the largest multiplicative persistence and returns it
#Input(s): first and last(int)
#Return(s): The value of the smallest number with the largest multiplicative persistence

def getSmallestNumberWithLargestMultiplicativePersistence(first, last):
    maxPersistence = 0
    smallestNumber = first

    for i in range(first, last + 1):
        persistence = getPersistence(i)
        if persistence > maxPersistence:
            maxPersistence = persistence
            smallestNumber = i

    return smallestNumber, maxPersistence

first = 222
last = 256

number, persistence = getSmallestNumberWithLargestMultiplicativePersistence(first, last)

print(f"The smallest number with the biggest persistence in the range {first}-{last} is {number} with persistence {persistence}.")