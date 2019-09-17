'''
Given a string, find the length of the longest substring without repeating characters.
Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:
    - iterate over the two lists simultaneously, node by node, and add the two digits (and carry)
    - the sum of two digits will be from 0 .. 18
    - we maintain a carry variable, in case of "overflow" (sum of 2 digits > 9)
    (carry can be 0 or 1)

    - also note that the trick is to have a dummy_head so that we can append nodes to it
    - in the end, we return dummy_head.next

Complexities:
    - time complexity: iterating over the two lists once, so time complexity is O(n+m) where
        n.m are the lengths of the two linked lists
    - space complexity is O(1) or constant
'''

from LinkedListNode import LinkedListNode

def add_two_numbers(l1, l2):
    dummy = LinkedListNode(-1)
    result = dummy # result will keep a pointer to the dummy_head
    l1_pointer, l2_pointer = l1, l2
    carry = 0

    # keep iterating until we have reached until the end of both lists and carry is 0
    while l1_pointer or l2_pointer or carry:
        val_one = l1_pointer.val if l1_pointer != None else 0
        val_two = l2_pointer.val if l2_pointer != None else 0
        addition = val_one + val_two + carry

        # carry is the first digit of the two digits of the addition
        # or 0 if the sum is single digit
        carry = addition // 10

        # add the second digit of the addition as a Node
        # or the only digit, if it's a single digit addition
        dummy.next = LinkedListNode(addition % 10)
        dummy = dummy.next

        # go to the next node in the list, if it exists
        if l1_pointer != None: l1_pointer = l1_pointer.next
        if l2_pointer != None: l2_pointer = l2_pointer.next

    return result.next

# all leetcode tests pass