'''
LC: https://leetcode.com/problems/sort-list/

Approach:
    - merge sort, O(n log n) time and O(log(n)) space complexity
    - space complexity due to stack space used by the recursive solution
    - using fast/slow two pointer technique to find the mid of the linked list

Note:
    - merge sort can be accomplished by following a bottom-up approach
    - omitting recursion will reduce the space complexity to O(1)
    - refer to the following for explanation and code:
    * explanation: https://www.youtube.com/watch?v=lOUe8Q9jQow
    * code: https://leetcode.com/problems/sort-list/discuss/46712/Bottom-to-up(not-recurring)-with-o(1)-space-complextity-and-o(nlgn)-time-complextity
'''
from ListNode import ListNode

def sortList(head):
    # edge case
    if not head: return None

    '''
    Merge sort begins here
    '''
    # base case
    if not head.next: return head

    # head of left half
    head_left = head

    # find head of right half
    left_tail = head
    fast, head_right = head, head
    while fast and fast.next:
        left_tail = head_right
        head_right = head_right.next
        fast = fast.next.next

    # break connection between left and right
    left_tail.next = None

    # mergesort left half
    left_sorted = sortList(head_left)

    # mergesort right half
    right_sorted = sortList(head_right)

    # merge
    sorted_list = merge(left_sorted, right_sorted)

    return sorted_list


# usual merge two linked lists operation
def merge(self, l1, l2):
    l1_p, l2_p = l1, l2
    dummy_head = ListNode(-1)
    tail = dummy_head

    while l1_p and l2_p:
        if l1_p.val <= l2_p.val:
            tail.next = l1_p
            l1_p = l1_p.next

        else:
            tail.next = l2_p
            l2_p = l2_p.next

        tail = tail.next

    tail.next = l1_p if l1_p else l2_p

    return dummy_head.next

# all leetcode tests pass as of May 1st 2020
