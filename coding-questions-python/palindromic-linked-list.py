'''
Given a singly linked list of characters, write a function that returns true if the given list is palindrome, else false.

One approach is to "push" each node on to a stack.
* Then iterate over the linked list again.
* For each elem:
    - pop an elem from stack
    - compare them: if different, return false
    - if same for all, return true
* Even though it gives a linear runtime, it uses extra linear space O(N).

Can we tackle this problem using a different approach that dones't use additional storage?
* Find the "middle" of the linked list
* Reverse the second half of the linked list
* Start from head and tail and keep comparing them until both the half reach the "end"
* Tricky when the length of the linked list is odd
* This solution gives the same runtime complexity O(N) but constant O(1) space complexity.
'''

