'''
User defined (singly) linked list none class.
Each node stores a value, and a pointer to next (node).

Sample usage:
```
second = LinkedListNode(5, None)
head = LinkedListNode(2, second)
```
'''

class ListNode:
    def __init__(self, val, next):
        self.val, self.next = val, next
