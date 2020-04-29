'''
LC: https://leetcode.com/problems/count-complete-tree-nodes/

Approach:
	- the naive approach is to count each node, and as there are 2^h - 1 nodes (at most) in a full binary tree,
	the runtime would be -- O(2^h) or O(n)
	- however, this approach would work for any binary tree, even if it's completely imbalanced
	- if we make use of the "complete"ness property, we can eliminate unneccessary computations
	
	- the approach suggests that half of the tree can be discarded at each recursive callable
	- explanation:
		* the height of a tree can be found by just going left
		* if the whole tree is empty, i.e., has height 0, there are 0 nodes
		* otherwise we check whether the height of the right subtree is just one less than that 
		of the whole tree, meaning left and right subtree have the same height
		
		a) if yes, then the last node on the last tree row is in the right subtree and the left subtree is a full tree 
		of height h-1. So we take the 2^h-1 nodes of the left subtree plus the 1 root node plus the number of nodes 
		in the right subtree (which we find recursively)
		
		b) if no, then the last node on the last tree row is in the left subtree and the right subtree is a full tree 
		of height h-2. So we take the 2^(h-1)-1 nodes of the right subtree plus the 1 root node plus the number 
		of nodes in the left subtree (which we find recursively)
		
Complexity analysis:
	- since we halve the tree in every recursive step, we have O(log(n)) steps
	- finding a height costs O(log(n))
	- so, the runtime complexity is O(log(n)^2)
	
	- O(log n) recursive calls
	- so, the space complexity is O(log(n))
	
Inspired by: https://leetcode.com/problems/count-complete-tree-nodes/discuss/61958/Concise-Java-solutions-O(log(n)2)
'''

# the height of a tree can be found by just going left
def height(root):
        return 0 if (not root) else (1 + height(root.left))
    
def countNodes(root):
	# height of the tree rooted at root
	h = height(root)
	
	# height is 0, so no nodes in the tree
	if h == 0: return 0
	
	# check height of right_subtree
	r_h = height(root.right)
	
	# height of left subtree = high of right subtree
	# last node of the last level is in the right subtree, so left subtree is full with height h - 1
	if r_h == h-1: return 1 + (2**(h - 1) - 1) + countNodes(root.right)
	
	# height of left subtree - 1 = high of right subtree
	# last node of the last level is in the left subtree, so right subtree is full with height h - 2
	else: return 1 + (2**(r_h) - 1) + countNodes(root.left)
	
# all leetcode tests pass as of 28th April 2020