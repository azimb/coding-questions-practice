'''
LC: https://leetcode.com/problems/search-a-2d-matrix/
YouTube: https://www.youtube.com/watch?v=FOa55B9Ikfg&list=PLiQ766zSC5jMZgWWdqy_6TpLivRGQaFD-&index=6
'''

def search_sorted_matrix_i(matrix, target):
    # corner case, matrix is empty
    if len(matrix) == 0: return False

    rows = len(matrix)
    cols = len(matrix[0])

    # left and right for the binary search on the imaginary 1D array
    start, end = 0, rows * cols - 1

    # regular binary search, but get the elems using it's x,y values
    # use the helper method to get x,y coordinates
    while start <= end:
        mid = start + (end - start) / 2
        cord = index_to_cord(matrix, mid)
        mid_elem = matrix[cord[0]][cord[1]]

        if mid_elem == target: return True  # found the target
        if mid_elem < target:
            start = mid + 1  # target is maybe in the right half
        else:
            end = mid - 1  # target is maybe in the left half

    # didn't find the target
    return False


# helper to get x,y values for given i index of an imaginary 1D array
def index_to_cord(self, matrix, i):
    cols = len(matrix[0])
    return (i / cols, i % cols)
