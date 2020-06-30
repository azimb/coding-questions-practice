'''
LC: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Pattern:
  - for root, grab right and place it as the right child of the right most node in the root's left subtree
  - do this for root's right
  (and keep doing this until root is None)

Another solution at: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37010/Share-my-simple-NON-recursive-solution-O(1)-space-complexity!

Complexity analysis:
  - every node is visited by "node" exactly once and by "cur" at most once
  - runtime is proportional to the number of steps taken by "node" and "cur"
  - so, the runtime complexity is O(N)

  - not using any auxiliary space
  - so, the space complexity is O(1)

Refer to this to understand the time complexity better:
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37010/Share-my-simple-NON-recursive-solution-O(1)-space-complexity!/35137
'''


def flatten(root):
    node = root
    while node:
        # find current node's prenode that will link to current node's right subtree
        if node.left:
            cur = node.left
            while cur.right: cur = cur.right
            cur.right = node.right

            # replace the current node's right subtree by it's left subtree
            node.right = node.left
            node.left = None

        node = node.right

# all leetcode tests pass as of June 29 2020
