'''
LC: https://leetcode.com/problems/maximal-square/
Approach:
  - dynamic programming
  - for each cell, consider it the bottom right cell of a 2*2 matrix
  x   x
  x  cell
  * if 0, max size square including this cell is 0
  * if 1, max size square including this cell is 1 + min(solution for cell above, cell left, cell top left) 
Complexity analysis: O(mn) time and space complexity
'''

def maximalSquare(self, matrix):
  if len(matrix) == 0: return 0 # corner case
  dp = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))] # 2D array/cache
  max_square = 0 # variable to track the max square side len

  for i in range(len(dp)):
    for j in range(len(dp[i])):
      if matrix[i][j] == "1": # possible to make square of 1s, only if cell contains 1
        dp[i][j] = 1 + min (self.subprob(dp,i-1,j), self.subprob(dp, i, j-1), self.subprob(dp, i-1, j-1)) # get the solution to the subproblems for top, left, and top-left
        max_square = max(max_square, dp[i][j]) # update max if necessary

  return max_square**2 # we have the len of max square, so # of 1s will be len*2
    
def subprob(self, dp, i, j):
  if i >= len(dp) or j >= len(dp[i]): return 0 # list index out of range
  return dp[i][j] # get subproblem solution if indices are valid
  
  # all leetcode tests pass as of 19th Oct 2019
