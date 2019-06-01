'''
Given an image, how will you turn it by 90 degrees?

NOTE: a 2D list can be "nicely" printed using numpy
`import numpy as np`
`print(np.matrix(matrix))`
'''

def rotateMatrix(matrix):
    numOfRows = len(matrix)
    # edge case
    if numOfRows == 0:
        return matrix

    numOfColoumns = len(matrix[0])

    result = []

    for row in range(numOfColoumns):
        temp = []
        for column in range(numOfRows):
            temp.append(0)
        result.append(temp)

    for row in range(numOfRows):
        for column in range(numOfColoumns):
            result[column][numOfRows - row -1] = matrix[row][column]

    return result

# tests
import unittest

class TestRotateMatrix(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(rotateMatrix([ [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15] ]), [ [11,6,1],[12,7,2],[13,8,3], [14,9,4], [15,10,5] ])
        self.assertEqual(rotateMatrix([ [21,22,23],[24,25,26],[27,28,29], [30,31,32], [33,34,35] ]), [ [33,30,27,24,21], [34,31,28,25,22], [35,32,29,26,23] ])
        self.assertEqual(rotateMatrix([ [4,3],[2,1] ]), [ [2,4], [1,3] ])
        self.assertEqual(rotateMatrix([]), [])

unittest.main()
