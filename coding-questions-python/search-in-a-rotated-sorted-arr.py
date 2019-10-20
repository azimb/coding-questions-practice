'''
LC: https://leetcode.com/problems/search-in-rotated-sorted-array/
Approach:
  - variation of the binary search
  - idea is to discard half of the seach space by checking:
      a) which half is sorted
      b) if the target lies in the sorted half

Complexity analysis: O(log n) time and O(1) space complexity
'''

def search_in_rotated_sorted(nums):
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = left + (right-left)/2
    # found the target
    if nums[mid] == target: return mid

    # right half is sorted
    elif nums[mid] < nums[right]:
      # it's in right half
      if nums[mid] < target <= nums[right]: left = mid + 1
      # it's not in right half, so check left half
      else: right = mid - 1

    # left half is sorted
    else: # nums[mid] > nums[right]
      # it's in left half
      if nums[left] <= target < nums[mid]: right = mid - 1
      # it's not in the left half, so check right half
      else: left = mid + 1

  # not found
  return -1

# all leetcode tests pass as of 19th Oct 2019
