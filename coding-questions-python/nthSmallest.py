#Find the nth smallest integer from a list
#The list is unsorted (obviously)
#Looks like a leetcode medium problem

import heapq

#lets find the smallest number first
def findSmallest(list):
	#edge case: empty list
	if len(list) == 0:
		return None
		
	#usual case 
	#note that this also works for the special case of singleton
	smallest = list[0]
	for elem in list:
		if elem < smallest:
			smallest = elem
	return smallest
			

#One approach is to find the smallest, remove it, and then keep going for n times
#This is very inefficient -- runtime ~ O(n*L) where n is the nth num (nth smallest) 
#  and L is the length of the argument 

#Another approach is to sort the array and use the appropriate index to return the corrent values
#This will be 0(n log n) runtime where n is the len of the list
#The space complexity will depend on the sorting algorithm used and if it sorts in place
#Assume merge sort so O(n) space complexity

#Another approach is to maintain a heap and then "pop" n times and return the appropriate head
#Same time and space complexity as approach two (line 25)
#O(nlogn) time (avg case) and O(n) space (worst case)
def findNthSmallest(list, n):
	#error checking 
	if n> len(list) or n < 1:
		return None;
		
	heapq.heapify(list)
	for dummy in range(n-1):
		heapq.heappop(list)
	
	return heapq.heappop(list)
	
	
#test cases
print(findNthSmallest([3,2,4,1,6,7], 1)) #must return 1
print(findNthSmallest([3,2,4,1,6,7], 5)) #must return 6
print(findNthSmallest([3,2,4,1,6,7], 0)) #must return None
print(findNthSmallest([3,2,4,1,6,7], 6)) #must return 7
print(findNthSmallest([3,2,4,1,6,7], 8)) #must return None