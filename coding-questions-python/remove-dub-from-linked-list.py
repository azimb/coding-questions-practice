def remove_duplicates(head):
    if head == None: return None

    prev = None
    cur = head
    seen = {}

    while cur != None:
        if cur.val in seen:
            prev.next = cur.next
        else:
            seen.add(cur.val)
        prev = cur
        cur = cur.next

# tests
import unittest
class TestRemoveDuplicates(unittest.TestCase):
    def test_addition(self):
        linked_list_one = array_to_linked_list([1, 2, 3, 4, 1, 5])
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