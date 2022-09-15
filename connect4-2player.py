import numpy as np

# Board dimentions
COLUMN_COUNT = 7
ROW_COUNT = 6

# Board creation
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

# Board printing is fliped so row 1 is in the bottom of the board
def print_board(board):
    print(np.flip(board, 0))

# Check that the column isnt full
def is_valid_spot(board, col):
    return board[ROW_COUNT-1][col] == 0

# Put a piece in selected column
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Get the next available row to put a piece in
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


# Defining all the winnning moves
def winning_move(board, piece):
    # Cheack horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    # check positivly sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    # check negativly sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()
print_board(board)

game_over = False
turn = 0

# Game running loop
while not game_over:
    turn = 1
    # player will keep his turn even if he enters an invalid input. Game will stop if one of the players wins.
    while turn == 1 and not game_over:
        # "try" and "except" so the game can keep running even when a player enters an invalid input.
        try:
            # get player input
            wanted_col = int(input(f'Player {turn} Select a column number (1-7 from left to right) : ')) - 1
        except ValueError:
            print('Thats not a valid input. Please enter a number between 1 and 7')
        else:
            if is_valid_spot(board, wanted_col):
                open_row = get_next_open_row(board, wanted_col)
                drop_piece(board, open_row, wanted_col, turn)
                print_board(board)
                if winning_move(board, turn):
                    print ("player 1 WON!!")
                    game_over = True
                turn = 2
            else:
                print('That spot is invalid. Please choose another column')
    
    while turn == 2 and not game_over:
        try:
            wanted_col = int(input(f'Player {turn} Select a column number (1-7 from left to right) : ')) - 1
        except ValueError:
            print('Thats not a valid input. Please enter a number between 1 and 7')
        else:
            if is_valid_spot(board, wanted_col):
                open_row = get_next_open_row(board, wanted_col)
                drop_piece(board, open_row, wanted_col, turn)
                print_board(board)
                if winning_move(board, turn):
                    print('Player 2 WON!!')
                    game_over = True
                turn = 1

            else:
                print('That spot is invalid. Please choose another column')
