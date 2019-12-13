'''
Nested List Weight Sum (Premium)

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

Approach (DFS):
  - because the input is nested, it is natural to think about the problem in a recursive way
  - we go through the list of nested integers one by one, keeping track of the current depth dd
  - if a nested integer is an integer n, we calculate its sum as n*d
  - otherwise, if the nested integer is a list, we calculate the sum of this list recursively using the same process 
    but with depth d+1

Complexity Analysis:
  - algorithm takes O(N) time, where N is the total number of nested elements in the input list
  - for example, the list [ [[[[1]]]], 2 ] contains 4 nested lists and 2 nested integers (1 and 2), so N=6
  
  - in terms of space, at most O(D) recursive calls are placed on the stack, where D is the maximum level of nesting in the input
  - for example, D=2 for the input [[1,1],2,[1,1]], and D=3 for the input [1,[4,[6]]]
'''

from numbers import Number

def sum_of_nested_ints(input_arr):
    return nested_sum_recursive(input_arr, 1)

def nested_sum_recursive(input_arr, depth):
  cur_sum = 0
  
  for elem in input_arr:
    if isinstance(elem, Number): cur_sum += elem * depth
    else: cur_sum += nested_sum_recursive(elem, depth + 1)

  return cur_sum

# Note that LC expects you to use NestedInteger interface, so the code may require some changes
