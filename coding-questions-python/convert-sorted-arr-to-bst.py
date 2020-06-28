'''
LC: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Approach:
  - in each recursive call, we have a parition of the array to look at
  - the middle elem of this parition will be the root node of th sub-tree
  - it's left and right children will be constructed recursilvely using the left and right sub-paritions
  
Complexity analysis:
  - since each array elem is visited once, the time complexity is O(n)
  - since the recursive stack will be a most log(N) size at one point in time, the space complexity is O(log(n))
'''

def sortedArrayToBST(snums):
    if not nums: return
    return self.sorted_array_to_bst_helper(nums, 0, len(nums) - 1)

def sorted_array_to_bst_helper(nums, low, high):
    # base case -- no elements to look at in this subtree
    if low > high: return
    
    # elem appearing at the middle of the parition will be the root of this tree/subtree
    mid = low + (high - low) / 2
    node = TreeNode(nums[mid])
    # generate the left/right subtree recursively using the left/right sub-paritions of this partition
    node.left = self.sorted_array_to_bst_helper(nums, low, mid - 1)
    node.right = self.sorted_array_to_bst_helper(nums, mid + 1, high)

    # return the head of this tree/subtree once it's recursively constructed
    return node 
  
# all leetcode tests pass as of 8th June 2020
