coins = 22
print("Take turns removing 1,2, or 3 coins.\nYou win if you take the last coin.")
p1name = input('Player 1, what is your name? ')
p2name = input('Player 2, what is your name? ')

while coins>0:
    player1 = int(input(p1name+' please enter a number: '))
    if player1 >3:
        print("Invalid entry by {}, please try again!".format (p1name))
        player1 = int(input(p1name+' please enter a number: '))
        coins = coins-player1
        print("Total coins remaining: "+str(coins))
    elif player1 == coins:
        print(p1name,"wins!")
        print(p2name,"loses!")
        break
    else:
        coins = coins-player1
        print("Total coins remaining: "+str(coins))
        
    player2 = int(input(p2name+' please enter a number: '))
    if player2 >3:
        print("Invalid entry by {}, please try again!".format(p2name))
        player2 = int(input(p2name+' please enter a number: '))
        coins = coins-player2
        print("Total coins remaining: "+str(coins))
    elif player2 == coins:
        print(p2name,"wins!")
        print(p1name,"loses!")
        break
    else:
        coins = coins-player2
        print("Total coins remaining: "+str(coins))
   
