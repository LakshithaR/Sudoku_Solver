#  SUDOKU SOLVER
***Welcome to the Sudoku Solver README, where we explore different techniques to tackle the challenging world of Sudoku Puzzles.***
<br><br>
Sudoku is a popular number puzzle game that involves filling a 9x9 grid with digits from 1 to 9, such that each column, each row, and each of the nine 3x3 subgrids contains all of the digits from 1 to 9 without repetition. Solving Sudoku puzzles involves using various techniques to deduce the correct numbers for each cell in the grid.
<br>   
This repository contains implementations of three different approaches to solving Sudoku puzzles:
  1. Naive Approach
  2. Backtracking
  3. Cross-Hatching with Backtracking
<br><br>

***1. NAIVE APPROACH***

The naive approach is to generate all possible configurations of numbers from 1 to 9 to fill the empty cells. Try every configuration one by one until the correct configuration is found, i.e. for every unassigned position fill the position with a number from 1 to 9. After filling all the unassigned positions check if the matrix is safe or not. If safe print else recurs for other cases.

**Time Complexity:** O(9(N*N)), For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)).

**Space Complexity:** O(N*N), To store the output array a matrix is needed.
<br><br><br>
***2. BACKTRACKING***

Like all other Backtracking problems, Sudoku can be solved by assigning numbers one by one to empty cells. Before assigning a number, check whether it is safe to assign. Check that the same number is not present in the current row, current column and current 3X3 subgrid. After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not. If the assignment doesn’t lead to a solution, then try the next number for the current empty cell. And if none of the number (1 to 9) leads to a solution, return false and print no solution exists.

**Time complexity:** O(9(N*N)), For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)).

**Space Complexity:** O(N*N), To store the output array a matrix is needed.
<br><br><br>
***3. CROSS-HATCHING WITH BACKTRACKING***

This method is an optimization of the above method 2. It runs 5X times faster than method 2. Like we used to fill sudoku by first identifying the element which is almost filled. It starts with identifying the row and column where the element should be placed. Picking the almost-filled elements first will give better pruning.

**Time complexity:** O(9^(n*n)), Due to the element that needs to fit in a cell will come earlier as we are filling almost filled elements first, it will help in less number of recursive calls.

**Auxiliary Space:** O(n*n), A graph of the remaining positions to be filled for the respected elements is created.
<br><br><br>
      While the naive approach is impractical for larger puzzles, both the Backtracking and Cross-Hatching with Backtracking approaches provide efficient solutions to Sudoku Puzzles. Cross-Hatching with Backtracking further enhances the backtracking method by leveraging logical strategies to prioritize placements and reduce the need for exhaustive backtracking.

It's important to note that Sudoku solving is NP-complete, meaning that no known algorithm guarantees a polynomial-time solution for all puzzles. The efficiency of these approaches depends on the specific puzzle and the techniques employed.
<br><br>
***Feel free to explore the implementations in this repository and try out the different solving methods for yourself!***
