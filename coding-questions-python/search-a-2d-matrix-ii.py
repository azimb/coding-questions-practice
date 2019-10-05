'''
LC: https://leetcode.com/problems/search-a-2d-matrix-ii/
YouTube: https://www.youtube.com/watch?v=FOa55B9Ikfg&list=PLiQ766zSC5jMZgWWdqy_6TpLivRGQaFD-&index=6
'''

def search_sorted_matrix_ii(matrix, target):
    # corner case -- empty matrix
    if len(matrix) == 0: return False
        
    # start from the bottom left corner
    row, col = len(matrix) - 1, 0
        
    # keep going until the row / col is invalid
    while row >= 0 and col < len(matrix[0]):
        # element at the cur row,col in the matrix 
        current = matrix[row][col]
            
        # if elem is found, return true
        # otherwise, go right if the elem is smaller, or up if the elem is bigger than target
        if current == target: return True    
        if current < target: col += 1
        else: row -= 1
        
    # target wasn't found
    return False

# all leetcode tests pass
