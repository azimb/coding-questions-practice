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

def merge_sorted(head_one, head_two):
    dummyNode = LinkedListNode(0, None)
    tail = dummyNode

    while True:
        if not head_one:
            tail.next = head_two
            break

        if not head_two:
            tail.next = head_one
            break

        if head_one.val <= head_two.val:
            tail.next = head_one
            tail = tail.next
            head_one = head_one.next
        else:
            tail.next = head_two
            tail = tail.next
            head_two = head_two.next

    return dummyNode.next

#utility method to convert a an array to a linked list
def array_to_linked_list(arr):
    if arr is None: return None
    current = None
    for i in range(len(arr)-1, -1, -1):
        new_node = LinkedListNode(arr[i], current)
        current = new_node
    return current

# tests
import unittest
class TestMergeLinkedLists(unittest.TestCase):
    def test_addition(self):
        linked_list_one = array_to_linked_list([1, 2, 3])
        linked_list_two = array_to_linked_list([4, 5, 6])
        result = array_to_linked_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted(linked_list_one, linked_list_two) == result, True)

        linked_list_one = array_to_linked_list([1, 3, 5])
        linked_list_two = array_to_linked_list([2, 4, 6])
        result = array_to_linked_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted(linked_list_one, linked_list_two) == result, True)


        linked_list_one = array_to_linked_list([7, 8])
        linked_list_two = array_to_linked_list([2, 3, 4, 5])
        result = array_to_linked_list([2,3,4,5,7,8])
        self.assertEqual(merge_sorted(linked_list_one, linked_list_two) == result, True)


        linked_list_one = array_to_linked_list([1])
        linked_list_two = array_to_linked_list(None)
        result = array_to_linked_list([1])
        self.assertEqual(merge_sorted(linked_list_one, linked_list_two) == result, True)


        linked_list_one = array_to_linked_list(None)
        linked_list_two = array_to_linked_list([5])
        result = array_to_linked_list([5])
        self.assertEqual(merge_sorted(linked_list_one, linked_list_two) == result, True)

        linked_list_one = array_to_linked_list([1])
        linked_list_two = array_to_linked_list([])
        result = array_to_linked_list([1])
        self.assertEqual(merge_sorted(linked_list_one, linked_list_two) == result, True)

        linked_list_one = array_to_linked_list([])
        linked_list_two = array_to_linked_list([4])
        result = array_to_linked_list([4])
        self.assertEqual(merge_sorted(linked_list_one, linked_list_two) == result, True)
        
        linked_list_one = array_to_linked_list([])
        linked_list_two = array_to_linked_list([])
        result = array_to_linked_list([])
        self.assertEqual(merge_sorted(linked_list_one, linked_list_two) == result, True)

unittest.main()

''' 
leetcode tests
All tests passed on leetcode
Runtime: 28 ms, faster than 63.70% of Python online submissions 
    for Merge Two Sorted Lists.
'''