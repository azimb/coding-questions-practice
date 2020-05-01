'''
LC: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

Approach 1:
    - recursive
    - swap first two nodes, made second node new_head, and recursively solve the rest of the list
    - old_heads's next is the answer of the recursive call
    - O(n) time and O(n) space complexity (space due to recursive call stacks)

Approach 2:
    - iterative
    - the trick is to use a pointer p that is previous to the next two nodes  to be swapped
    - next two nodes, swap_one and swap_two, are swapped
    - pointer becomes old_head (that is, node at index 1) -- this is because it is previous to the
    next two nodes that will be swapped (index 2,3)

    - IMP: remember to update _pointer.next_ in order to make sure new_head is set correctly

    - O(N) time and O(1) space complexity

Refer to the following for an explanation with diagrams:
https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11046/My-simple-JAVA-solution-for-share/186959
'''

'''
   a) Recursive
   O(N) time and O(N) space
'''
def swapPairs(self, head):
    if not head or not head.next: return head

    temp = self.swapPairs(head.next.next)
    head.next.next = head
    new_head = head.next
    head.next = temp

    return new_head


'''
b) Iterative
O(N) time and O(1) space
'''
from LinkedListNode import LinkedListNode
def swapPairs(head):
    dummy = LinkedListNode(-1)
    dummy.next = head

    point = dummy

    while point.next and point.next.next:
        swap_one = point.next
        swap_two = point.next.next

        swap_one.next = swap_two.next
        swap_two.next = swap_one

        point = swap_one
        point.next = swap_two

    return dummy.next

# all leetcode tests pass for both as of May 1 2020
