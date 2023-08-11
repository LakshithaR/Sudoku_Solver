# Number of Rows and columns = 9
N=9

#If solution exists printing the Grid
def printing(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=" ")
        print()
        
#To check if num can be placed in that particular cell        
def isSafe(grid, row, col ,num):
    #To check if num already exists in that particular row
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    #To check if num already exists in the particular column
    for x in range(9):
        if grid[x][col]==num:
            return False
        
    #To check if num is present in that particular 3*3 subgrid
    srow=row-row%3
    scol=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[srow+i][scol+j]==num:
                return False
    return True
        
#Takes a partially filled-in grid and attempts to assign values to all unassigned locations in such a
#way to meet the requirements for Sudoku solution.
def sudoku(grid,row,col):
    #If row = 8 and column = 9; return True to stop further operations
    if (row==N-1 and col==N):
        return True
    
    #If reached the end of the column, move to next row, and column becomes 0
    if col==N:
        row+=1
        col=0
        
    #if there is any value (except for 0), go to next column 
    if grid[row][col]>0:
        return sudoku(grid,row,col+1)
    
    #Iterate over the values from 1-9, to place the correct answer in that cell
    for i in range(1,N+1,1):
        #Checks if we can assign ith value to that particular row and column
        if isSafe(grid, row, col, i):
            grid[row][col]=i
            #Checking for next possibility with next column
            if sudoku(grid,row, col+1 ):
                return True
        #Replace the number with 0, because our assumption was wrong
        #So we iterate to next number
        grid[row][col]=0
    #If no such possible solution exists return False
    return False
      
#Replace the grid with sudoku question
#0 refers to the unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

#If solution exists
if (sudoku(grid,0,0)):
    #Print the Grid
    printing(grid)
#If solution does not exists
else:
    print("No Solution Exists")