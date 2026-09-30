import random

global month
global distance_travelled
global food_intake
global available_food

total_distance = 2000
available_food = 500
month = 3
DAYS_IN_MONTH=[0,31,28,31,30,31,30,31,31,30,31,30,31]
SICK_COUNT = [0,2,2,2,2,2,2,2,2,2,2,2,2]
miles_min = 30
miles_max = 60
travel_days_min = 3
travel_days_max = 7
rest_days_min = 2
rest_days_max = 5
hunt_days_min = 2
hunt_days_max = 5
distance_travelled = 0
days = 1
health_level = 5
food_intake = 5

commands= ["travel","rest","hunt","status","help","quit"]

#Name: advanceDate()
#Purpose: The purpose of this function is to advance the number of days and in turn, the months.
#This function ensures the game goes on as time goes on.
#Input(s): none
#Return(s): month and days
def advanceDate():
  global days
  global month
  while(days >= DAYS_IN_MONTH[month]):
    days = days - DAYS_IN_MONTH[month]
    month += 1
  return month, days


#Name: travel()
#Purpose: The purpose of this function is to first: increase the distance travelles by a random amount (between 30 and 60)
#Second: This purpose increases the food intake in accordance to the days travelled (with each day being multiplied by 5)
#Third: This purpose ensures the available food changes according to the food intake
#Input(s): none
#Return(s): none
def travel():
  global distance_travelled
  global days
  global month
  global food_intake
  global available_food
  distance_travelled += random.randint(miles_min,miles_max)
  d = random.randint(travel_days_min, travel_days_max)
  food_intake += (5*d)
  available_food=available_food - food_intake
  days+=d
  month, days = advanceDate()
  if(random.random()<0.06):
    fallSick()


#Name: rest()
#Purpose: This function changes the health level is one level higher if the user chooses to rest
#It also advances the date randomly (between 2 and 5) and changes the food_intake in accordance
#to the number of days rested
#Input(s): none
#Return(s): none
def rest():
  global health_level
  global days
  global month
  global food_intake
  if(health_level<5):
    health_level += 1
  d = random.randint(rest_days_min,rest_days_max)
  food_intake += (food_intake*d)
  days+=d
  month, days = advanceDate()
  if(random.random()<0.06):
    fallSick()


#Name: hunt()
#Purpose: If the user choose to hunt, this function ensures the available_food increases by 100
#It also increases the days advanced (between 2 and 5) and increases the food intake in accordance
#to the days advanced
#Input(s): none
#Return(s): none
def hunt():
  global total_food
  global days
  global month
  global available_food
  global food_intake
  available_food+=100
  d = random.randint(hunt_days_min,hunt_days_max)
  food_intake += (5*d)
  days+=d
  month, days = advanceDate()
  if(random.random()<0.06):
    fallSick()


#Name: status()
#Purpose: This function returns the food_intake, available_food, health_level, distance_travelled, month, and days
#Input(s): none
#Return(s): food_intake, available_food, health_level, distance_travelled, month, and days
def status():
  return "Food Intake: "+ str(food_intake), "Available Food: "+str(available_food), "Health Level: "+str(health_level), "Distance Travelled: "+str(distance_travelled),"Month: "+str(month),  "Days: "+str(days)


#Name: help()
#Purpose: This function returns the commands of the game: ["travel","rest","hunt","status","help","quit"]
#Input(s): none
#Return(s): commands
def help():
  return commands


#Name: fallSick()
#Purpose: This function reduces the current health level by 1 and reduces SICK_COUNT[month] by 1
#which ensures the user falls sick randomly twice in one month
#Input(s): none
#Return(s): none
def fallSick():
  global health_level
  if(SICK_COUNT[month]>0):
      health_level = health_level-1
      SICK_COUNT[month] = SICK_COUNT[month]-1


#Name: canGameContinue
#Purpose: This function determines whether the user can continue the game or not. If the complete the whole journey
#i.e, distance_travelled >= total distance. If the food_intake is greather than available_food, then the user looses
#the game due to food shortage. If the user hasn't reached the destination before December 31st, then they loose the
#game. Lastly, if the health_level of the user is 0, then the user looses the game.
#Input(s): none
#Return(s): True or False
def canGameContinue():
  if distance_travelled >= total_distance:
    print("Congragulations you reached Oregon. You won the game!!")
    return False
  elif food_intake >= available_food:
    print("Sorry, no food available. You lost the game!!")
    return False
  elif month==12 and distance_travelled<total_distance:
      print("Sorry, you've exceeded the deadline of Dec 31st. You lost the game!!")
      return False
  elif health_level == 0:
    print("Sorry, you are feeling sick. You lost the game!!")
    return False
  else:
    return True

print("Welcome to The Oregon Trail Game! You will undergo an arduous journey from St. Louis, Missouri to Oregon City, Oregon. ")
print("Here are the commands: Good Luck!")
print(help())
while(canGameContinue()):
  user_input = input("Please enter the command: ").lower()
  if(user_input=="travel"):
    travel()
    print(status())
  elif(user_input=="hunt"):
    hunt()
    print(status())
  elif(user_input=="rest"):
    rest()
    print(status())
  elif(user_input=="status"):
    print(status())
  elif(user_input=="help"):
    print(help())
  elif(user_input=="quit"):
    break
  else:
    print("Please enter a valid command")