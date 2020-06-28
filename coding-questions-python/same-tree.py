"""
LC: https://leetcode.com/problems/same-tree/

Approach:
    - simply use recursion, and depth first seacg
    - c if root_one and root_two are not None, and their values are equal.
    - if only one of them is None, the trees are NOT the same
    - if all checks are OK, recursive check if their left and right children are same

Complexity analysis:
    - since we will visit atmost each node once, we are doing linear amount of work
    - if one of the tree has less nodes, a base case check will fail after it's leaf node
    - so, we will see at most min(M, N) nodes #TODO: confirm
    - so, the time complexity is O(min(M,N)), where M,N = # of nodes in the two trees

    - DFS will use the stack space for recursion, and the stack will go linearly with the tree's height
    - so, the space complexity is O(min(H1, H2)), where H1, H2 = the heights of the two trees # TODO: confirm
"""


def is_same_tree(p, q):
    # base case -- both nodes are None, and two None trees/subtrees are "same"
    if not p and not q: return True
    # base case -- exactly one of the two nodes is None, so the trees are NOT "same"
    if not p or not q: return False
    # both trees are same if the two nodes are same, and their children are same
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# all leetcode tests pass as of June 27 2020
