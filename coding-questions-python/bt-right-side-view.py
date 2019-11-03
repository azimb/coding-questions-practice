'''
Binary Tree Right Side View
LC: https://leetcode.com/problems/binary-tree-right-side-view/

Approach:
  - it's a very simple approach
  - do a binary tree level order traversal, but only add the last node in the level to the output
  - how do we know which node is last in level?
    * once we finish travering a level, `node` points to the last popped node
    and this last popped node is the last node of the level we just looked at

Time and space complexity:
  - we are processing each node once so the time complexity is O(N)
  - space complexity is also O(N) due to the queue and the max recursion depth in worst case
'''

from collections import deque
def right_side_view(root):

  # edge case - empty tree
  if not root: return []

  # output will store the right most nodes of each level
  output = []
  # queue is used to perform a BFS / tarversal in a level order fashion
  queue = deque([root])
  
  while queue:
    # process level
    for i in range(len(queue)):
      node = queue.popleft()
      # add children to queue to process them in the next level
      if node.left: queue.append(node.left)
      if node.right: queue.append(node.right)
      
    # the last popped node will be the last node of the level we just processed
    output.append(node.val)

  return output
  
# all leetcode tests pass as of 3rd Nov 2019
