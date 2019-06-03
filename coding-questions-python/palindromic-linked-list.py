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

class LinkedListNode:
    def __init__(self, val, next):
        self.val, self.next = val, next

def checkPalindrome(listNode):
    slow = listNode
    fast = listNode

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        prevNode = slow
        curNode = prevNode.next
        nextNode = curNode.next

        prevNode.next = None

        while nextNode is not None:
            curNode.next = prevNode
            #prevNode.next = None

            prevNode = curNode
            curNode = nextNode
            nextNode = nextNode.next

        curNode.next = prevNode
        prevNode.next = None


fourth = LinkedListNode(9, None)
third = LinkedListNode(6, fourth)
second = LinkedListNode(5, third)
head = LinkedListNode(2, second)

checkPalindrome(head)
