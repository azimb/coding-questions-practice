'''
LC: https://leetcode.com/problems/delete-node-in-a-linked-list/

Approach:
    - the usual way of deleting a node node from a linked list is to modify the next pointer
    of the node before it, to point to the node after it
    - since we do not have access to the node before the one we want to delete, we have to replace
    the value of the node we want to delete with the value in the node after it, and then delete the node after it

Complexity analysis:
    - O(1) time and space complexity
'''


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

# all leetcode tests pass as of May 1st 2020
