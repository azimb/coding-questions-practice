'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.

Leetcode premium: https://leetcode.com/problems/inorder-successor-in-bst-ii/

Approach (inspired from pramp):
    - suppose the the inorder successor of input_node is successor_node
    - there are two cases:
        a) input_node has a right child. In this case, successor_node would be the node with the minimum key in
           input_node's right subtree
        b) input_node doesn't have a right child. In this case, successor_node would be one of input_node's ancestors.
           More specifically, within input_node's ancestor's chain (starting from inputNode all the way up to the root),
           successor_node is the first parent that has a left child in that chain
    - if the input_node doesn't have a right child, and all of it's ancestors are right children of its parents,
      input_node doesn't have a successor -- successor would be null

Why does this approach work (pramp.com):
    - So why is this always true? Well, if inputNode was inserted to the tree prior to successorNode,
      then since successorNode.key is greater than inputNode.key, but also smaller than all other keys greater than
      successorNode.key, successorNode has to be in inputNode's right subtree.

    -Now, if inputNode was inserted to the tree after successorNode was, then since inputNode.key is smaller than
    successorNode.key, but also larger than all other keys smaller than successorNode.key, inputNode has to be in
    successorNode's left subtree.

Time complexity:
    - in both cases, we are visiting O(H) number of nodes, where H is the height of the BST
    - for a balanced BST, H = log n (where n is the number of nodes in the tree)
    - so, the time complexity is O(log n) for a balanced BST

    - for an unbalanced BST, time complexity is O(n)

Space complexity:
    - throughout the entire algorithm we used only a constant amount of space
    - so, the space complexity is O(1) or constant
'''
def inorder_successor_in_bst(node):
    # corner case
    if not node: return None

    # if the node has a right child, find the node with the minimum value in the right child
    if node.right: return get_min_from_child(node.right)

    # if the node doesn't have a right child, the inorder successor is the first ancestor that has a left child in the ancestor chain
    child = node
    ancestor = node.parent
    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = child.parent

    return ancestor

def get_min_from_child(input_node):
    # get the node with the least value in the BST
    while input_node.left: input_node = input_node.left
    return input_node

# all leetcode tests pass