#Name: get_height()
#Purpose: This function asks the user for the height of the image they wish to create
#Input(s): none
#Return(s): height(int)

def get_height():
  height=int(input('What is the height of the drawing? '))
  return height
get_height()

#Name: get_width()
#Purpose: This function asks the user for the width of the image they wish to create
#Input(s): none
#Return(s): width(int)

def get_width():
  width=int(input('What is the width of the drawing? '))
  return width
get_width()

#Name: draw_stars()
#Purpose: This function calls get_height() and get_width() and given what the user inputs, this function draws a rectangle
#where height=number of rows and width=number of columns and each position is filled with a *
#Input(s): none
#Return(s): none

height = get_height()
width = get_width()
def draw_stars():
  for i in range(height):
    for j in range(width):
      print("* ", end='')
    print("")
draw_stars()

#Name: draw_stars_and_stripes()
#Purpose: This function calls get_height() and get_width() and given what the user inputs, this function draws a rectangle
#where height=number of rows and width=number of columns and each row alternates between *** and ---
#Input(s): none
#Return(s): none

height = get_height()
width = get_width()
def draw_stars_and_stripes():
  count=0
  for i in range(height):
    for j in range(width):
      if count%2==0:
        print("* ", end='')
      else:
        print("- ",end='')
    count=count+1
    print("")
draw_stars_and_stripes()

#Name: draw_increasing_triangle()
#Purpose: This function calls get_height() and get_width() and given what the user inputs, this function draws a triangle
#where height=number of rows
#Input(s): none
#Return(s): none

height = get_height()
def draw_increasing_triangle():

    for i in range(height):

        for j in range(i+1):

            print(j+1, end=" ")

        print()
draw_increasing_triangle()

#Name: draw__vertical_stars_and_stripes()
#Purpose: This function calls get_height() and get_width() and given what the user inputs, this function draws a rectangle
#where height=number of rows and width=number of columns and each spot alternates between * and -
#Input(s): none
#Return(s): none

height = get_height()
width = get_width()
def draw_vertical_stars_and_stripes():
  count=0
  for i in range(height):
    for j in range(width):
      if j%2==0:
        print("- ", end='')
      else:
        print("* ",end='')
    print("")
draw_vertical_stars_and_stripes()

#Name: draw_triangle()
#Purpose: This function calls get_height() and prints a triangle according to the user input
#Input(s): height(int)
#Return(s): none

height=get_height()
def draw_triangle(height):
    for i in range(1, height + 1):
        for j in range(height - i):
            print(" ", end="")
        for k in range(1, i*2):
            print("*", end="")
        print()

draw_triangle(3)