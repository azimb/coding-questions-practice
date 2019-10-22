'''
3sum closest
LC: https://leetcode.com/problems/3sum-closest/

Approach:
  - for each unique elem, do a standard 2sum search
  - for the 2sum search, increment left or decrement right to move closer to the target
  - for each sum, update global_sum if sum is closer to the target than global_sum is
  
Python lists are sorted by TimSort:
  - time complexity: O(N) best case and O(N logN) worst case
  - space complexity: O(1) best case and O(N) worst case
  
Time and space complexity: O(N^2) and O(N)
'''

def threeSumClosest(self, nums, target):     
  if len(nums) < 3: return 0
  global_sum = nums[0] + nums[1] + nums[2]

  nums.sort()

  for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i-1]: continue

      left, right = i+1, len(nums)-1
      while left < right:
          sum = nums[i] + nums[left] + nums[right]
          if sum == target: return sum
          elif sum < target: 
              while left < right and nums[left] == nums[left+1]: left +=1
              left += 1
          else: 
              while left < right and nums[right] == nums[right-1]: right -=1
              right -= 1

          if abs(sum-target) < abs(global_sum-target): global_sum = sum

  return global_sum
  
# all leetcode tests pass as of 13th Oct 2019
