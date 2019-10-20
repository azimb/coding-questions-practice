'''
LC: https://leetcode.com/problems/monotonic-array/
Approach:
  - start with two flags -- mon_inc, and mon_dec
  - for each number, compare it to the number on it's right
  * if number to the right is smaller, mon_inc will not hold
  * if number to the right is bigger, mon_dec will not hold
  - in the end check if either property (inc/dec) is True
Complexity analysis: O(N) time and O(1) space complexity
'''

def isMonotonic(self, A):
  inc, dec = True, True
  for i in range(len(A) - 1):
    if A[i] > A[i+1]: inc = False
    if A[i] < A[i+1]: dec = False
  return inc or dec

  '''
  # alternate approach: figure out if increasing or decreasing, then check all numbers

  if len(A) == 0 or len(A) == 1: return True

  index = 0
  # edge case where the first few numbers are same -- we cannot find out if we are checking for increasing or decreasing
  # ex: [1,1,0]
  # in this case, we find the last occurance of these duplicates
  while index < len(A)-1 and A[index] == A[index+1]: index += 1
  if index == len(A)-1: return True

  # increasing
  if A[index] <= A[index+1]:
    for i in range(index, len(A)-1): 
      if A[i] > A[i+1]: return False
    return True

  # decreasing
  else:
    for i in range(index, len(A)-1): 
      if A[i+1] > A[i]: return False
    return True
  '''
  
# all leetcode tests pass as of 20th Oct 2019
