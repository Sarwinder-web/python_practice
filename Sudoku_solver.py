def is_safe(board,row,col,num):
    for i in range(9):
        if board[row][i] == num:
            return False 
    
    for i in range(9):
        if board[i][col] == num:
            return False
        
    staring_row = (row//3)*3 
    starting_col = (col//3)*3

    for i in range(staring_row ,staring_row + 3):
        for j in range(starting_col , starting_col +3):
            if board[i][j] == num:
                return False
            
    return True 


def solve(board):

    for row in range(9):
        for col in range(9):

            if board[row][col]==".":
                for num in range(1,10):
                    if is_safe(board,row,col,num):
                        board[row][col] = num
                        if solve(board):
                            return True 
                        board[row][col] = "."

                return False
    return True

