'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Leetcode: https://leetcode.com/problems/two-sum/

Approach:
    - very simple one pass hash-map approach
    - for each elem, check if we have already "seen" the complement of the elem before
    - these "seen" elems and their indices are stored in a hash map

    - if the complement exists, we have found a solution
    - if it doesn't, store the elem with it's index so it can be used as some other elem's complement

Time complexity:
    - one pass
    - O(N) or linear

Space complexity:
    - storing at most all the elems of the nums array
    - O(N) or linear
'''

def two_sum(nums, target):
    # this hash-map will store the elem-index pair
    index_tracker = {}

    for i in range(len(nums)):
        # have we already seen the complement of the current elem
        look_for_number = target - nums[i]
        if look_for_number in index_tracker:
            return [index_tracker[look_for_number], i]
        # if complement doesn't exist. store the cur elem and it's index for future use
        index_tracker[nums[i]] = i

# tests
# assuming that there _exists exactly one solution_
import unittest
class TestTwoSum(unittest.TestCase):
    def test_general_success_cases(self):
        self.assertEqual(two_sum([4,7,1,-3,5,8,6], 3), [3,6])

    def test_only_two_elements_case(self):
        self.assertEqual(two_sum([4,7], 11), [0,1])

    def test_zero_case(self):
        self.assertEqual(two_sum([0,6,3,-9,2,-1,-11,7], 7), [0,7])

unittest.main()