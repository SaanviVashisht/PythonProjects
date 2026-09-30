
#List Comparision

#Name: find_longer_list()
#Purpose: This function checks which list is longer - x or y and returns the longer list
#Input(s): x and y (lists)
#Return(s): The longer list of the two entered (x and y)

def find_longer_list(x,y):
  if len(x)>len(y):
    return x
  elif len(y)>len(x):
    return y
  else:
    return x
find_longer_list()



#Name: find_shorter_list()
#Purpose: This function checks which list is shorter- x or y and returns the shorter list
#Input(s): x and y (lists)
#Return(s): The shorter list of the two entered (x and y)

def find_shorter_list(x,y):
  if len(x)>len(y):
    return y
  elif len(y)>len(x):
    return x
  else:
    return x
find_shorter_list()



#Name: find_common_elements()
#Purpose: This function checks for the common elements between the two lists entered, and returns a new list (z) with the common elements
#Input(s): x and y (lists)
#Return(s): The union (z) of the two lists entered (x and y)

def find_common_elements(x,y):

  z = [value for value in x if value in y]
  return z
find_common_elements()