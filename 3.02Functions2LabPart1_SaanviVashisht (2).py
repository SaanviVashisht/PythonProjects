#Quadratic Equation Solver
#Name: Quad_solve
#Purpose: Find solutions to the equation ax^2+bx+c=0 and returns the result.
#Uses the quadratic formula:
#  x =  -b +/- sqrt(b^2-4ac)
#       --------------------
#               2a
#Input(s): a,b and c(floats)
#Return(s): Solutions to the quadratic rounded to the hundredths place

from math import sqrt
emptyList=[]
def quad_solve(a,b,c):
  dis=b**2-4*a*c
  if dis>=0:
    x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    x1= round(x1,2)
    x2 = (-b - sqrt(b**2-4*a*c))/(2*a)
    x2= round(x2,2)
    emptyList.append(x1)
    emptyList.append(x2)
    return emptyList
  elif dis<0:
    print("Not real.")
quad_solve(1,-4,4)





#Name: Temperature Convertor
#Purpose: Takes in two argumnets current_temp and choice(which is either the value 1 or 2) and performs conversion based on the choice of the user. It then returns the new temperature.
#Input(s): Takes in two argumnets current_temp and choice
#Return(s): New temperature

def temp_convertor(current_temp,choice):
  if choice == 1:
    C = (current_temp-32) * (5/9)
    return(C)
  elif choice==2:
    F = (9/5*current_temp)+32
    return(F)





#Name: Weather Forecast
#Purpose: This function takes in a temperature and an identifier(1, or 2) and prints the weather forecast
#Input(s): Two inputs: temperature and temp_type_num (the identifier)
#Return(s): None

import random
def weather_forecast(temperature, temp_type_num,printTemp=False):
  probOfRain = random.randint(1,5)
  if temp_type_num == 1:
    C = temp_convertor(temperature,1)
    if printTemp:
      print(C)
    if C<=4:
      print("Today's weather will be cold, need winter jacket!")
      if probOfRain == 1:
        print("With a 10% chance of rain.")
      elif probOfRain == 2:
        print("With a 20% chance of rain.")
      elif probOfRain == 3:
        print("With a 30% chance of rain.")
      else:
        print("With a 40% chance of rain.")
    elif 4<C<18.5:
      print("Today's weather will be cool, sweater weather!")
      if probOfRain == 1:
        print("With a 10% chance of rain.")
      elif probOfRain == 2:
        print("With a 20% chance of rain.")
      elif probOfRain == 3:
        print("With a 30% chance of rain.")
      else:
        print("With a 40% chance of rain.")
    elif 18.5<=C<27.8:
      print("Today's weather will be perfect, very comfortable.")
      if probOfRain == 1:
        print("With a 10% chance of rain.")
      elif probOfRain == 2:
        print("With a 20% chance of rain.")
      elif probOfRain == 3:
        print("With a 30% chance of rain.")
      else:
        print("With a 40% chance of rain.")
    elif 27.8<=C:
      print("Today's weather will be too hot, don't melt!")
      if probOfRain == 1:
        print("With a 10% chance of rain.")
      elif probOfRain == 2:
        print("With a 20% chance of rain.")
      elif probOfRain == 3:
        print("With a 30% chance of rain.")
      else:
        print("With a 40% chance of rain.")

  elif temp_type_num == 2:
    F = temp_convertor(temperature,2)
    if printTemp:
      print(F)
    if F<=40:
      print("Today's weather will be cold, need winter jacket!")
      if probOfRain == 1:
        print("With a 10% chance of rain.")
      elif probOfRain == 2:
        print("With a 20% chance of rain.")
      elif probOfRain == 3:
        print("With a 30% chance of rain.")
      else:
        print("With a 40% chance of rain.")
    elif 40<F<65:
      print("Today's weather will be cool, sweater weather!")
      if probOfRain == 1:
        print("With a 10% chance of rain.")
      elif probOfRain == 2:
        print("With a 20% chance of rain.")
      elif probOfRain == 3:
        print("With a 30% chance of rain.")
      else:
        print("With a 40% chance of rain.")
    elif 65<=F<82:
      print("Today's weather will be perfect, very comfortable.")
      if probOfRain == 1:
        print("With a 10% chance of rain.")
      elif probOfRain == 2:
        print("With a 20% chance of rain.")
      elif probOfRain == 3:
        print("With a 30% chance of rain.")
      else:
        print("With a 40% chance of rain.")
    elif 82<=F:
      print("Today's weather will be too hot, don't melt!")
      if probOfRain == 1:
        print("With a 10% chance of rain.")
      elif probOfRain == 2:
        print("With a 20% chance of rain.")
      elif probOfRain == 3:
        print("With a 30% chance of rain.")
      else:
        print("With a 40% chance of rain.")



#Name: Putting it All Together
#Purpose: This function asks the user which temperature conversion they want to perform and then asks the user for the current temperature.
#The program will perform the conversion using the temperature conversion function. The result of this function will be passed into the
#weather forecast function and then the user will be given a weather forecast for the day.
#Input(s): Two inputs: current_temp and choice
#Return(s): ans 2

while 1==1:
  choice=int(input('''Welcome to weather forecast! Would you like to convert from
                  1) Farenheit to Celsius or
                  2) Celsius to Farenheit? '''))
  current_temp=int(input('Great! Please enter your temperature: '))

  ans2=weather_forecast(current_temp,choice,True)
  print(ans2)