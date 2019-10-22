'''
LC: https://leetcode.com/problems/copy-list-with-random-pointer/
'''
def clone_ll_with_random_pointers(head):
    '''
    O(N) time and O(N) space
    For each node in the original linked list, create a new clone node that will make our new copy
    Although we don't set the next and random pointers of our clone nodes in the first pass,
        the trick is to maintain a hashmap to create each node's mapping with it's clone

    In the second pass, we pick each node, get it's clone from the map, and set the clone's next
    and random pointers by using the node's own next and random nodes.

    To clarify, when you go to current node's random, you also have the random clone node your
    current clone node's randome node should map to.

    This guarantees a linear time and space complexity.

    # corner case -- head is None
    if not head: return None

    # first pass -- for each node, create a clone node, and create a mapping
    clone_mapping = {}
    cur = head
    while cur:
        new_clone = Node(cur.val, None, None)
        clone_mapping[cur] = new_clone
        cur = cur.next

    # second pass -- for each node, get it's clone node
    # set the clone's next and random usng your own next and random and then accessing _their_ clone nodes using the hashmap
    cur = head
    while cur:
        # cur's clone
        clone = clone_mapping[cur]
        if cur.next: clone.next = clone_mapping[cur.next]
        if cur.random: clone.random = clone_mapping[cur.random]
        cur = cur.next

    return clone_mapping[head]
    '''

    '''
    O(N) time and O(1) space.
    
    In this approach, we are modifying the original linked list, so that each node's next pointer
    points to it's clone -- this helps us avoid using auxiliary space (hashmap)

    Now, we can set the random poiter of the clone node, using current node's random nodes's next
    (as cur node's random node is pointing to _it's_ clone)

    In the end, we fix the next pointers for all nodes
    '''
    if not head: return None

    # first pass -- each node's next will point to it's clone
    # but cur's clone will point to cur's next
    # random pointers are not disturbed
    cur = head
    while cur:
        new_clone = Node(cur.val, None, None)
        new_clone.next = cur.next
        cur.next = new_clone

        cur = cur.next.next

    # setting the random pointers for the clone nodes
    cur = head
    while cur:
        if cur.random: cur.next.random = cur.random.next
        cur = cur.next.next

    # store clone's head to return later
    result = head.next

    # fixing the previously ruined next pointers
    cur = head
    mirror = None
    while cur != None:
        mirror = cur.next
        if mirror: cur.next = mirror.next
        cur = mirror

    return result

# all leetcode tests pass
