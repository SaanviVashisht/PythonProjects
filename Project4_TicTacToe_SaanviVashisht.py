#Name:initiate_game()
#Purpose: This function sets up the game
#Input(s): none
#Return(s): none

def initiate_game():
  board_positions = get_board_postions()
  print_board(board_positions)
  board = get_board()
  player_1, player_2 = initiate_players()
  is_board_full(board, player_1, player_2)




#Name:get_board_positions()
#Purpose: This function creates a playboard
#Input(s): none
#Return(s): board_positions(list)

def get_board_postions():
    board_positions = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    return board_positions



#Name:get_board()
#Purpose: This function creates a blank playboard
#Input(s): none
#Return(s): board(list)

def get_board():
    global board
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board



#Name:print_board()
#Purpose: This function prints the board
#Input(s): board(list)
#Return(s): board(list)

def print_board(board):
    rows = len(board)
    cols = len(board)
    print("---+----+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], " |", board[r][2])
        print("---+----+---")
    return board




#Name:initiate_players()
#Purpose: This function asks the users if they want to be "X" or "O" and assigns it to them
#Input(s): none
#Return(s): player_1 and player_2(str)

def initiate_players():
    player_1 = input("Player 1, do you want to be X or O? ").upper()
    if player_1 == "X":
        player_2 = "O"
        print("Player 2, you are O. ")
    else:
        player_2 = "X"
        print("Player 2, you are X. ")
    print("\n")
    return (player_1, player_2)


#Try-except: see how to turn the code around if player does not enter X or O


#Name:get_row_column()
#Purpose: This function, according to the player's input, returns a value of the board(a space of the board)
#Input(s): number(str)
#Return(s): space value of the board(int)

def get_row_column(number):
  match(number):
    case "1":
      return 0,0
    case "2":
      return 0,1
    case "3":
      return 0,2
    case "4":
      return 1,0
    case "5":
      return 1,1
    case "6":
      return 1,2
    case "7":
      return 2,0
    case "8":
      return 2,1
    case "9":
      return 2,2
    case _:
      return -1,-1




#Name: illegal_move()
#Purpose: This function checks if the player makes a move which is already made, and alerts them of the same
#Input(s): none
#Return(s): none

def illegal_move():
    print("The square you picked is already filled. Pick another one.")



#Name:is_winner()
#Purpose: This function checks if a player has won the game(using the various winning conditions of Tic Tac Toe)
#Input(s): board, player_1, player_2, and count
#Return(s): winner(bool)

def is_winner(board, player_1, player_2, count):
    winner = False
    #Checks the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == player_1):
            winner = True
            print("Player " + player_1 + ", you won!")

        elif (board[row][0] == board[row][1] == board[row][2] == player_2):
            winner = True
            print("Player " + player_2 + ", you won!")


    #Checks the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == player_1):
            winner = True
            print("Player " + player_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == player_2):
            winner = True
            print("Player " + player_2 + ", you won!")

    #Checks the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == player_1:
        winner = True
        print("Player " + player_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == player_2:
        winner = True
        print("Player " + player_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == player_1:
        winner = True
        print("Player " + player_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == player_2:
        winner = True
        print("Player " + player_2 + ", you won!")

    return winner




#Name:is_board_full()
#Purpose: This function checks if the board is full and if there is a tie
#Input(s): board, player_1, player_2
#Return(s): none

def is_board_full(board, player_1, player_2):
    count = 1
    winner = False
    while count < 10 and winner == False:
        gaming = start_game(board, player_1, player_2, count)
        pretty = print_board(board)

        if count == 9:
            print("The board is full. Game over.")
            if winner == False:
                print("There is a tie. ")

        #Checks if here is a winner
        winner = is_winner(board, player_1, player_2, count)
        count += 1
    if winner:
        print("Game over.")

    #This gives a report
    print_game_summary(count, winner, player_1, player_2)




#Name:print_game_summary()
#Purpose: This function prints the end results of the game - the winners or if there is a tie
#Input(s): count, winner, player_1, player_2
#Return(s): none

def print_game_summary(count, winner, player_1, player_2):
    print("\n")
    if (winner) and (count % 2 == 1 ):
        print("Winner : Player " + player_1 + ".")
    elif (winner) and (count % 2 == 0 ):
        print("Winner : Player " + player_2 + ".")
    else:
        print("There is a tie. ")

    restart = input("Do you want to restart the game (Y/N)? ").upper()
    if restart == "Y":
        initiate_game()
    else:
        print("Thanks for playing!")




#Name:start_game()
#Purpose: This function asks the user for their move, and places their symbol accordingly(while checking if that move has already been made)
#Input(s): board, player_1, player_2, count
#Return(s): board(list)

def start_game(board, player_1, player_2, count):
  #Decides the turn
    if count % 2 == 0:
        player = player_1
    elif count % 2 == 1:
        player = player_2
    print("Player "+ player + ", it is your turn. ")
    row_column = input("Where do you want to move? ")
    row, column = get_row_column(row_column)

    #Checks if player's selection is out of range
    while (row == -1 or column== -1):
        row_column = int(input("Select the correct move? "))
        row, column = get_row_column(row_column)

    #Checks if the square is already filled
    while (board[row][column] == player_1)or (board[row][column] == player_2):
        illegal_move()
        row_column = int(input("Where do you want to move? "))
        row, column = get_row_column(row_column)

    #Locates player's symbol on the board
    if player == player_1:
        board[row][column] = player_1

    else:
        board[row][column] = player_2

    return (board)

initiate_game()