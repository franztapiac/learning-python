# Homework #06 - Advanced Loops
# Written by Franz A. Tapia Chaca
# on 30 January 2021


# Function: Initialises a 2D matrix filled with spaces " ", with the specified size (rows and columns)
# example board = [ [" ", " ", " "],
#                   [" ", " ", " "],
#                   [" ", " ", " "] ]
# ^ 3 rows, 3 columns
def create_array(rows, columns):
    board = []
    for r in range(rows):
        board.append([" "])  # to the board list, append a list with one " " character to start the row
        for c in range(columns-1):
            board[r].append(" ")  # to the row, append a " " character for each remaining column
    return board


# Function: Prints a horizontal line with length appropriate for the number of columns
def h_line_print(columns):

    h_line_len = 2 * columns + 1

    for i in range(h_line_len):
        print("-", end="")
    print("\n", end="")


# Function: Prints playing board with specified size (rows and columns)
def print_board(rows, columns):

    # Create array of empty board data
    board = create_array(rows, columns)

    # Prints top line
    h_line_print(columns)

    # Prints rest of board
    for r in range(rows):
        for c in range(columns):
            print("|" + board[r][c], end="")
        print("|\n", end="")
        h_line_print(columns)

    if rows <= 16 and columns <= 94:  # max size of board that fits on my screen is 16 rows by 94 columns
        return True
    else:
        return False


row_input = int(input("Number of rows: "))
column_input = int(input("Number of columns: "))

print("Does the playing board fit on Franz's maximised terminal and screen without wrapping?\n"\
      + str(print_board(row_input, column_input)))
