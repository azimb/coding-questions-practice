'''
LC: https://leetcode.com/problems/linked-list-cycle-ii/

Approach 1:
  - use a hashset to track seen nodes
  - when the cur node is already in the hashset, return it
  - O(N) time and space complexity
  
Approach 2:
  - Floyd's Tortoise and Hare Algorithm
  - divides into two phases -- 1) find if linked list is cyclic 2) find enterance
  - algorithm:
    * once it has been confirmed that the linked list is cyclic, go on to phase 2
    * in phase two, two pointers p1 and p2 start from head and intersection
    * in every iteration, move them to their next
    * they will meet at the enterance node
    
  - O(N) time and O(1) space complexity
'''

def detectCycle(self, head):
  slow = fast = head
  while fast and fast.next:
    slow, fast = slow.next, fast.next.next
    # linked list is cyclic, find intersection and return it
    if slow == fast: return self.find_enterance(head, slow)
  # linked list is not cyclic
  return None

def find_enterance(self, head, intersection):
  # in every iteration, move the pointers to their next
  # when they meet, we have found the enterance node
  while head != intersection: head,intersection = head.next, intersection.next
  return head
  
  # all leetcode tests pass as of 22th Oct 2019
