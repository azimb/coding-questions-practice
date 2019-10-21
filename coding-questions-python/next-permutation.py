'''
LC: https://leetcode.com/problems/next-permutation/
YouTube: https://www.youtube.com/watch?v=quAS1iydq7U&t=201s

Approach:
  - there is a trick to this problem
  - refer to video: https://www.youtube.com/watch?v=quAS1iydq7U&t=201s

Trick:
  - from the end, for a decreasing sequence, no larger permutation is possible
  - the elem before this decreasing sequence has a next possible option, so we will mutate that
  - the next elem for this chosen elem will be the smallest elem bigger than this elem
  (and this will be found from the decreasing sequence that sits to the right)
  - next, we swap these two

  - now realize that the decreasing sequence is still decreasing, and no next perumtations are possible for it
  - however, we want the smallest permutation that can be formed by using the numbers only to the right
  - so, we need to place those numbers in the ascending order, and not descending
  - so, we reverse the numbers to the right

Complexity analysis: O(N) time and O(1) space complexity
'''
def nextPermutation(self, nums):
  # find the elem that sits to the left of a decreasing sequence
  index = len(nums) - 2
  while index >= 0 and nums[index] >= nums[index+1]: index -= 1

  # found a number such that sequence to it's right is a decreasing sequence
  if index >= 0:
    # find the elem that is the smallest larger number to the elem we are mutating
    swap_with = len(nums) - 1
    while swap_with >= 0 and nums[swap_with] <= nums[index]: swap_with -= 1
    # swap the elem with it's smallest bigger number
    nums[index], nums[swap_with] = nums[swap_with], nums[index]
    
  # index is negative, which means the entire sequence is decreasing
  # so, we need to reverse the whole array to get the next bigger permutation
  if index < 0: index = -1
  # reverse the decreasing sequence to make it ascending
  self.my_reverse(nums, index+1, len(nums)-1)

# helper function to reverse an array in place b/w the specified indices
def my_reverse(self, nums, start, end):
  while start < end:
    nums[start], nums[end] = nums[end], nums[start]
    start += 1; end -= 1

# all leetcode tests pass as of 21st Oct 2019
