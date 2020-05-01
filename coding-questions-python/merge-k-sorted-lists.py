'''
LC: https://leetcode.com/problems/merge-k-sorted-lists/

Approach:
    - we can merge first two lists (O(n)), then the result with the third list, etc.
    - basically, we "merge 2 lists" k-1 times
    - this costs us O(kN) where k is the number of linked lists.

    - a better approach is to use a priority queue
    - compare every k nodes (head of every linked list) and get the node with the smallest value (with heap)
    - append the next node of the popped node
    - time complexity : O(Nlogk) where k is the number of linked lists

    - IMP: in order to do this in place, we will:
    a) maintain a dummy head, and append the "next" smallest node each time to the tail
    b) store the reference to the node (and not just node.val) in the heap, so that when the smallest
    node (technically, it's value) is popped, we have a reference to the node, through which we can get
    it's next node (and enqueue it)

Complexity analysis:
    - each push/pop on the priority queue costs us O(log k) time
    - there are total N elements in k lists
    - so, time complexity is O(N log k)

    - inplace algorithm
    - so, space complexity is O(1)

For different approaches and more details, refer to:
https://leetcode.com/problems/merge-k-sorted-lists/solution/
'''

import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val

def mergeKLists(self, lists):
    min_heap = []
    heapq.heapify(min_heap)

    dummy_head = ListNode(-1)
    tail = dummy_head

    # append the head of each of the k lists into the priority queue
    for head in lists:
        if head: heapq.heappush(min_heap, (head.val, head))

    while min_heap:
        pair = heapq.heappop(min_heap)
        val, node = pair[0], pair[1]

        tail.next = ListNode(val)
        tail = tail.next

        if node.next != None: heapq.heappush(min_heap, (node.next.val, node.next))

    return dummy_head.next

# all leetcode tests pass as of May 1st 2020
