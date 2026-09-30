#Name: check_prime()
#Purpose: This function checks whether a number (an integer) entered is prime or not.
#If the integer is a prime number, the function returns True. If it isn't, it returns false.
#If the user does not enter an integer, the program tells the user to revise their input.
#Input(s): num (string)
#Return(s): True/False


from math import sqrt
emptylist=[]
def check_prime():
  try:
    num=input('Enter an integer: ')
    n = int(num)
    for i in range(1,n+1):
      mod=n%i
      if(mod ==0):
        emptylist.append(i)

    count=len(emptylist)
    if count == 2:
      return True#,emptylist
      print("yes")
    elif count >2:
      return False#,emptylist
      print("no")
  except ValueError:
      print('You have not entered an integer. Please enter again.')
      return False

check_prime()




#Name: prime_factors()
#Purpose: This function takes in an integer and does one of two things based on what user chooses:
  #1) Checks whether or not the number is prime
  #2) Gives a list of all the prime factors of the number
#Input(s): num (string)
#Return(s): True/False or emptyList

from math import sqrt
emptylist=[]
def prime_factors():
  try:
    num=input('Enter an integer: ')
    n = int(num)
    choice=int(input('Please enter 1 if you would just like to check if the number is prime. If you would like to see all the prime factors as well type 2: '))
    if choice==1:
        for i in range(1,n+1):
          mod=n%i
          if(mod ==0):
            emptylist.append(i)

        count=len(emptylist)
        if count == 2:
          return True#,emptylist
          print("yes")
        elif count >2:
          return False#,emptylist
          print("no")
    elif choice==2:
        for i in range(1,n+1):
          mod=n%i
          if(mod ==0):
            emptylist.append(i)

        count=len(emptylist)
        if count == 2:
          return True,emptylist
          print("yes")
        elif count >2:
          return False,emptylist
          print("no")
  except ValueError:
      print('You have not entered an integer. Please enter again.')
      return False

prime_factors()

