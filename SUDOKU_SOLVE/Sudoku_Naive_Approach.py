N=9
def printing(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=" ")
        print()
        
def isSafe(grid, row, col ,num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col]==num:
            return False
    srow=row-row%3
    scol=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[srow+i][scol+j]==num:
                return False
    return True
        

def sudoku(grid,row,col):
    if (row==N-1 and col==N):
        return True
    if col==N:
        row+=1
        col=0
    if grid[row][col]>0:
        return sudoku(grid,row,col+1)
    for i in range(1,N+1,1):
        if isSafe(grid, row, col, i):
            grid[row][col]=i
            if sudoku(grid,row, col+1 ):
                return True
        grid[row][col]=0
    return False
      
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
if (sudoku(grid,0,0)):
    printing(grid)
else:
    print("No Solution Exists")