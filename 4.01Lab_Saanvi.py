#Part I
#A
#Name: get_numbers()
#Purpose: This function asks the user to enter several integers and stores them in a list.
#The function does this until the user types "done".
#Input(s): none
#Return(s): numbers(list)
def get_numbers():
  numbers=[]
  while 1==1:
    try:
      listOfIntegers = int(input('Please enter integers and type "done" when you are done: '))
      numbers.append(listOfIntegers)
    except ValueError:
      break
  print("This is the list of numbers you have input",numbers)
  return numbers

get_numbers()

#Part I
#B
#Name: count_evens()
#Purpose: This function takes in a list and returns the number of even integers in the list
#Input(s): listOfIntegers(int)
#Return(s): even_numbers(list)
def count_evens(listOfIntegers):
  even_numbers=[]
  for i in listOfIntegers:
    if i%2==0:
      even_numbers.append(i)
  print("Numbers of evens in the list is",len(even_numbers))
  return even_numbers

#count_evens([1,2,3,4,5,6])

#Part I
#C
#Name: main()
#Purpose: This function uses a single line of code to call both functions(get_numbers() and count_evens())
#Input(s): none
#Return(s): none
def main():
  count_evens(get_numbers())

main()

#Part 2
#A
#Name: name_list()
#Purpose: This function asks the user to input names and stores them in a list. It returns the list of names created.
#This function continues to take the input from the user until the user types "done".
#Input(s): none
#Return(s): list1[list]
def name_list():
  list1=[]
  while 1==1:
    listOfNames = input("Please enter names: ")
    if listOfNames=='done':
      break
    list1.append(listOfNames)
  return list1
name_list()

#Part 2
#B
#Name: congrats()
#Purpose: This function takes in a list as an argument. This function uses a for loop to go through
#the inputted list of names, and prints out a congratulations statement for each person, using a
#random event from the events list.
#Input(s): listOfIntegers(int)
#Return(s): even_numbers(list)
import random

def congrats(x):
  listOfHappyEvents=[" on your first successful skydive"," on getting your driver's license", " on getting straight A's'"]
  for i in x:
    randomElement=random.choice(listOfHappyEvents)
    print("Congrats "+i+randomElement)
#congrats(x)

#Part 2
#C
#Name: main2()
#Purpose: This function uses a single line of code to call both functions(name_list() and congrats())
#Input(s): none
#Return(s): none
def main2():
  congrats(name_list())

main2()

#Part 3
#A
#Name: count_letter()
#Purpose: This function takes in a word and a letter and returns the number of
#times the letter occurs in the word.
#Input(s): two inputs - word and letter(string)
#Return(s): one of two - if the letter is not in the word then it returns that (str)
#otherwise it returns the count(int)
def count_letter(word,letter):
  count = 0
  for i in word:
    if i == letter:
      count = count+1
  if count==0:
    print("The word does not contain the letter.")
  return count

print(count_letter('San', 'z'))

#Main Program
word, letter = input("Enter a word and a letter seperated by a space: ").split(" ")
count_letter(word,letter)

#Part 4
#A
#Name: get_first_letter()
#Purpose: This function takes in a word and returns the first letter of the world capitalized
#Input(s): word(str)
#Return(s): newword(list)

def get_first_letter(word):
    newword = word[0].capitalize()
    return (newword)

get_first_letter('saanvi')

#Part 4
#B
#Name: acronym()
#Purpose: This function takes in a complete sentence and returns a list of capitalized letters where
#each letter is the first letter of every word in the sentence.
#Input(s): sentence(str)
#Return(s): chars(list)

def acronym(sentence):
  words=sentence.split(" ")
  chars=[]
  for word in words:
    chars.append(get_first_letter(word))
  return(chars)
acronym('hi i am saanvi')

#Part 4
#C
#Name: mainProgram()
#Purpose: This function asks the user for a sentence and then prints an acronym for the sentence.
#Input(s): none
#Return(s): none
def mainProgram():
  user=input('Enter a sentence to convert into an acronym: ')
  x = acronym(user)
  for i in x:
    print(i)
mainProgram()