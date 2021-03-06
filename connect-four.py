# Connect 4: Play on one computer
# Written by Franz A. Tapia Chaca
# on 06 March 2021

# Rules of the game: https://www.ludoteka.com/clasika/connect-4.html
# Epic olympic match: https://www.youtube.com/watch?v=d-7eiD2DNGw

###############
## FUNCTIONS ##
###############

# Function to initialise 6 x 7 board with empty spaces
def initialiseBoard(board):
    for row in range(1, 7):  # 1 to 6
        board.append([])            # add a new row
        for column in range(1, 8):  # 1 to 7
            board[row-1].append(" ")  # and fill that row with spaces


# Function to print the current board to the screen
def printBoard(board):
    print("  1 2 3 4 5 6 7")
    for row in range(1, 7):  # 1 to 6
        print(str(row) + "|", end="")
        for column in range(1, 8):  # 1 to 7
            print(board[row-1][column-1] + "|", end="")
        print("\n", end="")


# Function to confirm that player played a valid move
def validMove(board, moveColumn):
    if 1 <= moveColumn <= 7 and board[0][moveColumn - 1] == " ":
        return True


# Function to update the board with the player input
def updateBoard(board, moveColumn, player):
    for row in range(6, 0, -1):  # 6 to 1
        if board[row-1][moveColumn-1] == " ":
            board[row-1][moveColumn-1] = player
            break


# Function to determine if player connected 4
def connectFour(board, moveColumn, player):
    # Connect 4 analysis is based on counting same-player adjacent moves, for each move,
    # across the move row, column and diagonals
    # For a graphical explanation, visit:
    # https://github.com/franztapiac/pirple.com-python/blob/main/supplementary-connectFour-function.pdf

    # 1. Get row of play
    #####################
    moveRow = 6  # last possible row
    for row in range(5, 0, -1):  # 5 to 1
        if board[row-1][moveColumn-1] != " ":
            moveRow = row
        else:
            break

    # 2. Row analysis
    ##################
    count = 0
    for column in range(1, 8):  # 1 to 7
        if board[moveRow-1][column-1] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # 3. Column analysis
    #####################
    count = 0
    for row in range(1, 7):  # 1 to 6
        if board[row-1][moveColumn-1] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # 4. Diagonal analysis 1: left to right \
    ##########################################

    # Starting element
    startRow = moveRow
    startColumn = moveColumn
    while True:
        if startRow == 1 or startColumn == 1:
            break
        else:
            startRow -= 1
            startColumn -= 1

    # Ending element
    endRow = moveRow
    endColumn = moveColumn
    while True:
        if endRow == 6 or endColumn == 7:
            break
        else:
            endRow += 1
            endColumn += 1

    # Counting iteration
    count = 0
    if endRow - startRow + 1 >= 4:  # If connect 4 is even possible in the diagonal
        for shift in range(startRow - moveRow, endRow - moveRow + 1):
            if board[moveRow-1+shift][moveColumn-1+shift] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # 5. Diagonal analysis 2: left to right /
    ##########################################
    # Starting element
    startRow = moveRow
    startColumn = moveColumn
    while True:
        if startRow == 6 or startColumn == 1:
            break
        else:
            startRow += 1
            startColumn -= 1

    # Ending element
    endRow = moveRow
    endColumn = moveColumn
    while True:
        if endRow == 1 or endColumn == 7:
            break
        else:
            endRow -= 1
            endColumn += 1

    # Counting iteration
    count = 0
    if startRow - endRow + 1 >= 4:  # If connect 4 is even possible in the diagonal
        for shift in range(startRow - moveRow, endRow - moveRow - 1, -1):
            if board[moveRow-1+shift][moveColumn-1-shift] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0


######################
## BODY OF THE GAME ##
######################

wishToPlay = True

while wishToPlay:
    board = []              # An empty list
    initialiseBoard(board)  # is made into a 6 x 7 board with empty spaces
    printBoard(board)       # and is printed onto the screen.
    player = "o"

    while True:         # Loop used to iterate turn-taking

        while True:     # Loop used to validate user input
            try:
                moveColumn = int(input("Player " + player + ", which column (1-7) do you wish to play at?"))
            except:     # if non-integers are entered, program doesn't break down
                print("Invalid input. Please enter an integer between 1 to 7.")
                printBoard(board)
                continue
            if validMove(board, moveColumn):
                updateBoard(board, moveColumn, player)
                break   # Exit user input loop
            else:
                print("Invalid input. Please enter an integer between 1 to 7.")
                printBoard(board)

        printBoard(board)
        if connectFour(board, moveColumn, player):
            print("Connect 4!")
            print("Player " + player + " wins!")
            break   # Exit turn-taking loop
        else:
            if player == "o":
                player = "x"
            else:
                player = "o"

    while True:     # Loop used to determine user's intention to play again
        encore = input("Do you wish to play again (Y/N)?")
        if encore == "y" or encore == "Y":
            break
        elif encore == "n" or encore == "N":
            wishToPlay = False
            break
        else:
            print("Invalid input. Only enter y/Y for Yes or n/N for No.")
            continue
