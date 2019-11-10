'''
LC: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Approach:
  - for each node, we compute a maximum contribution that this node and one/zero of its subtrees could add
    (in other words, it's a maximum gain one could have including the node (and maybe one of its subtrees) into the path)
  
  - if one would know for sure that the max path contains root, the problem would be solved as max_gain(root)
  - unfortunately, the max path does not need to go through the root
  - so, we need to check at each step what is better: 
    * to continue the current path or 
    * to start a new path with the current node as a highest node in this new path
    
  - each path has a highest node, which is also the lowest common ancestor of all other nodes on the path
  - for each node:
    * we compute the maximum path sum with input node as the "highest" node
    * and we return the maximum sum of the path that can be extended to input node's parent using cur_node and (maybe) one of its child
    
  - we will track "max_sum"
  - it's the value says whether this current root is the final root, so we use left + right + node.val
  
  - but to the upper layer(after return statement), we cannot choose both left and right branches
  - so we need to select the larger one, so we use max(left, right) + node.val to prune the lower brunch
  
  - to conclude: Each node actually has two roles when it comes to function maxPathDown:
    * when processing the final result max_sum, the node is treated as the highest point of a path
    * when calculating its return value, it is only part of a path (left or right part), and this return value 
      will be used to calculate path sum of other paths with some other nodes(above the current one) as their highest point
      
Time and space complexity:
  - O(N) time and O(H) space complexity
  - N = number of nodes in the binary tree
  - H = height of the BT -- N in worst case and log N in the best case
'''

def maxPathSum(self, root):
  max_sum = [root.val]
  self.sum_bt(root, max_sum)
  return max_sum[0]


def sum_bt(self, node, max_sum):
  # null node - sum is 0
  if not node: return 0

  # max_path sum from left and right subtree
  left_sum = max(self.sum_bt(node.left, max_sum), 0)
  right_sum = max(self.sum_bt(node.right, max_sum), 0)

  # current node is treated as the highest point of a path
  max_sum[0] = max(max_sum[0], node.val + left_sum + right_sum)

  # it's a part of a path
  return node.val + max(left_sum, right_sum)
  
# all leetcode tests pass as of 10th Nov 2019
