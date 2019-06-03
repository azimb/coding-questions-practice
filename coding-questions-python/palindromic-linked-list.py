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
    # edge case
    if listNode is None:
        return True

    slow = listNode
    fast = listNode

    # find slow, which is the middle of the list
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half of the list
    result = reverseLinkedList(slow)
    slow.next = None

    # iterate over the "two" linked lists
    headOfListOne = listNode
    headOfListTwo = result

    # keep going until both the lists have nodes
    while(headOfListOne and headOfListTwo is not None):
        # if the values of the nodes match, set the pointer to next and continue
        if(headOfListOne.val == headOfListTwo.val):
            headOfListOne = headOfListOne.next
            headOfListTwo = headOfListTwo.next
            continue
        # values are different, indicated non-palindromic -- return False
        return False
    # while loop finished, all nodes matched -- return True
    return True

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

# all leet code tests passed