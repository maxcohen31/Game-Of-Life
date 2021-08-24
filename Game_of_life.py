## CONWAY'S GAME OF LIFE ##
#Author: Emanuele

# Rules:
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# Game of life algorithm that takes a starting board and return a new board configuration based on game rules

from random import randint

# Random board
HEIGHT = 30
WIDTH = 30
grid = [[randint(0, 1) for i in range(HEIGHT)] for j in range(WIDTH)]

# Glider pattern
glider = [[0, 0, 1],
         [1, 0, 1],
         [0, 1, 1]]

# Spinner pattern
spinner = [[0, 1, 0],
           [0, 1, 0],
           [0, 1, 0]]

# Gosper glider gun pattern
gosper_glider_gun = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


def game_of_life(board):
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # Cell neighbors
    for row in range(len(board)):
        for col in range(len(board[0])):
            neighbors_alive = 0
            for n in neighbors:
                cell_row = row + n[0] # Row of the neighboring cell
                cell_col = col + n[1] # Column of the neighboring cell
                
                # Check if the cell is valid and if it was a living cell
                if 0 <= cell_row < len(board) and 0 <= cell_col < len(board[0]) and abs(board[cell_row][cell_col]) == 1:
                    neighbors_alive += 1
            # Rule 1-3        
            if board[row][col] == 1 and neighbors_alive < 2 or neighbors_alive > 3:
                board[row][col] = -1 # The cell is now dead
            # Rule 4              
            if board[row][col] == 0 and neighbors_alive == 3:
                board[row][col] = 2 # The cell is now alive
    
    # Return the new board            
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] > 0:
                board[row][col] = 1
            else:    
                board[row][col] = 0                            
    return board
        
