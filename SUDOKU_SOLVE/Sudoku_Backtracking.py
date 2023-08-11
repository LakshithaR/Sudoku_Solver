#If Solution exists, print the Grid
def printing(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()
        
# Function to Find the entry in the Grid that is still not used; Searches the grid to find an
# entry that is still unassigned. If found, the reference parameters row, col will be set the location
# that is unassigned, and true is returned. If no unassigned entries remains, false is returned.
# 'l' is a list  variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns.        
def find_empty_loc(grid,l):
    for i in range(9):
        for j in range(9):
            #If there still exixts any unassigned values (i.e. 0)
            if (grid[i][j]==0):
                l[0]=i
                l[1]=j
                return True
    #If all cells are assigned, return False
    return False

#If num is present in that particular row
def in_row(grid,row,num):
    for i in range(9):
        #If num exists in that particular row, then return False
        if grid[row][i]==num:
            return False
    #If no num exists in any rows, then return True
    return True

#If num is present in that particular column
def in_col(grid,col,num):
    for i in range(9):
        #If num exists in that particular column, then return False
        if grid[i][col]==num:
            return False
    #If no num exists in any columns, then return True
    return True

#If num is present in that particular 3*3 subgrid
def in_grid(grid,row,col,num):
    for i in range(3):
        for j in range(3):
            #If num exists in that particular 3*3 subgrid
            if grid[row+i][col+j]==num:
                return False
    #If no num exists in any grid(3*3), then return False
    return True

#Checks if num can be placed in that cell or not
def check_loc_safe(grid,row,col,num):
    #Returns True if num can be placed in that particular cell, else return False
    return (in_row(grid,row,num)  and
        in_col(grid,col,num) and
        in_grid(grid,row-row%3,col-col%3,num))
    
#Takes a partially filled-in grid and attempts to assign values to all unassigned locations in such a
#way to meet the requirements for Sudoku solution.      
def sudoku(grid):
    #'l' is a list variable that keeps the record of row and col in find_empty_loc() 
    l=[0,0]
    
    #If there is no unassigned cells, then we can return True
    if (not find_empty_loc(grid,l)):
        return True
    
    #Assigning list values to row and col that we got from the above Function
    row=l[0]
    col=l[1]
    
    #Considering the digits from 1 to 9
    for i in range(1,10):
        #If we can place i in that particular cell
        if (check_loc_safe(grid,row,col,i)):
            #make tentative assignment
            grid[row][col]=i  
            
            #If success, the return           
            if sudoku(grid):
                return True   
            
            #If not, assign value of the cell to 0, then iterate over next value         
            grid[row][col]=0
            
    #This is used to trigger backtracking    
    return False

#Driver main function to test above functions
if __name__=="__main__":
    
    #creating a 2D array for the grid with initial values 0
    grid=[[0 for i in range(9)]for y in range(9)]
    
    #Assign values
    #Replace the grid with sudoku question
    #0 refers to the unassigned cells
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    #If solution exists   
    if (sudoku(grid)):
        #Print the Grid
        printing(grid)
    #If no solutions exists        
    else:        
        print("No Solution Exists")