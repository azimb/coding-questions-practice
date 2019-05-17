#Find the nth smallest integer from a list
#The list is unsorted (obviously)

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

#Another approach is to maintain a heap and then "pop" n times and return the appropriate head
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