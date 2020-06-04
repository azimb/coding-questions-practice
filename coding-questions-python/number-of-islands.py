'''
LC: https://leetcode.com/problems/number-of-islands/

Approach:
    - just drown every island, one of by one
    - search through the grid for an island
    * as soon as you encounter one, take a note of it and "drown the island"
    - the island cell and the adjacent cells are made water (or just noted visited) by essentially doing a dfs on the grid

Time complexity:
    - each cell can at most be visited 5 times (from 4 adjacent cells and in the nested for loop search)
    - so, the time complexity is O(M+N), where M = # of rows, and N = # of cols

Space complexity:
    - stack space will be used for recursion, and the stack will go linearly in proportion to the # of rows/cols
    - so, the space complexity is O(M+N)
'''


def numIslands(grid):
    islands = 0

    # look at each cell to find islands
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # part of island
            if grid[row][col] == '1':
                islands += 1
                remove_island(grid, row, col)

    return islands


# dfs helper to clear the island
def remove_island(self, grid, row, col):
    # helper to check if the cell index is valid or not
    def is_valid(row, col):
        return (0 <= row < len(grid)) and (0 <= col < len(grid[row]))

    # fell off the grid
    if not is_valid(row, col): return

    # not a part of the island
    if grid[row][col] == '0': return

    # "drown" the current cell, and then check adjacent cells
    grid[row][col] = '0'
    self.remove_island(grid, row - 1, col)  # go up
    self.remove_island(grid, row + 1, col)  # go down
    self.remove_island(grid, row, col - 1)  # go left
    self.remove_island(grid, row, col + 1)  # go right

# all leetcode tests pass as of June 4 2020
