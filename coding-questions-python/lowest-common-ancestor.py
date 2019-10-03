'''
LC: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

 YouTube: https://www.youtube.com/watch?v=py3R23aAPCA

    The key is that we want to root ourselves at a node and then search left and then right for either of the 2 nodes given.
    If we see either node, we will return it, if we do not find the node in a subtree search the value of null will be returned and bubbled up.

    After we search both left and right we ask ourselves what our results mean.

    If we found nothing to the left, we just bubble up what is on the right (whatever that search result may be). This node we sit at cannot be the LCA since the left and right            did not yield the 2 nodes we want.

    If we found nothing to the right, we just bubble up what is on the left (whatever that search result may be). This node we sit at cannot be the LCA since the left and right            did not yield the 2 nodes we want.

    If both the right and left result are not null, we have found our LCA.
    Why? We know it is an ancestor at the least but we definitely know it is the lowest common ancestor because we went bottom upwards, whatever we hit will be the LCA and it              will bubble up

    Time: O( n ) We will be touching the whole tree in the search, there are n nodes in the tree and we do O(1) work at each node.
    Space: O( h ) Stack usage at maximum will be the trees height. Worst case would be O(n) if our tree is skewed purely to the left or right and we need to find deep nodes.
'''

def lowestCommonAncestor(self, root, p, q):
    # root is None, so it cannot be the LCA
    if not root: return None

    # if one of the two nodes we are looking for has been found, send it back upwards
    if root == p or root == q: return root

    # can one of the two nodes be found in the left subtree
    left_lca = self.lowestCommonAncestor(root.left, p, q)
    # can one of the two nodes be found in the right subtree
    right_lca = self.lowestCommonAncestor(root.right, p, q)

    # if node is not found in the left subtree, return what you found from right subtree
    if not left_lca: return right_lca
    # if not is not found in right subtree, return what you found from left subtree
    if not right_lca: return left_lca

    # if both nodes found (one in each subtree), the current node is the lowest common ancestor
    return root
