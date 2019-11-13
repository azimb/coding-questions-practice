'''
Nested List Weight Sum II (Premium)
LC: https://leetcode.com/problems/nested-list-weight-sum-ii/

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., 
the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.

Example 2:
Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.


Approach:
  - Instead of multiplying by depth, add integers multiple times 
    (by going level by level and adding the unweighted sum to the weighted sum after each level)
  - check: https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83655/JAVA-AC-BFS-solution/275829
    
# TODO: time and space complexity
'''

from collections import deque

def depthSumInverse(nestedList):
  unweighted, weighted = 0, 0
  queue = deque(nestedList)

  while queue:
    for i in range(len(queue)):
      nested_int = queue.popleft()

      if nested_int.isInteger(): unweighted += nested_int.getInteger()
      else: 
        for ni in nested_int.getList(): queue.append(ni)

    weighted += unweighted

  return weighted
  
# all leetcode tests pass as of 12th Nov 2019
