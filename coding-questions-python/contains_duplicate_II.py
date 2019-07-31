'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Leetcode: https://leetcode.com/problems/contains-duplicate-ii/

Approach:
    - the idea is to iterate over the array and simltaneously maintain a hashmap to track each letter's _MOST RECENT_ index
    - on each iteration, check if num is in the map
        -- if it is, grab and the index and check if the current_index - grabbed_index is at most k
        -- if it is, return the True
        -- otherwise, replace the value of the num in the hashmap with the new index
        (why: say the current index is i and the grabbed index is j. Either i-j <= k or i=j k.
            If i-j <= k, then we return True. But if i-j > k, there is no index new_i that will give make new_i - j <= k.
            This is because i-j is already greater than k, and new_i is greater than i. So, new_i - j _HAS TO_ to be greater than k.

Complexities:
    - linear time and linear space complexity
'''

def containsNearbyDuplicates(nums, k):
    # edge case -- nums is None
    if nums is None: return False

    # hash map to store the most recent indices for each elem in the input array
    index_tracker = {}

    # iterating over all the elements (just once)
    for i in range(len(nums)):
        num = nums[i]
        # if the elem is in the hash map
        if num in index_tracker:
            # grab the it's value (or it's most recent index that we have encoutered)
            j = index_tracker[num]
            # check if the difference of the current index and the grabbed index is at most k
            if i - j <= k: return True

        # place the elem in the hashmap with it's index if a) it's not in the hashmap or b) it's most recent index is "too small"
        index_tracker[num] = i

    # haven't encountered two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    return False

# tests
import unittest
class TestCheckNumEquality(unittest.TestCase):

    def test_general_true_cases(self):
        self.assertTrue(containsNearbyDuplicates([1, 2, 3, 1], 3))
        self.assertTrue(containsNearbyDuplicates([7, 3, 1, 5, -3, -2, 0, 0, 0, 3, 9, 2, 5], 6))



    def test_general_false_cases(self):
        self.assertFalse(containsNearbyDuplicates([1, 2, 3, 1, 2, 3], 2))
        self.assertFalse(containsNearbyDuplicates([7, 1, 5, -3, -2, 0, 0, 0, 3, 9, 2, 5], 0))


    def test_edge_cases(self):
        self.assertFalse(containsNearbyDuplicates([7], 1))
        self.assertFalse(containsNearbyDuplicates([7], 0))

        self.assertFalse(containsNearbyDuplicates([], 5))
        self.assertFalse(containsNearbyDuplicates([], 0))

        self.assertFalse(containsNearbyDuplicates(None, 3))
        self.assertFalse(containsNearbyDuplicates(None, 0))

unittest.main()
