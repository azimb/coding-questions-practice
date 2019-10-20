'''
LC: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Similar to: https://github.com/baghadiya/coding-questions-practice/blob/master/coding-questions-python/search-in-a-rotated-sorted-arr.py
(only difference: this problem allows duplicates)

Approach:
  - the only place where search-in-a-rotated-sorted-arr fails is when we have a case like this: [num, x, x, x, num, x, x, x, num]
                                                                                                                ^     
                                                                                                               mid
  (that is, nums[mid] == nums[start])
  - this means:
    * the first half could be out of order (i.e. NOT in the ascending order) and we have to deal this case separately
    * in that case, it is guaranteed that nums[right] also equals to nums[mid]
    * so what we can do is to check if nums[mid]== nums[left] == nums[right] before the original logic
    * and if so, we can move left and right both towards the middle by 1
    
Complexity analysis:
  - O(log n) avg case, and O(n) worst case time complexity
  - O(1) space complexity
   
Inspired by: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28218/My-8ms-C%2B%2B-solution-(o(logn)-on-average-o(n)-worst-case)
'''

def search(self, nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = left + (right-left)/2
    # found the target
    if nums[mid] == target: return True

    # trick -- the only special case -- check if nums[mid] is the same as num[left]
    if nums[mid] == nums[right] == nums[left]: left += 1; right -= 1

    elif nums[mid] <= nums[right]: # right half is sorted
      # it maybe in right half
      if nums[mid] < target <= nums[right]: left = mid + 1
      # if not, try left half
      else: right = mid - 1

    else: # left half is sorted
      # it maybe in left half
      if nums[left] <= target < nums[mid]: right = mid - 1
      #if not, try right half
      else: left = mid + 1

  # not found
  return False

# all leetcode tests pass as of 20th Oct 2019
