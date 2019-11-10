'''
LC: https://leetcode.com/problems/move-zeroes/

Approach:
  - move all the non-zero entries forward
  - fill the remaining array with 0s
  
Time and space complexity: linear time and constant space complexity
'''

def moveZeroes(self, nums):
  # this is the index where the next non-zero entry will go
  insert_position = 0
  
  # move all the non-zero entries forward
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[insert_position] = nums[i]
      insert_position += 1

  # after the last non-zero entry, fill the remaining array with 0s
  while insert_position < len(nums):
    nums[insert_position] = 0
    insert_position += 1
      
# all leetcode tests pass as of 10th Nov 2019
