def remove_duplicates(head):
    if head is None: return None

    prev, cur = None, head
    seen = set()

    while cur is not None:
        if cur.val in seen:
            prev.next = cur.next
        else:
            seen.add(cur.val)
            prev = cur
        cur = cur.next

    return head


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


# utility method to convert a an array to a linked list
def array_to_linked_list(arr):
    if arr is None: return None
    current = None
    for i in range(len(arr)-1, -1, -1):
        new_node = LinkedListNode(arr[i], current)
        current = new_node
    return current


# tests
import unittest
class TestRemoveDuplicates(unittest.TestCase):
    def test_addition(self):
        linked_list_one = array_to_linked_list([1, 2, 3, 4, 1, 5])
        result = array_to_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates(linked_list_one) == result, True)


        linked_list_one = array_to_linked_list([6, 9, 3, 2, 9, 5, 9, 6, 2])
        result = array_to_linked_list([6, 9, 3, 2, 5])
        self.assertEqual(remove_duplicates(linked_list_one) == result, True)


        linked_list_one = array_to_linked_list([-7, - 8])
        result = array_to_linked_list([-7, -8])
        self.assertEqual(remove_duplicates(linked_list_one) == result, True)

        linked_list_one = array_to_linked_list([12])
        result = array_to_linked_list([12])
        self.assertEqual(remove_duplicates(linked_list_one) == result, True)


        linked_list_one = array_to_linked_list([])
        result = array_to_linked_list([])
        self.assertEqual(remove_duplicates(linked_list_one) == result, True) 

        linked_list_one = array_to_linked_list(None)
        result = None
        self.assertEqual(remove_duplicates(linked_list_one) == result, True)

unittest.main()

# all leetcode tests pass
# Runtime: 28 ms, faster than 82.26% of Python online submissions for Remove Duplicates from Sorted List.