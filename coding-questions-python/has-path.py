'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all
the values along the path equals the given sum.
Note: A leaf is a node with no children.

Approach:
    - if root is leaf node (no left/right child), then check if the sum is the same as it's value
    - if root's left child is None, try check if right child has a root-to-leaf path that adds up to (sum - val)
    - if root's right child is None, try check if left child has a root-to-leaf path that adds up to (sum - val)
    - otherwise, check if the right or thr left child has a root-to-leaf path that adds up to (sum - val)

Time complexity:
    - we will visit each node once
    - so the time complexity is O(N)
    (where N is the total # of nodes in the tree)

Space complexity:
    - TODO: understand this
'''

def hasPathSum(root):
    # edge case -- must never be true unless root is None
    if not root: return False

    # base case -- leaf node
    if root.left is None and root.right is None:
        return root.val == sum

    # if left subtree is None, recurse for right subtree
    if root.left is None:
        return hasPathSum(root.right, sum - root.val)

    # if right subtree is None, recurse for left subtree
    if root.right is None:
        return hasPathSum(root.left, sum - root.val)

    # check if either of the left or right subtree has a root-to-leaf path such that it's equal to sum - root's val
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)