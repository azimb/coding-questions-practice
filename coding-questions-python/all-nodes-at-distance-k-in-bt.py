'''
LC: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
YouTube: https://www.youtube.com/watch?v=nPtARJ2cYrg
Complexity Analysis: O(n) time and space complexity
'''

from collections import deque

def distanceK(self, root, target, K):
  if not root: return []

  parents_mapping = {}
  self.map_parent(root, None, parents_mapping)

  seen = set([target])
  queue = deque([target])
  level = 0

  while queue:
    if level == K: 
      nodes_at_distance_k = []
      for node in queue: nodes_at_distance_k.append(node.val)
      return nodes_at_distance_k

    for i in range(len(queue)):
      node = queue.popleft()
      self.check_and_add(node.left, seen, queue)
      self.check_and_add(node.right, seen, queue)
      self.check_and_add(parents_mapping[node], seen, queue)

      level += 1

  return []

def map_parent(self, node, parent, parents_mapping):
  if node == None: return
  parents_mapping[node] = parent
  self.map_parent(node.left, node, parents_mapping)
  self.map_parent(node.right, node, parents_mapping)


def check_and_add(self, node, seen, queue):
  if not node: return
  if node not in seen:
    seen.add(node)
    queue.append(node)

# all leetcode tests pass
