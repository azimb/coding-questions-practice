'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
    corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Approach:
    - this problem can be approached recursively
    - as the robot can only go either right or down, the number of paths for the robot to go from start to end are:
        (number of ways for the robot to go from start+right to end)
                                    +
        (number of ways for the robot to go from start+down to end)

    - if a  recursion tree is drawn for this problem, you can notice that several subproblems are being computed
        multiple times
    - this is unnecessary work, and can be omitted to improve efficiency / make our algo more optimal

    - idea is to use a 2d array as a memo to store the already computed result to go from a certain row, col to the end
        so that the result of this sub-problem can be reused later for other subproblems

Time complexity:
    - with the help of the 2d array, we make sure that we compute the result only for nm cells
    - so, the time complexity is O(nm)

Space complexity:
    - the maximum depth of recursion is O(nm) #TODO: verify this
    - the size of the memo/2d array is also nm
    - so, the space complexity is O(nm)
'''

def unique_paths_i(cols, rows):
    # a memo as a 2d array; memo[row][col] = # of unique paths from row,col to end
    memo = [[0 for x in range(cols)] for y in range(rows)]

    return count_paths_from_cell(0, 0, memo)

def count_paths_from_cell(row, col, memo):
    # checkout for index out of range
    if not is_valid_cell(row, col, memo): return 0
    # check if we have reached the end / desired destination
    if is_at_end(row, col, memo): return 1

    # the memo doesn't have the result for this row,col
    if memo[row][col] == 0:
        # recursively call to calculate recursive paths from the cell to the right, and the cell to the bottom
        # the addition of those paths is the num of unique paths from current cell
        result = count_paths_from_cell(row + 1, col, memo) + count_paths_from_cell(row, col + 1, memo)
        # store the result in the memo for future use
        memo[row][col] = result
        return result

    # memo already has the num of ways from row,col due to previous computations
    else:
        return memo[row][col]

def is_valid_cell(row, col, memo):
    if row >= len(memo) or col >= len(memo[0]): return False
    return True

def is_at_end(row, col, memo):
    if row == len(memo) - 1 and col == len(memo[0]) - 1: return True
    return False

# all leetcode tests pass
