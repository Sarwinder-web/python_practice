def isSafe(board, row, col):
    n = len(board)

    # column check
    for i in range(row - 1, -1, -1):
        if board[i][col] == 1:
            return False

    # left diagonal ↖
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # right diagonal ↗
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row):
    n = len(board)

    # base case
    if row == n:
        for r in board:
            print(r)
        print()
        return

    # try every column in this row
    for col in range(n):

        if isSafe(board, row, col):

            board[row][col] = 1      # place queen

            solve(board, row + 1)    # go to next row

            board[row][col] = 0      # backtrack

# driver code
n = 4
board = [[0 for _ in range(n)] for _ in range(n)]

solve(board, 0)