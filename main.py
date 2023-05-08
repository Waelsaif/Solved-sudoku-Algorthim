import numpy as np
from array import *

board = [[9, 6, 0, 0, 4, 0, 1, 0, 0],
        [0, 0, 0, 3, 8, 0, 0, 0, 0],
        [7, 0, 8, 0, 6, 0, 0, 0, 9],
        [1, 2, 0, 8, 0, 0, 9, 0, 3],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [3, 0, 5, 0, 0, 2, 0, 6, 4],
        [8, 0, 0, 0, 9, 0, 4, 0, 7],
        [0, 0, 0, 0, 3, 8, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 8, 5]]

def possible(y,x,n):          
    global board
    for i in range (0,9):
        if board[y][i] == n:  
            return False
    for i in range (0,9):     
        if board[i][x] == n:  
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range (0,3):
        for j in range (0,3):
            if board[y0+i][x0+j] == n:  
                return False
    return True

possible(4,4,5)  

print("The solved Sudoku is:");

def solve():
    global board
    for y in range (9):
        for x in range (9):
            if board[y][x] == 0:   
                for n in range (1,10):
                    if possible(y,x,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0  
                return  
    print(np.matrix(board))   
    input("")
    
solve()
