'''
LC: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
YouTube: https://www.youtube.com/watch?v=suj1ro8TIVY
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

  def serialize(self, root):
    if not root: return "X,"
    left = self.serialize(root.left)
    right = self.serialize(root.right)
    return str(root.val) + "," + left + right


  def deserialize(self, data):
    queue = deque([])
    data_list = data.split(",")
    for elem in data_list: queue.append(elem)
    return self.deserialize_helper(queue)

  def deserialize_helper(self, nodes_remaining):
    value = nodes_remaining.popleft()
    if value == "X": return None
    new_node = TreeNode(value)
    new_node.left = self.deserialize_helper(nodes_remaining)
    new_node.right = self.deserialize_helper(nodes_remaining)
    return new_node
        
# all leetcode tests pass as of 25th Oct 2019
