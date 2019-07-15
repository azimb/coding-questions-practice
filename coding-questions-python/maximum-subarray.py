'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Approach (discarded as it's too inefficient)
- maintain a 2D array that stores a number that each index
- the number at index i,j is the sum of the sub array starting at index i and ending at index j
- runtime complexity:
- space complexity: O(N^2) where N is the length of the input array

Optimized solution:
    - this problem can be solved in a linear time with the help for Kadane's algorithm
    (https://www.google.com/search?client=ubuntu&channel=fs&q=kadane%27s+algorithm&ie=utf-8&oe=utf-8)
    (https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
    - keep a track of max_so_far and global_max
    - max_so_far at index i will indicate the max sum of subarray ending at index i

    - for each elem, the max_so_far will be either the sum of max_so_far and the elem, or the elem itself
        based on whichever is higher
    - basically reset the max_so_far when adding the current elem doesn't help
    - since we want the maximum value subarray, if the  max_so_far is less than the current elem,
        then we might as well start the array with the current elem
    - once max_so_far exceeds the global_max, global total is set to running total

    - global total is used because max_so_far may reduce as we keep iterating
    - the idea is that starting at some indices is strictly worse than some indices before it

    - runtime complexity is O(N) and space complexity is O(1)
'''


def maximum_subarray(input_arr):
    if len(input_arr) == 0: return 0

    current_max = global_max = input_arr[0]
    for i in range(1, len(input_arr)):
        current_max = max(current_max + input_arr[i], input_arr[i])
        global_max = max(global_max, current_max)

    return global_max

#tests
import unittest
class TestMaximumSubarray(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(maximum_subarray([1,2,3,4,5]), 15)
        self.assertEqual(maximum_subarray([-5, -3, -1, 0, 1, 3, 5]), 9)
        self.assertEqual(maximum_subarray([2, -3, 0, 9, 6, -5, -2, -1, 0, 1, 2, 13]), 23)
        self.assertEqual(maximum_subarray([-4]), -4)
        self.assertEqual(maximum_subarray([-2, -1]), -1)
        self.assertEqual(maximum_subarray([]), 0)

unittest.main()

# all leetcode tests pass
# Runtime: 52 ms, faster than 70.59% of Python online submissions for Maximum Subarray