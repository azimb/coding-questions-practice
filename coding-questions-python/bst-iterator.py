'''
LC: https://leetcode.com/problems/binary-search-tree-iterator/

Naive Approach:
    - do an inorder search and store the nodes in an auxiliary array
    - O(N) time and O(N) space

Optimized approach:
    - this approach is known as controlled recursion
    - we already know that we can't really pause a recursion in between and then start it off sometime later
    - however, if we could simulate a controlled recursion for an inorder traversal, we wouldn't really
    need to use any additional space other than the space used by the stack for our recursion simulation

    - in this approach, we approahc inorder traversal iteratively and we will use a custom stack
    - since we are using a custom data structure, we can pause and resume the recursion at will

    - important:
    * the stack top always contains the element to be returned for the next() function call.
    * for a given node root, the next smallest element will always be the leftmost element in its tree
    * after a call to next(), there are two possible scenarios:
    1. the popped node is a leaf node, so here, we don't have to do anything -- O(1)
    2. the popped node has a right child, so here, we call our helper function on the node's right child
    (the node either won't have a left child or would already have the left subtree processed)
    -- comparatively costly operation, based on the structure of the tree

    -- We keep on maintaining the invariant this way in the function call for next and this way we will
    always be able to return the next smallest element in the BST from the top of the stack

Time Complexity analysis:
    - next involves two major operations:
    1. we pop an element from the stack which becomes the next smallest element to return. This is a O(1) operation.
    2.  we then make a call to our helper function _inorder_left which iterates over a bunch of nodes. This is clearly a linear time operation i.e. O(N)O(N) in the worst case.

    - Thus, the amortized (average) time complexity for this function would still be O(1)

Space complexity analysis:
    - the space complexity is O(h)O(h) which is occupied by our custom stack for simulating the inorder traversal

For more details, refer to: https://leetcode.com/problems/binary-search-tree-iterator/solution/
'''


class BSTIterator(object):
    def __init__(self, root):
        # stack for the recursion simulation
        self.stack = []
        self._inorder_left(root)

    def next(self):
        # node at the top of the stack is the next smallest element
        node = self.stack.pop()
        # call the helper function for the right child
        self._inorder_left(node.right)
        return node.val

    def hasNext(self):
        # if stack is not empty, next exists
        return len(self.stack) > 0

    def _inorder_left(self, node):
        # for a given node, add all the elements in the leftmost branch of the tree
        while node:
            self.stack.append(node)
            node = node.left

# all leetcode tests pass as of May 15 2020
