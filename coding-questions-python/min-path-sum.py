'''
LC: https://leetcode.com/problems/minimum-path-sum/

Top down dp approach with the help of a 2D array cache
Similart to: https://github.com/baghadiya/coding-questions-practice/blob/master/coding-questions-python/unique-paths-i.py
O(mn) time and space complexity
# TODO: more efficient with 1D cache 
'''

def minPathSum(grid):
  return min_path_sum_recursive(grid, 0, 0, [[-1 for x in range(len(grid[0]))] for y in range(len(grid))])


def min_path_sum_recursive(grid, row, col, cache):
  if not is_valid(grid, row, col): return sys.maxsize
  if is_at_end(grid, row, col): return grid[row][col]

  if cache[row][col] != -1: return cache[row][col]

  ans = grid[row][col] + min ( min_path_sum_recursive(grid, row+1, col, cache), min_path_sum_recursive(grid, row, col+1, cache) )
  cache[row][col] = ans
  return ans


def is_valid(grid, row, col):
  return row < len(grid) and col < len(grid[row])

def is_at_end(grid, row, col):
  return row == len(grid) - 1 and col == len(grid[row])-1
  
# all leetcode tests pass as of 20th Oct 2019
