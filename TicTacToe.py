player = 1
playerOne = 'X'
playerTwo = 'O'
def display_gameboard(gameBoard):
    '''
    Literally just a print statement that displays the gameBoard
    '''
    print(f'Here is the current game board:\n{gameBoard[0]}|{gameBoard[1]}|{gameBoard[2]}\n{gameBoard[3]}|{gameBoard[4]}|{gameBoard[5]}\n{gameBoard[6]}|{gameBoard[7]}|{gameBoard[8]}')

def user_choice():
    '''
    This function asks the user where they would like to place their piece in the current board.
    The available spaces is kept up using the acceptableRange list. If the player's choice is in
    the list it will pop that space out of the list and place the player's piece on the gameBoard.
    If not on the list it asks the user for an acceptable input.
    '''
    choice = 'wrong'
    while choice not in acceptableRange:
        choice = input(f"Please pick where you would like to place your piece ({acceptableRange}): ")
        if choice not in acceptableRange:
            print("Sorry, invalid choice!")
    acceptableRange.pop(acceptableRange.index(choice))
    return int(choice)-1 # subtracting 1 to get the proper index for placing the player's piece


def place_piece(gameBoard, position, player):
    '''
    This function places the player's piece into the gameBoard and returns the updated gameBoard
    '''
    if player == 1:
        gameBoard[position] = playerOne
    else:
        gameBoard[position] = playerTwo

    return gameBoard
def game_won(gameBoard, playerPiece):
    '''
    Checks all 8 possible winning scenarios.
    First 3 are rows, followed by the 3 columns and finally the 2 diagonals.
    '''
    return (gameBoard[0]==gameBoard[1]==gameBoard[2]==playerPiece) or\
           (gameBoard[3]==gameBoard[4]==gameBoard[5]==playerPiece) or\
           (gameBoard[6]==gameBoard[7]==gameBoard[8]==playerPiece) or\
           (gameBoard[0]==gameBoard[3]==gameBoard[6]==playerPiece) or\
           (gameBoard[1]==gameBoard[4]==gameBoard[7]==playerPiece) or\
           (gameBoard[2]==gameBoard[5]==gameBoard[8]==playerPiece) or\
           (gameBoard[0]==gameBoard[4]==gameBoard[8]==playerPiece) or\
           (gameBoard[6]==gameBoard[4]==gameBoard[2]==playerPiece)

def game_on():
    '''
    This function asks if the players are ready to play the game if yes it sets up the gameBoard
    with the new_game function.
    '''
    choice = 'Wrong'

    while choice not in ['Y', 'N']:
        choice = input("Ready to play? (Y or N) ").upper()

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose Y or N")

        if choice == 'Y':
            new_game()
            return True
        else:
            return False
def play_again():
    '''
    This function returns true if the players want to play another game.
    As long as it returns true the main loop running the game will keep going.
    Assumes that anything entered besides y means that you no longer want to continue.
    '''
    choice = input("Would you like to play again(Y or N)? ").upper()
    return choice == 'Y'

def new_game():
    '''
    This functions sets up the gameBoard and the acceptableRange at the start of every game.
    It returns these two variables as a tuple that must be unpacked.
    '''
    gameBoard = ['1','2','3','4','5','6','7','8','9']
    acceptableRange = ['1','2','3','4','5','6','7','8','9']
    return (gameBoard, acceptableRange)

'''
This is the while loop that controls the game function.  It makes all the calls to the above
functions and does the checks to see whether the game will continue or not.
'''
print("WELCOME TO TIC TAC TOE!\n\n\n")
while True:
    gameBoard, acceptableRange = new_game()
    gameOn = game_on()
    while gameOn:
        display_gameboard(gameBoard)
        position = user_choice()
        place_piece(gameBoard, position, player)
        if player == 1:
            if game_won(gameBoard, playerOne):
                print("\n\nPlayer One WINS!!!\n\n")
                break
            elif len(acceptableRange) == 0: # will only enter this if the board is full and neither player has been declared a winner.
                print("\n\n\nCATS GAME!!!\n\n\n")
                break
            else:
                player += 1
        else:
            if game_won(gameBoard, playerTwo):
                print("\n\nPlayer Two WINS!!!\n\n")
                break
            elif len(acceptableRange) == 0:
                print("\n\n\nCATS GAME!!!\n\n\n")
                break
            else:
                player -=1

    if not play_again():
        break
