'''
LC: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Pattern:
  (may not be the most optimal, time complexity analysis pending)
  - for root, grab right and place it as the right child of the right most node in the root's left subtree
  - do this for root's right
  (and keep doing this until root is None)
  
Complexity analysis: # TODO
'''
def flatten(self, root):
  node = root
  while node:
    if node.left:
      cur = node.left
      while cur.right: cur = cur.right
      cur.right = node.right

      node.right = node.left
      node.left = None

    node = node.right
    
# all leetcode tests pass as of 
