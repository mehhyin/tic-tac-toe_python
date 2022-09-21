#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def new_board():
    return {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

#restart game board 
# board = new_board

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    board[position] = mark


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    board_copy = {}
    for key, value in board.items():
        if value == ' ':                                        #and value != 'X' and value != 'O' (redundant, don't have to add that in since only need to check for empty spaces)
            board_copy[key] = str(key)
        else:
            board_copy[key] = value 
        
    

    print(board_copy[1] + ' | ' + board_copy[2] + ' | ' + board_copy[3] + '\n' +
          '---------' + '\n' +
          board_copy[4] + ' | ' + board_copy[5] + ' | ' + board_copy[6] + '\n' +
          '---------' + '\n' +
          board_copy[7] + ' | ' + board_copy[8] + ' | ' + board_copy[9])



# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    if not position.isdigit():
        print('Error, ' + position + ' is not a number!')              #check if the value entered is a digit or not. If it isn’t a digit then print an error message. If enter abc = program stop
        return False
    x = int(position)
    if x < 1 or x > 9 or board[x] == 'X' or board[x] == 'O':
        return False
    return True 
    

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
    [1, 5, 9],
    [7, 5, 3]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for a, b, c in winCombinations:
        if(board[a] == board[b] == board[c] == player):
            return True
    return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for y in board:
        if board[y] == ' ':
            return False
    return True



#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
def game():
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')
    gameEnded = False
    currentTurnPlayer = 'X'
# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")

#asking for input and validating it
        while not validateMove(move):
            print('Invalid input, please try again!')
            move = input(currentTurnPlayer + "'s turn, input: ")

#updating the board
        markBoard(int(move), currentTurnPlayer)
        printBoard()

#check win or tie situation
        if checkWin(currentTurnPlayer):
            print('You are the winner : ' + currentTurnPlayer)
            gameEnded = True

        elif checkFull():
            print('It is a tie!')
            gameEnded = True
            
    #switch user
        else:
            if currentTurnPlayer == 'X':
                currentTurnPlayer = 'O'
            else:
                currentTurnPlayer = 'X'
        

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
game()                          
while True:
    restart = input('Do you want to restart the game? (y/n): ')
    if restart == 'y' or restart == 'Y' or restart == 'YES' or restart == 'yes' or restart == 'Yes':
        board = new_board()        #will restart the board or else it will continue to use the previous filled board
        game()
    elif restart == 'n'or restart == 'N' or restart == 'NO' or restart == 'no' or restart == 'No':
        print('Thanks for playing!')
        break                 
    else:
        print('Invalid')
        # continue   (don't have to put continue since its redundant)            


