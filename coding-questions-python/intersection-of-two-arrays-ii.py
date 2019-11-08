'''
LC: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Follow up for: https://github.com/baghadiya/coding-questions-practice/blob/master/coding-questions-python/intersection-of-two-arrays-i.py

Approach:
  - the idea is very similar to intersection-of-two-arrays-i
  - but for this question, the each element in the result should appear as many times as it shows in both arrays
  - so, instead of a hashset, we will use a hashmap and store the elements' frequencies
  
  - instead of removing the intersection elem from the seach_map, we will decrement it's frequency
  
Note: create a map for the smaller array to reduce the amount of space used

Time and space complexity:
  - same as the previous question
  - O(M+N) time and O(M) space where M = length of the smaller list and N = len of the other list
'''

def intersect(self, nums1, nums2):
  if len(nums2) < len(nums1): nums1, nums2 = nums2, nums1
  output = []
  nums1_map = Counter(nums1)
  for num in nums2:
    if num in nums1_map:
      output.append(num)
      nums1_map[num] -= 1
      if nums1_map[num] == 0: del nums1_map[num]
  return output
  
# all leetcode tests pass as of 7th Nov 2019
