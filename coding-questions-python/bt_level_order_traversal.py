'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/

Approach:
    - we are going to nodes of keep eah tree level in a queue
    - in Python, a deque can be used to implement a queue

    - for each level:
        * pop the nodes from the queue
        * add them to a list
        * add this list to the ouput_list
        * and add their children to the queue

Time complexity:
    - each node is processed exactly once
    - so, the time complexity is O(n) or linear

Space complexity:
    - #FIXME: not sure if this is correct
    - using extra space for the queue (and also the output array, but do we count the space used for the return list?)
    - space complexity is O(n) or linear #TODO: verify this
'''

from collections import deque

def bt_level_order_traversal(root):
    # corner case to handle null input
    # if not root: return []

    # start with a queue that contains the root
    queue = deque([root])
    output = []

    # keep going until all the nodes are looked at
    while len(queue) > 0:
        # this list will store all the nodes in the current level
        current_level = [] # loop x times, where x is the len of the current level
        for i in range(len(queue)):
            node = queue.popleft() # get the first elem from the queue, this is the same as list.pop(0)
            current_level.append(node.val)

            # append the left and right subtrees to the queue
            if node.left: queue.append(node.left)
            if node.right:queue.append(node.right)

        # current level has been looked at, append it to the output array
        output.append(current_level)

    return output

# all leetcode tests pass