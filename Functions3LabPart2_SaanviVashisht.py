#List Comparision

#Longer List

def find_longer_list():
  x= list(input('Please enter a list: '))
  y=list(input('Please enter another list: '))
  if len(x)>len(y):
    return x
  elif len(y)>len(x):
    return y
  else:
    return x
find_longer_list()



#Shorter List

def find_shorter_list():
  x= list(input('Please enter a list: '))
  y=list(input('Please enter another list: '))
  if len(x)>len(y):
    return y
  elif len(y)>len(x):
    return x
  else:
    return x
find_shorter_list()



#Intersection of Two Lists

def find_common_elements():
  x= list(input('Please enter a list: '))
  y=list(input('Please enter another list: '))
  z = [value for value in x if value in y]
  return z
find_common_elements()