'''
User defined (singly) linked list none class.
Each node stores a value, and a pointer to next (node).

Sample usage:
```
second = LinkedListNode(5, None)
head = LinkedListNode(2, second)
```
'''

class LinkedListNode:
    def __init__(self, val, next):
        self.val, self.next = val, next

    def __eq__(self, other):
        head = self
        while head and other:
            if head.val != other.val:
                return False
            head, other = head.next, other.next
        return head is None and other is None

import unittest
class TestLinkedListEq(unittest.TestCase):
    def test_addition(self):
        first_three = LinkedListNode(-7, None)
        first_two = LinkedListNode(0, first_three)
        first_one = LinkedListNode(4, first_two)

        second_two = LinkedListNode(0, None)
        second_one = LinkedListNode(4, second_two)

        third_two = LinkedListNode(-2, None)
        third_one = LinkedListNode(7, third_two)

        fourth_two = LinkedListNode(-2, None)
        fourth_one = LinkedListNode(7, fourth_two)

        fifth_one = (31, None)
        sixth_one = (-20, None)
        seventh_one = (31, None)

        self.assertEqual(third_one == fourth_one, True) # general case for True with same len
        self.assertEqual(second_one == third_one, False)  # general case for False with same len
        self.assertEqual(first_one == second_one, False) # case for False due to extra elements
        self.assertEqual(fifth_one == seventh_one, True) # case for True with singletons
        self.assertEqual(fifth_one == sixth_one, False)  # case for False with singletons
        self.assertEqual(sixth_one == None, False)  # case for False with singleton and None
        self.assertEqual(None == None, True) # case for True with Nones

unittest.main()