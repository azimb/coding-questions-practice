'''
LC: https://leetcode.com/problems/binary-tree-inorder-traversal/
Approach: regular inorder traversal
Complexity analysis: O(N) time and space complexity
'''

def inorderTraversal(root):
  output = []
  inorder_recursive(root, output)
  return output

def inorder_recursive(root, output):
  if not root: return
  inorder_recursive(root.left, output)
  output.append(root.val)
  inorder_recursive(root.right, output)
  
# all leetcode tests pass as of 20th Oct 2019
