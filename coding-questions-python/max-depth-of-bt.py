'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Approach:
    - if reached leaf, return 0 (as the depth is 0 from here)
    - else return 1 + max of left child's depth and right child's depth
    - runtime: O(2^n) -- visiting each node in the tree
    - space complexity: O(n) -- maximum recursion depth
'''

def max_depth(root):
    if root is None: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))