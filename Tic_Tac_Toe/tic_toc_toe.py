import random

#simply prints the divider between rows
def printHorDiv():
    print ("-------------")

#prints out the tic tac toe board in its current state
def PrintBoard(board):
    print (" " + board[6] + " " + "|" + " "  + board[7] + " " + "|" + " " + board[8])
    printHorDiv()
    print (" " + board[3] + " " + "|" + " "  + board[4] + " " + "|" + " " + board[5])
    printHorDiv()
    print (" " + board[0] + " " + "|" + " "  + board[1] + " " + "|" + " " + board[2])


#check if any of the winning states have all 3 entries matching, and those entries aren't blank.
def WinCheck (board):
    #horizontal wins
    if (board[0] == board[1] and board[0] == board[2] and not (board[0] ==" ")):
        return True
    elif (board[3] == board[4] and board[3] == board[5] and not (board[3] ==" ")):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and not (board[6] ==" ")):
        return True
    #vertical wins
    elif (board[0] == board[3] and board[0] == board[6] and not (board[0] ==" ")):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and not (board[1] ==" ")):
       return True
    elif (board[2] == board[5] and board[2] == board[8] and not (board[2] ==" ")):
       return True
    #diagonal wins
    elif (board[0] == board[4] and board[0] == board[8] and not (board[0] ==" ")):
       return True
    elif (board[2] == board[4] and board[2] == board[6] and not (board[2] ==" ")):
       return True
    else:
        return False

#if there's no blanks left, return true
def TieChecker(board):
    blankdetector = False
    for i in range (0,9):
        if board[i] == " ":
            blankdetector = True
    return not blankdetector 


#ask the player which letter they want to be, keep asking until they input correctly
def GetPlayerLetter():
    choice = ""
    validchoice = False
    while (not validchoice):
        choice = input("Player 1, please choose your side (x or o):")
        if ((not choice == "x") and (not choice == "o")):
            print ("please check your input and try again")
        else:
            validchoice = True
    return choice

def GetPlayMode():
    choice = ""
    validchoice = False
    while (not validchoice):
        choice = input("Would you like to play a player or cpu? (type p or c):")
        if ((not choice == "p") and (not choice == "c")):
            print ("Please check your input and try again")
        else:
            validchoice = True
    return choice


#returns list of possible valid moves    
def ComputerMoveFinder(board):
    availablemoves = [i for i, position in enumerate(board) if position == " "]
    return availablemoves


#checks for moves where the computer can win, and the player can win
def ComputerCriticalMoveDetector(availablemoves, board, playerletter, computerletter):
    winningmoves = []
    blockingmoves = []
    #try placing each letter in each available space and check which ones lead to a win
    for possiblemove in availablemoves:
        board[possiblemove] = playerletter
        if WinCheck(board):
            blockingmoves.append(possiblemove)
        board[possiblemove] = computerletter
        if WinCheck(board):
            winningmoves.append(possiblemove)
        board[possiblemove] = " "
    return (winningmoves, blockingmoves)
            

def NewGame ():
    #keep track of how the game ended
    #1 = player1 won, 2 = player2 won, 0 = tie
    wincondition = 0

    #show the players the input map
    print ("I recommend you play on a number pad!")
    print ("Please refer to the following input map when making your moves"  )
    board = ["1","2","3","4","5","6","7","8","9"]
    PrintBoard(board)
    #clear the board
    for i in range(0,9):
        board[i]= " "
    #ask the player if they want to play a person or cpu
    playmode = GetPlayMode()
   
    
    #ask the player which side they want to be
    playerone = GetPlayerLetter()
    if playerone == "x":
        playertwo = "o"
    else:
        playertwo = "x"
    print ("Player one is " + playerone)
    print ("Player two is " + playertwo)
    #randomize who goes first
    currentplayer =  random.randint(1,2)
    if currentplayer == 1:
        print ("Player one is going first")
    else:
        print ("Player two is going first")
    #check if the game is won, if not, a player goes, and then the turn is switched to the other player until someone wins or ties
    while not WinCheck(board) and not TieChecker(board):
        #if a new round starts, it could end in a tie
        wincondition = 0
        if currentplayer == 1:
            #some blank spaces before showing the current state for clarity
            print (" ")
            print (" ")
            print ("Player one's turn")
            Playerturn (board, playerone)
            #switch players
            currentplayer = 2
            #if the game just ended, player one won
            if WinCheck(board):
                wincondition = 1

        elif playmode == "c":
            print (" ")
            print (" ")
            print ("Cpu's turn")
            possiblemoves = ComputerMoveFinder(board)
            critical = ComputerCriticalMoveDetector(possiblemoves, board, playerone, playertwo)
            #if theres a winning move, make it
            if critical[0]:
                play = random.choice(critical[0])
            #if theres a winning move for the player, block it
            elif critical[1]:
                play = random.choice(critical[1])
            #otherwise pick a random move
            else:
                play = random.choice(possiblemoves)
            board[play] = playertwo
            currentplayer = 1
            if WinCheck(board):
                wincondition = 2
        else:
            print (" ")
            print (" ")
            print ("Player two's turn")
            Playerturn (board, playertwo)
            currentplayer = 1
            #if the game just ended, player two won
            if WinCheck(board):
                wincondition = 2
    #display the final state of the board
    print (" ")
    print (" ")
    print ("Final state of the game!")
    PrintBoard(board)
    #was it a draw or a victory? celebrate
    if wincondition == 0:
        print ("Draw game!")
    elif wincondition == 1:
        print ("Player one has won!")
    else:
        print ("Player two has won!")
        


#during a players turn, display the current state of the board, and ask for a move until a proper one is made
def Playerturn (board, player):

    PrintBoard(board)
    validmove = False
    while not validmove:
        choice = input("Please pick where you would like to place an " + player + " :(1-9)")
        #call function that handles player move
        validmove = BoardMoveCheck(choice, board)
        #when a valid move is finally made, update the board
        if validmove:
            board[int(choice)-1] = player
    return board


#check if the requested move is possible and properly formatted, if not try again
def BoardMoveCheck(number, board):
    if number not in ["1","2","3","4","5","6","7","8","9"]:
        print ("Please pick a number between 1 and 9")
        return False
    elif (board[int(number) - 1] == " "):
        return True
    else:
        print ("Invalid move, please try again")
        return False

    
        

#main start

#seed our rand function
random.seed()
stillplaying = True
while (stillplaying):
    #start the game
    NewGame()
    result = input("Would you like to play again? (y/n)")
    if not result == "y":
        stillplaying = False


#user input map
# 7, 8, 9
# 4, 5, 6
# 1, 2, 3

#programmer array map
# 6,7,8
# 3,4,5
# 0,1,2

