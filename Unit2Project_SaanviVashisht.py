#The whole game is put into one function - beginGame
#The user can define the board game and pass it as a parameter

def beginGame(boardGames):
  rowsCount= len(boardGames)  #rowsCount and columnsCount tell us the total number of rows and columns in boardGames
  columnsCount = len(boardGames[0])
  print("Welcome to the Monster Mansion! You are currently trapped in a dungeon, and to escape, you must win this game! To get started type any of the following commands: left, right, up, down, grab, fight, help, or inventory.")
  print('The current room contains nothing.')
  rows=0  #These are all the variables involved in the game/the functioning of the game
  columns=0
  swordCount=0
  magicStones=0
  swordRow=0
  swordColumn=0
  isValid = True

  while(1==1):
    user = input("What do you wish to do? ").lower()

#This block of code accounts for all the possibilites if the user gives the input "down"
    if user=="down":
        backward='up' #This variable helps in ensuring that the user can go back upwards, in case they encounter a monster while coming downwards
        print('Your input is down.')
        gameBoardValue = boardGames[rows][columns].lower()
        if(gameBoardValue == "stairsdown" ):
          if(rows==0):
            print('You cannot move down')
          else:
            rows=rows-1
            print(rows)
            print(columns)


        else:
          print("Your input is invalid as there are no stairs")
          #isValid = False

#This block of code accounts for all the possibilites if the user gives the input "right"
    elif user=='right':
        backward='left' #This variable helps in ensuring that the user can go back left, in case they encounter a monster while coming right
        print('Your input is right.')
        columns=columns+1
        print(rows)
        print(columns)

        if(columns==columnsCount): #This condition ensures the user does not move out of the boundry of the board game defined
          print('You cannot move right')
          columns = columnsCount - 1
          #isValid = False
        gameBoardValue = boardGames[rows][columns].lower()
        if(gameBoardValue == "stairsup"):
          print("You have encountered stairs-up.")
        if(gameBoardValue == "stairsdown"):
          print("You have encountered stairs-down.")

#This block of code accounts for all the possibilites if the user gives the input "left"
    elif user=='left':
        backward='right' #This variable helps in ensuring that the user can go back right, in case they encounter a monster while coming left
        print('Your input is left.')
        columns = columns -1
        print(rows)
        print(columns)

        if(columns==-1):
          print('You cannot move left')
          columns=0
          #isValid = False
        gameBoardValue = boardGames[rows][columns].lower()
        if(gameBoardValue == "stairsup"  ):
          print("You have encountered stairs-up.")
        if(gameBoardValue == "stairsdown"  ):
          print("You have encountered stairs-down.")


#This block of code accounts for all the possibilites if the user gives the input "up"
    elif user=='up':
        backward='down' #This variable helps in ensuring that the user can go back downwards, in case they encounter a monster while coming upwards
        print('Your input is up.')
        gameBoardValue = boardGames[rows][columns].lower()
        if(gameBoardValue == "stairsup"  ):
          if(rows==rowsCount-1): #This condition ensures the user does not move out of the boundry of the board game defined
            print('You cannot move up.')
          else:
              rows=rows+1
              print(rows)
              print(columns)



        else:
          print("Your input is invalid as there are no stairs.")
          #isValid = False

    elif user=='help':
      print('You can choose from the following commands: left, right, up, down, grab, fight, help, or inventory.')
    elif user=="inventory":
      print("Sword count is ",swordCount)
      print("Magicstones count is ", magicStones)

    elif user=="restart":
      beginGame(boardGames)

#This block of code accounts for informing the user what each room contains everytime they enter that room
#If the user chooses to grab a sword or magic stones, the swords and magic stones disappear from that room once grabbed
    if isValid:
      print("The current room contains ",gameBoardValue)
      if(gameBoardValue== "sword"):
        swordInput = input("You have a sword. What do you wish to do? ").lower()
        if swordInput == "grab":
          swordCount = swordCount +1
          print("Your sword count is ",swordCount)
          boardGames[rows][columns] = "Nothing"
      if (gameBoardValue == "magicstones"  ):
        stoneInput = input("You have Magic stones. What do you wish to do? ").lower()
        if stoneInput == "grab":
          magicStones= magicStones+1
          boardGames[rows][columns] = "Nothing"
          gameBoardValue = "nothing"

      if (gameBoardValue == "win!"  ):
        print("You have encountered the winning prize")
        monsInput = input("What do you wish to do? ").lower()
        if(monsInput == "grab"):
          print("YOU WIN!!!!")
          break
  #Once the user encounters the boss monster, they must have both a sword and magic stones to defeat it, i.e., the sword count and magicstones count must be greater than 0
  #Once the boss monster is killed, it no longer exists in that room, and the sword and magic stones are set to 0
    #The same logic is applied for the monster
      if (gameBoardValue == "bossmonster"):
        print("You have encountered the Boss Monster")
        print("Your sword count is ",magicStones)
        print("Your Magic stones count is ",swordCount)
        monsInput = input("What do you wish to do? ").lower()
        if(monsInput == "fight" and swordCount > 0 and magicStones > 0):
          swordCount = swordCount -1
          magicStones = magicStones -1
          boardGames[rows][columns] = "Nothing"
          print("You have killed the monster and your sword count is",swordCount)
      if (gameBoardValue == "monster"):
        print("You have encountered the monster")
        print("Your sword count is ",swordCount)
        monsInput = input("What do you wish to do? ").lower()
        if(monsInput == "fight" and swordCount > 0):
          swordCount = swordCount -1
          boardGames[rows][columns] = "Nothing"
          print("You have killed the monster and your sword count is",swordCount)
        elif(monsInput==backward):
          if backward=='left':
            columns = columns -1
            print(rows)
            print(columns)
          elif backward=='right':
            columns=columns+1
            print(rows)
            print(columns)
          elif backward=='up':
            rows=rows+1
            print(rows)
            print(columns)
          else:
            rows=rows-1
            print(rows)
            print(columns)

        else:
          print("You have encountered the monster and either you don't have a sword or you don't want to fight. So, you lost the game!!")
          break;

rows=3
columns = 5
boardGames = [["" for x in range(columns)] for y in range(rows)]

boardGames[0][0]="Start"
boardGames[0][1]="Sword"
boardGames[0][2]="Nothing"
boardGames[0][3]="Monster"
boardGames[0][4]="StairsUp"
boardGames[1][0]="Nothing"
boardGames[1][1]="StairsUp"
boardGames[1][2]="Monster"
boardGames[1][3]="Sword"
boardGames[1][4]="StairsDown"
boardGames[2][0]="Sword"
boardGames[2][1]="StairsDown"
boardGames[2][2]="MagicStones"
boardGames[2][3]="BossMonster"
boardGames[2][4]="Win!"

beginGame(boardGames)