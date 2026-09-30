
#Name: user_info
#Purpose: asks the user for their first name and the month they were born, stores this information in a list.
#Input: none
#Return: list of information

def user_info():
    firstname=input("What is your first name?")
    birthmonth=input("What is your birth month?")
    lista=[firstname,birthmonth]
    return lista


#name: city_list()
#purpose: This function continually asks the user for a list of cities. Each city is appended to a list. The user must give at least one city.
#purpose: when the user types 'done', the function returns the list of cities
#Input: no input
#Return: the list of cities
def city_list():
    cities=[]
    while True:
        addcity=str(input('type in a city:'))
        if addcity=='done':
            print(cities)
            break
        else:
            cities.append(addcity)


###Name: random_element
###Purpose: Takes in a list and picks a random element from the list, returning the randomly selected element
###Input: list
###Returns: Random element

import random
def random_element(list):
    element = list[random.randint(0, len(list)-1)]
    return element


#Name:length_converter
#Purpose: takes in a string and returns number of characters in the string
#Input: string
#Returns: the number of characters in the string

def length_converter(userString):
    return len(userString)


#name=lucky_number
#purpose:magical math to return a number - the function takes two number inputs. The first input is the length of the birth month. The second input is the length of the randomly selected city name.
#purpose: the function also picks a random number between 1-50, then performs some magical math (which the user decides), on the three numbers to return the lucky number. 
#inputs: 2 integers
#return=integer


def lucky_number(name,city):
    user=len(name)
    place=len(city)
    number=random.randint(1,50)
    lucky=user+place+number
    return lucky


###Name: Final
###Purpose: This function takes in three inputs: the user name, the selected city, and the lucky number. It then greets user and tells them which city to play powerball in with the lucky number.
###Inputs: Name, City, Number
#Output: None

def final(name, city, number):
    print('''Hello {}! You should play power ball in {}, using the number {}'''.format(name,city,number))


