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


