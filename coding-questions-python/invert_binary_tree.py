'''
Invert a binary tree. Examples are given on leetcode.
Essentially, for each tree, tree.left, tree.right = tree/.right, tree.left

Leetcode: https://leetcode.com/problems/invert-binary-tree/
'''

def invert_bt(root):
    # base case
    if root is None: return None

    # swap left and right sub trees
    root.left, root.right = root.right, root.left

    # recursive invert both left and right sub tree
    root.left = invert_bt(root.left)
    root.right = invert_bt(root.right)

    # return tree after inversion
    return root

# unit tests pening
# all leetcode tests pass
