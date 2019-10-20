'''
LC: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Approach:
  - variation of binary search
  - discard half of the search space by using the following trick
  a) if nums[mid] > nums[right] --> pivot is in the right half
  b) else pivot is in the right half
  * easy to find pivot when cur elem is bigger than right, or smaller than left
  
Time/Space complexity analysis: O(log n) time and O(1) space complexity
'''

def find_min_in_rotated_sorted_arr(nums):
  # edge case -- singleton
  if len(nums) == 1: return nums[0]
  
  # binary search
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = left + (right-left)/2

    if nums[mid] > nums[mid+1]: return nums[mid+1] # next elem is smallest
    elif nums[mid] < nums[mid-1]: return nums[mid] # cur elem is smallest
    elif nums[mid] > nums[right]: left = mid + 1 # search in right half
    else: right = mid - 1 # search in left half

  # unreachable
  return -1
  
# all leetcode tests pass as of 19th Oct 2019
