'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Approach:
    - if both trees (roots) are None, return True as both are leafs
    - if their values are different (or one of them is None) return False
    - otherwise check that both trees have the same left subtree _and_ have the same right subtree
    - this is a recursive approach and we will visit each node
    - time complexity is O(2^N)
    - space complexity is O(N) as that will be the depth of the recursion
'''

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val: return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
