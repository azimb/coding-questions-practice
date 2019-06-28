def remove_duplicates(head):
    if head == None: return None

    prev = None
    cur = head
    seen = {}

    while cur != None:
        if cur.val in seen:
            prev.next = cur.next
        else:
            seen.add(cur.val)
        prev = cur
        cur = cur.next

