def remove_duplicates(head):
    if head == None: return None

    prev = None
    cur = head
    seen = set()

    while cur != None:
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
class TestRemoveDuplicates(unittest.TestCase):
    def test_addition(self):
        linked_list_one = array_to_linked_list([1, 2, 3, 4, 1, 5])
        result = array_to_linked_list([1, 2, 3, 4, 5])
        #self.assertEqual(remove_duplicates(linked_list_one) == result, True)


        linked_list_one = array_to_linked_list([6, 9, 3, 2, 9, 5, 9, 6, 2])
        result = array_to_linked_list([6, 9, 3, 2, 5])

        ans = remove_duplicates(linked_list_one)

        while ans is not None:
            print(ans.val)
            ans = ans.next

        #self.assertEqual(remove_duplicates(linked_list_one) == result, True)

        '''
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
        '''
unittest.main()
'''
result = array_to_linked_list([1, 2, 3, 4, 5])
while result != None:
    print(result.val)
    result = result.next
'''