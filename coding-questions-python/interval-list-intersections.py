'''
Interval List Intersections
LC: https://leetcode.com/problems/interval-list-intersections/

Approach:
  - we will use the idea of merge intervals
  - consider the interval A[0] with the smallest endpoint
  - then A[0] can only intersect one interval in array B
  (if two intervals in B intersect A[0], then they both share the endpoint of A[0] -- 
  but intervals in B are disjoint, so this is not possible)

  So, the underlying algorithm follows the idea that:
  * if A[i]'s end point is smaller than B[j]'s end point, then A[i] can only intersect B[j]
  * after, we can discard A[i] since it cannot intersect anything else

  * similarly, if B[j]'s end point is smaller than A[i]'s end point, then B[j] can only intersect A[i]
  * so we then discard B[j]

  Tirck:
  * we use two pointers, i and j, to virtually manage "discarding"

Time and space complexity:
- O(M+N) time and O(M+N) space (includes the space required by the output array)
where M,N are the lengths of the two input arrays (A and B)
'''

def intervalIntersection(A, B):
  output = []  # output array stores the intersected intervals
  i = j = 0 # virtually manage "discarding" using these two pointers

  while i < len(A) and j < len(B):
    # check if A[i], B[j] intersect by genating [bigger starting point, smaller ending point]
    low = max( A[i][0],B[j][0] )
    high = min( A[i][1],B[j][1] )
    # if they don't intersect, start point will be bigger than ending point
    if low <= high: output.append([low, high])

    # the trick here is that if A[i] has smaller ending point, discard it as it cannot intersect with any other interval in B
    # similarly, if B[j] has smaller ending point, discard it as it cannot intersect with any other interval in A
    (i,j) = (i+1, j) if (A[i][1] < B[j][1]) else (i,j+1)

  return output
  
# all leetcode tests pass as of 3rd Nov 2019
