'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Approach:
- maintain a 2D array that stores a number that each index
- the number at index i,j is the sum of the sub array starting at index i and ending at index j
- runtime complexity:
- space complexity: O(N^2) where N is the length of the input array

#TODO: discuss runtime complexity
'''

def maximum_subarray(input_arr):
    #init 2D array with 0 at all indices
    sum_tracker = init_list(input_arr)

    #set the values of sub arrays of length 1 and 2
    for i in range(len(input_arr)):
        sum_tracker[i][i] = input_arr[i]
        if i != len(input_arr) - 1:
            sum_tracker[i][i+1] = input_arr[i] + input_arr[i+1]

    #set the values of sub arrays of len length greater than 2
    k = 0
    for i in range(2, len(input_arr)):
        for j in range(len(input_arr) - i):
            k = i + j
            sum_tracker[j][k] = input_arr[j] + input_arr[k] + sum_tracker[j+1][k-1]

    #find the maximum sum from the calculated sums of each sub array
    max = 0
    for outer in sum_tracker:
        for inner in outer:
            if inner>max: max = inner
    #return sum_tracker
    return max

def init_list(input_arr):
    result = []
    for i in range(len(input_arr)):
        result.append([])
        for j in range(len(input_arr)):
            result[i].append(0)
    return result

#tests

import unittest
class TestMaximumSubarray(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(maximum_subarray([1,2,3,4,5]), 15)
        self.assertEqual(maximum_subarray([-5, -3, -1, 0, 1, 3, 5]), 9)
        self.assertEqual(maximum_subarray([2, -3, 0, 9, 6, -5, -2, -1, 0, 1, 2, 13]), 23)
        self.assertEqual(maximum_subarray([4]), 4)
        self.assertEqual(maximum_subarray([]), 0)
        
unittest.main()