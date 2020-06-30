'''
LC: https://leetcode.com/problems/max-area-of-island/

Very similar to number of islands
https://github.com/baghadiya/coding-questions-practice/blob/master/coding-questions-python/number-of-islands.py

Approach:
    - use DFS to drown every island, one by one
    - for each island, calcuate the # of 1s -- this is equal to the island's area

Complexity analysis:
    - time and space complexity are linear, or O(M+N) where M = # of rows and N = # of columns
'''


def maxAreaOfIsland(grid):
    max_area = 0
    # look at each cell to find islands
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # found an island
            if grid[row][col] == 1:
                max_area = max(max_area, get_area_and_drown_island(grid, row, col))

    return max_area


def get_area_and_drown_island(grid, row, col):
    # base case -- not a part of the island, or fell off the grid
    if row < 0 or row == len(grid) or col < 0 or col == len(grid[row]) or grid[row][col] == 0: return 0

    # is an island, and area >= 1
    area = 1

    # drown this piece of island
    grid[row][col] = 0

    area += get_area_and_drown_island(grid, row + 1, col)  # down
    area += get_area_and_drown_island(grid, row - 1, col)  # up
    area += get_area_and_drown_island(grid, row, col + 1)  # right
    area += get_area_and_drown_island(grid, row, col - 1)  # left

    return area

# all leetcode tests pass as of June 29 2020
