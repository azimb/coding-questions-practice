'''
LC: https://leetcode.com/problems/merge-two-sorted-lists/
Complexity analysis: O(m+n) time complexity.
    O(1) space complexity, excluding the space required for the output/new linked list.
'''

class LinkedListNode:
    def __init__(self, val, next):
        self.val, self.next = val, next

def merge_sorted(self, l1, l2):
    dummy_node = LinkedListNode(-1)
    tail = dummy_node

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy_node.next

# tests
#trivial test
second_one = LinkedListNode(5, None)
head_one = LinkedListNode(2, second_one)
second_two = LinkedListNode(3, None)
head_two = LinkedListNode(1, second_two)
result = merge_sorted(head_one, head_two)
while result is not None:
    print(result.val)
    result = result.next

''' 
leetcode tests

All tests passed on leetcode
Runtime: 28 ms, faster than 63.70% of Python online submissions 
    for Merge Two Sorted Lists.
'''
