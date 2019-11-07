'''
LC: https://leetcode.com/problems/diameter-of-binary-tree/
Approach:
  - the idea is that for every node, length of longest path that passes through it is
    MaxDepth of its left subtree + MaxDepth of its right subtree.
  - for each node, find the longest path that passes through it, and update the record of longest_path if required
  
Time and space complexity analysis:
  - we visit each node once, so the time complexity is O(N)
  - recursion can lead to a stack space of O(H), where H = log n in best case and N in worst case
'''

def diameterOfBinaryTree(root):
  # passing diameter by reference, that's why wrapped in a list
  diameter = [0]
  # regualr max_depth recursive approach, but diameter will be updated whenever necessary
  max_depth(root, diameter)
  # grab the diameter from the wrapper
  return diameter[0]

def max_depth(root, diameter):
  # base case, root is None - so depth is 0
  if not root: return 0
  # get the depth of left subtree
  left_depth = max_depth(root.left, diameter)
  # get the depth of right subtree
  right_depth =  max_depth(root.right,diameter)
  # diamater is the sum of max_depth of left and right subtree
  diameter[0] = max(diameter[0], left_depth + right_depth)
  # get the max depth by getting the max depth of children and adding 1 to it
  return 1 + max(left_depth,right_depth)
  
# all leetcode tests pass as of 7th November 2019
