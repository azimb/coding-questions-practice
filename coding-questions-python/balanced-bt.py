'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the depth of the two subtrees of every node never differ by more than 1
'''
def isBalanced(root):
    if root is None:
        return True

    return abs(getMaxDepth(root.left) - getMaxDepth(root.right)) <= 1 and (
                isBalanced(root.left) and isBalanced(root.right))

def getMaxDepth(root):
    if root is None:
        return 0

    return 1 + max(getMaxDepth(root.left), getMaxDepth(root.right))