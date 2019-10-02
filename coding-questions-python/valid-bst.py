'''
LC: https://leetcode.com/problems/validate-binary-search-tree/
YouTube: https://www.youtube.com/watch?v=MILxfAbIhrE
'''

'''
Easy to check if node.left.val < node.val and node.right.val > node.val
But what if node.left subtree has some value later that is bigger that node.val? Or vice versa with node.right?

The idea is to "remember" what the values where, or, to have a constraint/range of values each node can be
The left subtree's root cannot have a value bigger that cur node's val
    and _it's_ left subtree's val can't be bigger than _it's_ value, and so on..
    
Time complexity is O(N) and space complexity is O(H)
'''
import sys
def isValidBST(self, root):
    # root can be any number, so range is INT_MIN - INT_MAX
    return self.is_valid_bst_recursive(root, [-1 * sys.maxsize, sys.maxsize])


def is_valid_bst_recursive(self, root, valid_range):
    # base case
    if not root: return True

    # if the node val is not within the range it's allowed to be, return false
    if root.val <= valid_range[0] or root.val >= valid_range[1]: return False

    # check if left is a valid bst, and give it a range that stops at cur node's val
    left = self.is_valid_bst_recursive(root.left, [valid_range[0], root.val])

    # vice versa
    right = self.is_valid_bst_recursive(root.right, [root.val, valid_range[1]])

    # return true iff left and right are valid bsts
    return left and right

# all leetcode tests pass
