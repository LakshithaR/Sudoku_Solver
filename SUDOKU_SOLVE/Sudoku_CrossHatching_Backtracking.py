N = 9  # Size of the Sudoku grid

# A utility function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

# Checks whether it's safe to place 'num' in the given row and column
def is_safe(grid, row, col, num):
    # Check if num is present in that particular row and column
    if num in grid[row] or num in [grid[i][col] for i in range(N)]:
        return False
    
    # Check if num is present in that 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

# Find the empty cell with the fewest remaining candidates
def find_empty_cell(grid):
    #These variables are initialized to large values (N + 1 for min_candidates and
    #-1 for min_row and min_col).
    #min_candidates will be used to track the minimum number of remaining candidates,
    #and min_row and min_col will store the row and column coordinates of the cell with
    #the minimum candidates.
    min_candidates = N + 1
    min_row, min_col = -1, -1
    
    #Iterate over nested loop
    for i in range(N):
        for j in range(N):
            #Checks for an empty cell
            if grid[i][j] == 0:
                
                #Calculates candidates for the cell
                candidates = set(range(1, N + 1)) - set(grid[i]) - set(grid[r][j] for r in range(N))
                
                #Checks the length of the candidates and min_cand
                if len(candidates) < min_candidates:
                    
                    #Updates 'min_cand','min_row','min_col'
                    min_candidates = len(candidates)
                    min_row, min_col = i, j
                    
    #Returns the row and column coordinates of the cell with the fewest remaining candidates.
    return min_row, min_col

#Solve Sudoku using Cross-Hatching and Backtracking
def solve_sudoku(grid):
    #stores row and col where empty cells are left
    row, col = find_empty_cell(grid)
    
    #If there is no empty cell left
    if row == -1:
        return True  # All cells are filled
    
    #Iterate over values to fill the cell
    for num in range(1, N + 1):
        #If num can be placed in that particular cell
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            
            #If success, the return 
            if solve_sudoku(grid):
                return True
            
            #If not, assign value of the cell to 0, then iterate over next value
            grid[row][col] = 0  # Backtrack
            
    #This is used to trigger backtracking 
    return False

#Sudoku grid
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
if solve_sudoku(grid):
    #Print the Grid
    print_grid(grid)
#If no sultion exists
else:
    print("No solution exists.")
