def is_ssafe(board,row,col,n):

    for i in range(row):
        if board[i][col] == "Q":
            return False
    
    
    i , j = row , col 
    while i>=0 and j>=0:
        if board[i][j] == "Q":
            return False
        i -=1
        j -=1
    
    i , j = row , col
    while i>=0 and j<n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True
    
def solve(board,row,n):
    if row==n:
        print(board)
        return
        
    for col in range(n):
        if is_ssafe(board,row,col,n):
            board[row][col]="Q"
            solve(board,row +1 ,n)
            board[row][col]="."

n = 4
board = [["." for _ in range(n)] for _ in range(n)]


