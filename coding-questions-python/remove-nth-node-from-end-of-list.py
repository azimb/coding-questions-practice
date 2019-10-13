'''
Remove nth node from the end of a singly linked list
LC: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Time and space complexity: O(N) and O(1)
'''

def removeNthFromEnd(self, head, n):
  prev = None # will stop at one before the node to be removed
  cur = last = head # will stop at the node to be removed

  # the idea is to make last point to n nodes after cur, so cur stops at the node to be removed
  for i in range(n): last = last.next

  # find the node to be removed using cur pointer
  while last: prev, cur, last = cur, cur.next, last.next

  # not prev means remove head
  if not prev: return head.next

  # remove cur by setting prev's next pointer to cur's next node
  prev.next = cur.next 

  return head
  
# all leetcode tests pass as of 13th Oct 2019
