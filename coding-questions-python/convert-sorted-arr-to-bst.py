'''
LC: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''

def sortedArrayToBST(self, nums):
  if not nums: return None

  mid = 0 + ( 0 + (len(nums)-1))/2

  root = TreeNode(nums[mid])
  root.left = self.sortedArrayToBST(nums[:mid])
  root.right = self.sortedArrayToBST(nums[mid+1:])

  return root
  
# all leetcode tests pass as of 13th Nov 2019
