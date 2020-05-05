'''
LC: https://leetcode.com/problems/reorder-list/

Approach:
    - the approach is pretty straight forward
    - divide the list into two halfs, and reverse the second half
    - then use two pointers, say p1 and p2, to traverse through both lists at the same time
    - in each iteration, grab a node from each list and append it to the resultant list

Complexity Analysis:
    - finding mid -- O(N)
    - reversing the second half of the list -- O(N/2) or O(N)
    - iterating over both halves -- O(N)
    - so, the time complexity is O(N)

    - taking out nodes from both halves and appending same nodes
    - this is an in-place algorithm
    - so, the space complexity is O(1)
'''

from ListNode import ListNode

def reorderList(self, head):
    # edge case
    if not head or not head.next: return head

    # find mid
    prev = None
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # divide the list into two parts
    prev.next = None

    # pointers for both lists
    p1, p2 = head, slow
    # reverse the second list
    p2 = self.rev(p2)

    dummy = ListNode(-1)
    tail = dummy

    # iterate through both lists simultaneously, and append a node from each to the resultant list
    while p1 or p2:
        if p1:
            tail.next = p1
            tail = tail.next
            p1 = p1.next

        if p2:
            tail.next = p2
            tail = tail.next
            p2 = p2.next

    return dummy.next


def rev(self, head):
    prev, cur = None, head
    while cur: cur.next, prev, cur = prev, cur, cur.next
    return prev

# all leetcode tests pass as of May 2 2020
