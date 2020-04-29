'''
LC: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Approach:
	- this problem can be easily converted to "Kth Smallest Number in N Sorted Lists"
	- as each row (or column) of the given matrix can be seen as a sorted list, we essentially need to 
	find the "Kth smallest number in ‘N’ sorted lists" where N = # of rows
	
Algorithm:
	- we first build a min_heap with first elements of each row
	- we look k times, and in each iteration, we pop an element and push it's right neighbour (col + 1) 
	into the heap
	- as we need to find the neighbour of each elem, we store the elem in the heap with it's row and 
	col number from the matrix
	
Complexity analysis:
	- we first build a min_heap with element at index 0 of each row of the N lists -- 
		this takes O(N * log(N)) time
	- we push k-1 elements into the heap (k while loop iterations - push neighbour in each iteration 
		except last) -- this takes O(K * log(N)) time
	- so, the time complexity is O(N * log(N) + K * log(N)) *
	* verify this

	- we will store at most N elements in the heap at any point in times
	- so, the space complexity is O(N)
	
Inspired by: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
'''

import heapq

def kthSmallest( matrix, k):
	# will maintain the N elements at any point in time
	min_heap = []
	heapq.heapify(min_heap)
	
	# put first elem of each of the N sorted lists (each row) in the heap
	# each elem should be accompanied by it's row, col so that it's neighbour can later by determined
	for i in range(len(matrix)): heapq.heappush(min_heap, (matrix[i][0], (i, 0)))
	
	
	# remove k elem from the heap -- the kth removal will be the kth smallest elem
	count = 0
	while min_heap:
		top = heapq.heappop(min_heap)
		elem, coords = top[0], top[1]
		count += 1
		
		# kth smallest elem
		if count == k: return elem
		
		# neighbour (in the next col) exists
		n_coords = (coords[0], coords[1] + 1)
		if n_coords[1] < len(matrix[0]):
			neighbour = matrix[n_coords[0]][n_coords[1]]
			# append the right neighbour
			heapq.heappush( min_heap, (neighbour,n_coords) )
	
	# only reaches here when k > N where N = # of elems in the matrix
	return -1

# all leetcode tests pass as of 28th April 2020