'''
LC: https://leetcode.com/problems/min-stack/

Approach:
    - regular use of python list as stack, but storing tutples (elem, min)
    - along with elem, we store the min_so_far
    - this avoids the O(N) search on the stack on each get_min() call

Complexity analysis:
    - push, pop, top, and getMin -- O(1) time
    - list uses linear space

    - so, O(1) time and O(N) space complexity
'''


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        # along with the elem, store min_so_far
        prev_max = float('inf') if not self.stack else self.stack[-1][1]
        self.stack.append((x, min(x, prev_max)))

    def pop(self):
        # popping the pair (elem, min_so_far), so return just the elem
        pair = self.stack.pop()
        return pair[0]

    def top(self):
        # just get the elem from the pair
        return self.stack[-1][0]

    def getMin(self):
        # pair store elem, and min_so_far as a pair (tuple), so return min_so_far
        return self.stack[-1][1]

# all leetcode tests pass as of May 05 2020
