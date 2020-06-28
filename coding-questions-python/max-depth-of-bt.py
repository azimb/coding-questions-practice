'''
LC: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Approach:
    - simple recursive DFS
    - for each node, it's max depth is 1 + max ( depth of left child, depth of right child )
    - base case is a null node, with depth 0

Complexity analysis:
    - we will visit each node exact once
    - so the time complexity is O(n)

    - we will use O(H) stack space, where H = height of the tree
    - O(log n) in base case, and O(n) if the tree is skewed
    - so, the space complexity is O(H)
'''


def max_depth_of_bt(root):
    # base case -- the depth of a null node is 0
    if not root: return 0
    # max depth of the tree rooted at this node is 1 + the max depth from one of the children
    return 1 + max(max_depth_of_bt(root.left), max_depth_of_bt(root.right))

# all leetcode tests pass as of June 27 2020
