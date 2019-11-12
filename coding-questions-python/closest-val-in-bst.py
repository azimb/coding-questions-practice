'''
Closest Binary Search Tree Value (Premium)

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
Note:
  - Given target value is a floating point.
  - You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:
Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

Approach:
  - as this is a binary search tree, we will perform a binary search
  - and for each node we visit, we will make it the closest node if it's closer to the target than the current closest node
  
Time and space complexity:
  - O(H) time and O(1) space complexity
'''

def closestValue(self, root, target):
  # closest will track the closest value to the target
  # val is a helper variable
  closest = val = root.val
  
  # binary search
  while root:
      val = root.val
      # updare closest if cur node's val is closer to target than current closest
      if abs(val-target) < abs(closest-target): closest = val
      # go left or right -- traditional binary search
      root = root.left if target < val else root.right

  # closest holds the closest node value to targer
  return closest
  
# all leetcode tests pass as of 12th Nov 2019
