'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
    and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Leetcode: https://leetcode.com/problems/add-two-numbers/

Approach:
    -- note: var carry will keep a track of the "remainder" or "carry" from the addition of the previous two nodes
    - loop each node in both lists simultaneously
    - add the values of both nodes and carry
        . if the sum is less than 10, make a node with that value and append it to the result
        (make carry 0)
        . else, grab the last digit from the sum , make a node with that value and append it to the result
        (make carry 1)
    - in the end if any nodes in either of lists haven't been visited yet,
        use carry accordingly and append them to the result
    - if carry is not 0 in the end (i.e. carry is 1), make a new node with value 1 and append it to the end of result

Complexities:
    - linear or O(N) time complexity
    - constant or O(1) space complexity
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

def add_two_numbers(l1, l2):
    # references to the head nodes of the two input lists
    l1_pointer = l1
    l2_pointer = l2

    counter = 0
    # this is the resultant list
    # each node's value will be a result of the addition of the corresponding values from each list

    sum = LinkedListNode(0, None)
    head = sum

    # this variable will help "carry" over a part of the sum of two nums to the next sum
    carry = 0

    while l1_pointer or l2_pointer:

        if counter == 20:
            break

        val_one = 0 if l1_pointer is None else l1_pointer.val
        val_two = 0 if l2_pointer is None else l2_pointer.val


        addition = val_one + val_two + carry
        sum.next = LinkedListNode(addition%10, None)
        sum = sum.next
        carry = carry//10


        if l1_pointer is not None: l1_pointer = l1_pointer.next
        if l2_pointer is not None: l2_pointer = l2_pointer.next


        counter += 1


    if carry > 0:
        sum.next = LinkedListNode(carry, None)



    return head.next

    '''
    # keep going until we reach the end of either of lists
    while l1_pointer is not None and l2_pointer is not None:
        num = l1_pointer.val + l2_pointer.val + carry
        if num < 10:
            sum.next = LinkedListNode(num, None)
            sum = sum.next
            carry = 0

        else:
            sum.next = LinkedListNode(num % 10, None)
            sum = sum.next
            carry = 1

        l1_pointer = l1_pointer.next
        l2_pointer = l2_pointer.next

    while l1_pointer is not None:
        num = l1_pointer.val + carry
        if num < 10:
            sum.next = LinkedListNode(num, None)
            sum = sum.next
            carry = 0

        else:
            sum.next = LinkedListNode(num % 10, None)
            sum = sum.next
            carry = 1

        l1_pointer = l1_pointer.next

    while l2_pointer is not None:
        num = l2_pointer.val + carry
        if num < 10:
            sum.next = LinkedListNode(num, None)
            sum = sum.next
            carry = 0

        else:
            sum.next = LinkedListNode(num % 10, None)
            sum = sum.next
            carry = 1

        l2_pointer = l2_pointer.next

    if carry == 1:
        sum.next = LinkedListNode(1, None)
        sum = sum.next

    return head.next
    '''


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
    def test_no_carry_same_size(self):
        linked_list_one = array_to_linked_list([1, 2, 3])
        linked_list_two = array_to_linked_list([4, 5, 6])
        result = array_to_linked_list([5, 7, 9])
        self.assertEqual(add_two_numbers(linked_list_one, linked_list_two) == result, True)

    def test_no_carry_longer_listTwo(self):
        linked_list_one = array_to_linked_list([1, 2, 3])
        linked_list_two = array_to_linked_list([4, 5, 6, 5, 5, 9, 0, 6])
        result = array_to_linked_list([5, 7, 9, 5, 5, 9, 0, 6])
        self.assertEqual(add_two_numbers(linked_list_one, linked_list_two) == result, True)

    def test_no_carry_longer_listOne(self):
        linked_list_one = array_to_linked_list([7, 3, 9, 6, 5, 2])
        linked_list_two = array_to_linked_list([2, 5, 0, 0])
        result = array_to_linked_list([9, 8, 9, 6, 5, 2])
        self.assertEqual(add_two_numbers(linked_list_one, linked_list_two) == result, True)

    def test_carry_same_size(self):
        linked_list_one = array_to_linked_list([5, 4, 3])
        linked_list_two = array_to_linked_list([4, 6, 1])
        result = array_to_linked_list([9, 0, 5])
        self.assertEqual(add_two_numbers(linked_list_one, linked_list_two) == result, True)

    def test_carry_longer_listTwo(self):
        linked_list_one = array_to_linked_list([9, 2, 8])
        linked_list_two = array_to_linked_list([4, 5, 8, 5, 5, 9, 0, 6])
        result = array_to_linked_list([3, 8, 6, 6, 5, 9, 0, 6])
        self.assertEqual(add_two_numbers(linked_list_one, linked_list_two) == result, True)

    def test_no_carry_longer_listOne(self):
        linked_list_one = array_to_linked_list([8, 3, 9, 6, 5, 2])
        linked_list_two = array_to_linked_list([9, 8, 0, 0])
        result = array_to_linked_list([7, 2, 0, 7, 5, 2])
        self.assertEqual(add_two_numbers(linked_list_one, linked_list_two) == result, True)

    def test_carry_overflow(self):
        linked_list_one = array_to_linked_list([1, 3, 9, 6])
        linked_list_two = array_to_linked_list([1, 5, 6, 8])
        result = array_to_linked_list([2, 8, 5, 5, 1])
        self.assertEqual(add_two_numbers(linked_list_one, linked_list_two) == result, True)

unittest.main()

# all leetcode tests passed
# Runtime: 52 ms, faster than 84.13% of Python online submissions for Add Two Numbers.