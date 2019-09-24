'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.

Note: a node has no pointer to it's parent

Leetode Premium: https://leetcode.com/problems/inorder-successor-in-bst/

Approach:
    - Case 1: node p has a right child
        Go deep to the left most node in the right subtree of node p (find min in p.right)

    - Case 2: node p _doesn't_ have a right child
        Go to the nearest ancestor for which node p would be in the left substree
        The idea is to keep a track of a successor whenever you access a node left subtree

Time complexity:
    - case 1 -- O(Hp) where Hp is the height of BST with root p (best case)
    - case 2 -- O(H) where H is the height of the given BST (worst case)

video explanation: https://www.youtube.com/watch?v=5cPbNCrdotA
'''

def inorderSuccessor(root, p):
    # if p has a right child, successor is the min node in the right child
    if p.right:
        p = p.right
        while p.left: p = p.left
        return p

    # p doesn't have a right child
    # successor is a node in the chain of ancestors from root to p
    # specifically, it's deepest ancestor who's left subtree p lies in
    successor = None
    ancestor = root

    while ancestor != p:
        # search in left
        if ancestor.val > p.val:
            successor = ancestor  # we went left, so update the successor
            ancestor = ancestor.left

        # search in right
        else:
            ancestor = ancestor.right

    return successor
