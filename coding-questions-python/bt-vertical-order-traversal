'''
Binary Tree Vertical Order Traversal (Premium)
LC: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
YouTube: https://www.youtube.com/watch?v=PQKkr036wRc&t=54s

Approach:
  - each node is at a certain distance away from it's left
  ex:      1
          / \
         /   \
        2     3
             / \
            /   \
           4     5
  1 is 0 units away, 2 is -1 units away, 3 is +1 units away, 4 s 0 units away, and 5 is +2 units away
  
  - we can make buckets of nodes depending on their distances, and keep track of min,max distance on the fly
  - in the end, we will get the buckets from min distance all the way upto max distance
  
  - how to calculate distance
    * root's distance is 0
    * it's left child's distance is parent's distance - 1
    * it's right child's distance is parent's distance + 1
    
   - traversal
    * do a level order traversal (bfs + queue)
    * with each node, store it's distance, so childrens' distances can easily be calculated
    
Time and space complexity:
  - time complexity is O(N)
  - space complexity is O(longest level of binary tree)
  # TODO: verify
'''

from collections import defaultdict
from collections import deque
class Solution(object):
  def verticalOrder(self, root):
    if not root: return []

    buckets = defaultdict(list)
    min_max_distance = [sys.maxsize, -sys.maxsize]

    self.level_order_traversal(root, buckets, min_max_distance)

    vertically_ordered_nodes = []
    for i in range(min_max_distance[0], min_max_distance[1] + 1):
      if i in buckets: vertically_ordered_nodes.append(buckets[i])

    return vertically_ordered_nodes

  def level_order_traversal(self, root, buckets, min_max_distance):
    queue = deque([(root, 0)])
    
    while queue:
      for _ in range(len(queue)):
        pair = queue.popleft()
        node, distance = pair[0], pair[1]

        buckets[distance].append(node.val)

        min_max_distance[0] = min(min_max_distance[0], distance)
        min_max_distance[1] = max(min_max_distance[1], distance)

        if node.left: queue.append( (node.left, distance-1) )
        if node.right: queue.append( (node.right, distance+1) )

# all leetcode tests pass as of 9th Nov 2019
