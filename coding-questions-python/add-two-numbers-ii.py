'''
LC: https://leetcode.com/problems/add-two-numbers-ii/

Approach:
    - pretty straight forward, and similar to / makes use of add two numbers i
    - reverse both lists, add as added in "add two numbers i", and then reverse the answer
    - O(M+N) time and O(1) space complexity

Note: you could check leetcode discuss for other ways to solve this problem
'''

from ListNode import  ListNode

def addTwoNumbers(l1, l2):
    # reverse both lists
    l1_rev = reverseLinkedList(l1)
    l2_rev = reverseLinkedList(l2)

    # added reversed lists, and reverse the anseer
    ans_rev = addTwoNumbersHelper(l1_rev, l2_rev)
    ans = reverseLinkedList(ans_rev)

    # reverse the input lists again, as the input must not be destroyed
    l1 = reverseLinkedList(l1_rev)
    l2 = reverseLinkedList(l2_rev)

    # return the resultant list
    return ans


# util function to reverse a singly linked list
def reverseLinkedList(head):
    prev, cur = None, head
    while cur: cur.next, prev, cur = prev, cur, cur.next
    return prev


# util function to add two intergers represented as singly linked list
# refer to the following for an in-depth explanation:
# https://github.com/baghadiya/coding-questions-practice/blob/master/coding-questions-python/add-two-numbers.py
def addTwoNumbersHelper(l1, l2):
    l1_p, l2_p = l1, l2
    carry, dummy_result = 0, ListNode(-1)
    tail = dummy_result

    while l1_p or l2_p or carry:
        l1_val = 0 if not l1_p else l1_p.val
        l2_val = 0 if not l2_p else l2_p.val

        cur_sum = l1_val + l2_val + carry

        tail.next = ListNode(cur_sum % 10)
        tail = tail.next

        carry = cur_sum / 10

        if l1_p: l1_p = l1_p.next
        if l2_p: l2_p = l2_p.next

    return dummy_result.next

# all leetcode tests pass as of April 30 2020
