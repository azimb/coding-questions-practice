'''
LC: https://leetcode.com/problems/symmetric-tree/

Approach:
    - tree is symmetric when both it's left and right children are mirror
    - two tree are mirror if:
        a) they have the same value
        b) t1's left child is the mirror of t2'right child and t1'right child is a mirror of t2's left child

Time and space complexities are O(N) and O(H).
'''
def isSymmetric(self, root):
    # base case -- null tree/node is symmetric
    if not root: return True
    return are_mirror(root.left, root.right)


def are_mirror(self, tree_one, tree_two):
    # if both trees are null, they are mirror
    if not tree_one and not tree_two: return True

    # reached here, that means either/both of them are not null
    # if one of them is null, then they are not mirror so return false
    if not tree_one or not tree_two: return False
    if tree_one.val != tree_two.val: return False

    # t1's left child must be a mirror of t2'right, and vice versa
    return self.are_mirror(tree_one.left, tree_two.right) and self.are_mirror(tree_one.right, tree_two.left)

# all leetcode tests pass
