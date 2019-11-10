'''
LC: https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Approach:
  - standard BFS level order traversal
  - whenever you see a null node, make sure it's the last null node
  (by looping through the queue and making sure no null nodes are present)
  - a null node can be represented by TreeNode("#") for this problem
  
- O(N) time and space complexity- for detailed explanation refer to: 
  https://github.com/baghadiya/coding-questions-practice/blob/master/time-complexity-graph-traversal.md
'''

def isCompleteTree(self, root):
  if not root: return True

  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node.val == "#": # discovered null node
      while queue: # verify no non-null nodes appear after
        node = queue.popleft()
        if node.val != "#": return False
      return True

    if node.left: queue.append(node.left)
    else: queue.append(TreeNode("#")) # null node

    if node.right: queue.append(node.right)
    else: queue.append(TreeNode("#")) # null node

  # verified all the nodes
  return True
        
# all leetcode tests pass as of 10th Nov 2019
