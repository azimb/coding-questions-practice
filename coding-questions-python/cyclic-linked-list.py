'''
LC: https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
'''

'''
Initial approach:
If the linked list has unique values, we can use a set to keep a track of "seen" values.
Each time we see a new value, we first check in the "seen" set. If we haven't, we add to the set and move on.
And if we have, we return true. If we "fall out" of list, we return false.

Limitations:
- list must have unique elements
- O(N) space required

Note: instead of storing the node's val, we can store it's reference in the hashset. 
This means, we don't need to worry about duplicate node values anymore, every node will have it's own reference.
However, we are still using O(N) space, and this can be optimized.

Updated algorithm:
Use a two pointer appproach -- one fast (moves by 2 steps) and one slow (moves by a single step).
Keep moving them until fast falls out of the list. If before fast "falls off" from the list and 
fast and slow meet, that indicates a cycle so immediately return true.
'''

class LinkedListNode:
    def __init__(self, val, next):
        self.val, self.next = val, next

def checkCyclic(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True

    return False

# testing

import unittest
class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_addition(self):
        fourth = LinkedListNode(9, None)
        third = LinkedListNode(6, fourth)
        second = LinkedListNode(5, third)
        head = LinkedListNode(2, second)
        self.assertEqual(checkCyclic(head), False)

        fourth.next = second
        self.assertEqual(checkCyclic(head), True)

        head = LinkedListNode(2, None)
        self.assertEqual(checkCyclic(head), False)

        self.assertEqual(checkCyclic(None), False)

        singleton = LinkedListNode(31, None)
        singleton.next = singleton
        self.assertEqual(checkCyclic(singleton), True)

unittest.main()
