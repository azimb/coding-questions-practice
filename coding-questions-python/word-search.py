'''
LC: https://leetcode.com/problems/word-search/
Approach:
  - usual visit+dfs for each cell of the matrix
  - if first word[0] matches with cur board char,
    look for word[1:][0] in the cell above, below, left, or right
  - repeat

Complexity analysis: O(mn * 4s) time complexity, O(1) space complexity
# TODO: confirm
'''

def exist(self, board, word):
  for row in range(len(board)):
    for col in range(len(board[row])):
      # can we find the word at this index?
      if self.dfs(board, word, row, col): return True 
  # word not found
  return False
    
    
def dfs(self, board, word, row, col):
  if len(word) == 0: return True # all letters of the word matched
  if not self.cell_valid(board, row, col): return False # invalid cell
  if word[0] != board[row][col]: return False # board char doesn't match with the char from the word

  temp = board[row][col] # store the original to be used later
  
  board[row][col]  = "#" # mark this cell as visited

  ans = self.dfs(board, word[1:], row+1, col) or self.dfs(board, word[1:], row, col+1) or self.dfs(board, word[1:], row-1, col) or self.dfs(board, word[1:], row, col-1) # perform a dfs on left, right, up, and down cell

  board[row][col]  = temp # restore the orig value of the cell

  return ans # this will be true if either of the 4 cells returned True

def cell_valid(self, board, row, col):
  return row >= 0 and row < len(board) and col >= 0 and col < (len(board[row]))

# all leetcode tests pass as of 20th Oct 2019
