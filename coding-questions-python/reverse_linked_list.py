'''
First thing that comes to my mind:
	Iterate over the linked list and add each element to a stack.
	Keep poping the items from the stack and set the next value of each node.
	Ex: a->b->c
	Stack (bottom)a,b,c(top)
	pop, set next to pop
	
	This gives us a linear time and linear space complexity.
	
Update:
We are dealing with linked lists. Linked lists --> Pointers
Can we play around with pointers to avoid using additional space?
Looks like best concievable runtime is linear as we need to "touch" each element
	atleast once in order to reverse the order.

(Updated) Algo design / pseudocode

a -> b -> c -> d -> e -> f
a <- b <-c <- d <- e <- f
			  	   
-- edge cases
if null return null
if head.next null return head

-- generic algo
prev = head
current = prev.next
next = current.next

while(next == null)
	current.next = prev
	prev = current
	current = next
    next = current.next

current.next = prev
return current
Runtime complexity is O(N) where N is the length of the linked list. Constant space complexity.
'''

class LinkedListNode:
    def __init__(self, val, next):
        self.val, self.next = val, next

def reverseLinkedList(head):
    # empty list
    if head is None:
        return None

    # singleton
    elif head.next is None:
        return head

    # generic case
    else:
        prev = head
        current = prev.next
        next = current.next

        prev.next is None

        while next is not None:
            current.next = prev
            prev = current
            current = next
            next = current.next

        current.next = prev
        head.next = None
        return current

fourth = LinkedListNode(9, None)
third = LinkedListNode(6, fourth)
second = LinkedListNode(5, third)
head = LinkedListNode(2, second)

# testing on leetcode
# https://leetcode.com/problems/reverse-linked-list/
# all tests passed. solution faster than more than 96% of the solutions