'''
LC: https://leetcode.com/problems/intersection-of-two-linked-lists/

Approach 1:
    - straight forward approach, hashtable tracks the reference of seen nodes
    - O(M+N) time and O(M) space complexity

Approach 2:
    - a tricky two pointer technique solution
    - in the first iteration, we will reset the pointer of one linkedlist to the head of
        another linkedlist after it reaches the tail node. In the second iteration,
        we will move two pointers until they points to the same node.
    - our operations in first iteration will help us counteract the difference
    - so if two linkedlist intersects, the meeting point in second iteration must be the intersection point
    - if the two linked lists have no intersection at all, then the meeting pointer in second iteration must
        be the tail node of both lists, which is null
    Read more at: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
    - O(M+N) time and O(1) space complexity

Approach 3:
    - fairly straight forward
    _ find the difference in length, d, and skip first d nodes of the teh longer list
    - then iterate simultaneously until nodes match or one of the pointer reaches None
    - O(M+N) time and O(1) space
'''

def getIntersectionNode(headA, headB):
    '''
    # approach 1
    # O(M + N) time and O(M) space
    if not headA or not headB: return None
    seen = set([])

    while headA:
        seen.add(headA); headA = headA.next

    while headB:
        if headB in seen: return headB; headB = headB.next

    return None
    '''

    '''
    # approach 2
    # O(M+N) time and O(1) space -- two pointer technique
    # read about this technique: 
    if not headA or not headB: return None
    
    a, b = headA, headB
    
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    
    return a
    '''

    # O(M+N) time and O(1) space -- using the difference in length
    if not headA or not headB: return None

    a, lenA = headA, 0
    while a: a = a.next; lenA += 1

    b, lenB = headB, 0
    while b: b = b.next; lenB += 1

    a, b = headA, headB
    if lenA > lenB:
        a = increment(a, lenA - lenB)
    else:
        b = increment(b, lenB - lenA)

    while a and b:
        if a == b: return a
        a = a.next
        b = b.next

    return None

def increment(node, times):
    for _ in range(times):
        if node: node = node.next
    return node

# all leetcode tests pass as of May 2 2020
