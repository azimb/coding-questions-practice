'''
LC: https://leetcode.com/problems/palindrome-linked-list/
GfG: https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/

O(N) time complexity, and O(1) space complexity
'''

def isPalindrome(self, head):

    if not head or not head.next: return True # empty ll or singleton

    l1_tail = None # tail of the first half of the ll
    mid = None # will store the mid elem, if the len of ll is odd
    palindrome = True # this flag will be used to return

    # find the middle, remem to store the tail of list one
    slow = fast = head
    while fast and fast.next: 
        l1_tail = slow
        slow, fast = slow.next, fast.next.next

    # if the len is odd, start of second half of list will be slow.next
    # remem to also store the middle
    if fast:
        mid = slow
        slow = slow.next
        l1_tail.next = None

    # reverse the second half
    slow = self.rev(slow)

    # check both lists: make flag false if any of the ndoes don't match and break   
    cur = head
    while slow:
        if cur.val != slow.val:
            palindrome = False
            break
        cur, slow = cur.next, slow.next

    # reverse the second half again
    slow = self.rev(slow)

    # if not mid: tail of first list .next =>  head of list 2
    # if mid: tail of first list .next => mid . next => head of list 2
    if mid: 
        l1_tail.next = mid
        l1_tail = l1_tail.next    
    l1_tail.next = slow

      # return flag
      return palindrome
        
        
# reverse a singly linked list
def rev(self, head):
    prev, cur = None, head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

# all leetcode tests pass as of Oct 6th 2019
