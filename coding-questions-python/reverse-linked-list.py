'''
Reverse linked list: https://leetcode.com/problems/reverse-linked-list/
Reverse linked list ii: https://leetcode.com/problems/reverse-linked-list-ii/
^ refer to for help: https://www.youtube.com/watch?v=GSJuwQzKSnI
'''

'''
O(N) runtime, O(1) space 
- simply make each node point to it's previous
- return the original tail as the new head
'''
def reverseList(head):
    prev, cur = None, head
    while cur: cur.next, prev, cur = prev, cur, cur.next
    return prev


'''
O(N) time and O(1) space
- reverse the nodes b/w the mth and nth node (inclusive)
'''

'''
    Reverse Linked List II
    Visual of the three parts:
    x x x         xs x x x x xr     x x 
    -----         -------------     ---
    unreversed    reversed      unreversed

    after first loop:
    x x x         xs x x x x xe     x x 
        |         |
       prev      cur
    connection   tail

    After second loop:

    x x x         xe x x x x xs     x x 
        |                     |     |
    connection              tail   cur
'''

def reverseList2(head, m, n):
    # loop m-1 times, then prev cur points to the start of the sublist that needs to be reversed
    # remember to decrement n, as m-n nodes starting from m need to be reversed
    prev, cur = None, head
    while m > 1:
        prev, cur = cur, cur.next
        m -= 1
        n -= 1

    # prev points to the node that is previous of the start of the sublist that needs to be reversed
    # prev.next -> reversed_sublist
    connection = prev

    # after reversing the sublist, the cur node (or the head of the sublist) will appear at the end
    # so we store in the tail pointer, to be used later to connect the remaining part of the list
    tail = cur

    # reverse m-n nodes, or the (updated) amount of n nodes
    while n > 0:
        cur.next, cur, prev = prev, cur.next, cur
        n -= 1

    # connection was not None, i.e. sublist didn't start at the head. So it needs to appear as "next" of the
    #  unreversed part of the list
    if connection: connection.next = prev
    # sublist (that was reversed) started at head, so it's head becomes the new head
    else: head = prev

    # cur currently points to the part of the list that:
    # a) remain un-reversed
    # b) and appears after the reversed sublist
    # so, we connect the tail of the reversed sublist to this un-reversed part
    tail.next = cur

    return head

# all leetcode tests pass for both as of April 30 2020
