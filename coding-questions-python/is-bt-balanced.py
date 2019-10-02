'''
LC: https://leetcode.com/problems/balanced-binary-tree/
YouTube: https://www.youtube.com/watch?v=LU4fGD-fgJQ&t=648s

A recursive but a bottom up approach (the regular recursive top down cause O(n^2) runtime).
Drill down to the leaf node, and move up.
For each node, the tree is balanced rooted at that node if:
    a) left and right subtrees are balanced
    b) abs (left.height - right.height) > 1

Whenever we see a node (while going top to bottom) that is not balanced, return false right away
    which means we don't have to check all the remaining nodes.

As usual, time complexity is O(N) and space complexity is O(H)
'''

def isBalanced(self, root):
    return self.balance_status_with_height(root)[0]


def balance_status_with_height(self, node):
    # base case
    if not node: return (True, -1)

    # check left tree is balanced
    left = self.balance_status_with_height(node.left)
    if left[0] == False: return left

    # check right tree is balanced
    right = self.balance_status_with_height(node.right)
    if right[0] == False: return right

    # if both are balanced, use their heights to find if the tree rooted at the cur node is balanced
    is_balanced = abs(left[1] - right[1]) <= 1
    height = 1 + max(left[1], right[1])

    return (is_balanced, height)

# all leetcode tests pass
