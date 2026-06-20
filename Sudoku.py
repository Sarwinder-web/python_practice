def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board,row,col,num):
    n=9
    # row checking 
    for c in range(n):
        if board[row][c]==num:
            return False
    # col checking 
    for r in range(n):
        if board[r][col]:
            return False 
    # for 3*3 box
    start_row = (row//3)*3
    start_col = (col//3)*3
    for r in range(start_row,start_row+3):
        for c in range(start_col,start_col+3):
            if board[row][col]==num:
                return False
    return True 
def solve(board):
    empty = find_empty(board)

    if empty is None:
        return True 
    
    row , col = empty 

    for num in range(1,10):

        if is_valid(board,row,col,num):
            board[row][col]=num

        if  solve(board):
            return True 
        
        board[row][col]=0

    return False 

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],

    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],

    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve(board):

    for row in board:
        print(*row)

else:
    print("No solution exists")