class LinkedListNode:
    def __init__(self, val, next):
        self.val, self.next = val, next

def merge_sorted(head_one, head_two):
    dummyNode = LinkedListNode(0, None)
    tail = dummyNode

    while True:
        if not head_one:
            tail.next = head_two
            break

        if not head_two:
            tail.next = head_one
            break

        if head_one.val <= head_two.val:
            tail.next = head_one
            tail = tail.next
            head_one = head_one.next
        else:
            tail.next = head_two
            tail = tail.next
            head_two = head_two.next

    return dummyNode.next

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
