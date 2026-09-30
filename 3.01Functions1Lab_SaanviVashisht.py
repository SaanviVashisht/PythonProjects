
# Name: add_num
# Purpose: add_num takes in two numbers, adds them, then prints their sum
# Input: two inputs - x and y
# Returns: sum of x and y
def add_num(x,y):
  return x+y
add_num(3,8)




# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str)
# Returns: none
def birthday_song(name):
  print ("Happy Birthday to you! Happy Birthday to you! Happy Birthday dear", name,"Happy Birthday to you!")
birthday_song('Saanvi')




# Name: eightball_response()
# Purpose: to simulate a magic eight-ball by selecting random responses to user questions.
# Input: none
# Return: string

import random
def eightball_response():
  while 1==1:

    question=input("Ask the magic eight ball a yes or no question. Type 'no' if you wish for the program to stop running.")
    possibleResponses=['Outlook is good','Ask again later','Yes','No','Most likey no','Most likey yes','Maybe','Outlook is not good']
    random_element = random.choice(possibleResponses)

    if question.lower() =="no":
      break
    else:
      print(random_element)

eightball_response()