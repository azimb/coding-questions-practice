'''
Convert Binary Search Tree to Sorted Doubly Linked List (Premium)
LC: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
YouTube: https://www.youtube.com/watch?v=FsxTX7-yhOw

Approach:
  - usual inorder search with a variation
  - recurse left, process node, recurse right
  - process node:
    * link up prev with cur node
    * if no prev, cur node is head
  - REMEMBER to make cur node as prev

Time complexity:
  - each node is process exactly once
  - O(N) or linear
  
Space complexity:
  - space used by the call stack, so O(H)
  - H is log n when the tree is balanced, or N in the worst case
'''

class Solution(object):
  head = tail = None
  def treeToDoublyList(self, root):
    def bst_to_dll(root):
      # base case
      if not root: return

      # inorder traversal, so recurse left, process node, and then recurse right

      # 1. recursive left
      bst_to_dll(root.left)

      # 2. process node
      if not self.tail: self.head = root # fir node in inorder traversal, this becomes the head of dll
      else: # link cur with prev
        root.left = self.tail
        self.tail.right = root

      # for the next node (in inorder), cur node becomes prev
      self.tail = root

      # 3. recurse right
      bst_to_dll(root.right)

    # edge case
    if not root: return

    # recursively convert bst to ll
    bst_to_dll(root)
    # link head and tail
    self.head.left = self.tail
    self.tail.right = self.head
    # return head
    return self.head
    
# all leetcode tests pass as of 5th November 2019
