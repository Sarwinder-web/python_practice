def maze(r,c,path,grid,path_matrix,step):
    rows = len(grid)
    cols = len(grid[0])
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return
    if not grid[r][c]:
        return
    
    if r==rows -1 and c == cols -1:
        path_matrix[r][c] = step 
        print(path)

        for row in  path_matrix:
            print(row)
        print()
        
        path_matrix[r][c]=0
        return
    
    grid[r][c] = False
    path_matrix[r][c] = step
    
    if c < cols -1:
        maze(r,c+1,path + "R",grid,path_matrix,step +1 )
    if r < rows -1:
        maze(r+1,c,path + "D",grid,path_matrix,step +1)
    if c > 0:
        maze(r,c-1,path + "L",grid,path_matrix,step +1)
    if r>0:
        maze(r-1,c,path + "U",grid,path_matrix,step +1)
    
    grid[r][c] = True 
    path_matrix[r][c]=0

grid = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

path_matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

maze(0, 0, "", grid, path_matrix, 1)