'''
3sum
LC: https://leetcode.com/problems/3sum/

Approach:
  - sort the array
  - for each elem, do the standard 2sum search for the remaining elems
  - to avoid duplicates, check that the cur_num is not the same as the num before
  - to avoid duplicates in 2sum search, once two numbers have been chosen, skip all nums that are same
  - to optimize, stop looking for more answers when cur_num > 0 as no nums > cur_num can sum together to make 0
  
Time and space complexities: O(N^2) and O(1)
'''

def threeSum(self, nums):
output = []
nums.sort()

for i in range(len(nums) - 2):
  # if num > 0, nums after num will be > 0. No way to add them to make sum 0
  if nums[i] > 0: break 
  # already looked at the solution for this number, skip duplicate
  if i > 0 and nums[i] == nums[i-1]: continue
  # standard two sum
  start = i+1; end = len(nums)-1; target = -1*nums[i]
  
  while start < end:
    sum = nums[start] + nums[end]

    if sum == target:
      output.append( [ nums[i], nums[start], nums[end]] )
      while start < end and nums[start] == nums[start+1]: start += 1
      while start < end and nums[end] == nums[end-1]: end -= 1
      start += 1; end -= 1

    elif sum > target: 
      # skip duplicates
      while start < end and nums[end] == nums[end-1]: end -= 1
      end -= 1

    else:
      # skip duplicates
      while start < end and nums[start] == nums[start+1]: start += 1
      start += 1

return output

# all leetcode tests pass as of 13th Oct 2019
