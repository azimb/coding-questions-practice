'''
LC: https://leetcode.com/problems/intersection-of-two-arrays/

Approach:
  - we can look at each number in the smaller array if it's present in the longer array
  - we can use a set to allow fast lookups
  - to trick to handle duplicates is that:
    * once you append an intersection, delete it from the search set
    * this will make sure that you don't match the same elem more than once
    
Time and space complexity:
  - we will visit each elem in both arrays once, so the time complexity is O(M+N)
  - we will make a hashset for one of the arrays, so the space complexity is O(M)
'''

def intersection(self, nums1, nums2):
  # all unique elements of nums1, along with O(1) lookup
  nums1_set = set(nums1)

  result = []
  '''
  For each num in nums2, if there is an intersection, append it to the output
  Also remove it from the set of nums1 because you don't want the duplicates to be appended to the output.
  '''
  for num in nums2:
    if num in nums1_set:
      result.append(num)
      nums1_set.remove(num)
  return result
  
# all leetcode tests pass as of 7th Nov 2019
