'''
The selection sort is a combination of searching and sorting. During each pass, the unsorted element
with the smallest (or largest) value is moved to its proper position in the array. The number of times
the sort passes through the array is one less than the number of items in the array.

Time complexity: O(n^2) -- worst/avg/best
Space complexity: O(1)
'''

from ListNode import ListNode


def selection_sort_linked_list(head):
    sorted_list = ListNode(-1)
    tail = sorted_list

    while head:
        prev, cur = None, head
        lowest, node_previous, node, node_next = float('+inf'), None, None, None
        while cur:
            if cur.val < lowest:
                node_previous, node, node_next = prev, cur, cur.next
                lowest = node.val
            prev, cur = cur, cur.next

        if not node_previous:
            head = node.next
        else:
            node_previous.next = node.next

        node.next = None

        tail.next = node
        tail = tail.next

    return sorted_list.next
