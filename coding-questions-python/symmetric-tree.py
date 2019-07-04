'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

Approach:
    - a tree being symmetric is equivalent to it being a mirror image of itself
    - two trees are mirror images of each other if their values are same and
        (i) first tree's right child is the same as second tree's left child
        (ii) second tree's right child is the same as first tree's left child

    - if both trees are None, then they are mirrored
    - if just one of them is None, then they are not

Time complexity:
    - we will visit each node once in worst case
    - so time complexity is O(N)
      (where N is the total number of nodes in the tree)

Space complexity:
    - depth of recursion will be O(N)
    - so space complexity will be O(N)
    (where N is the total number of nodes in the tree)
    TODO: verify this
'''


def isSymmetric(root):

       return areMirror(root, root)

def areMirror(tree_one, tree_two):
        if not tree_one and not tree_two:
            return True

        elif not tree_one or not tree_two:
            return False

        else:
            return tree_one.val == tree_two.val and areMirror(tree_one.right, tree_two.left) and areMirror(tree_one.left, tree_two.right)