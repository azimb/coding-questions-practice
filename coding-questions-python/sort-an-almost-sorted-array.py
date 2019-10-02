'''
Given an array of n elements, where each element is at most k away from its target position,
    devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7
    in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

GfG: https://www.geeksforgeeks.org/nearly-sorted-algorithm/
YouTube: https://www.youtube.com/watch?v=yQ84lk-EXTQ
'''

import heapq

def k_sorted(arr, k):
    # heap initially contains the first k+1 elems
    heap = arr[:k+1]
    heapq.heapify(heap)

    # for each index, find the smallest elem from the available options in the heap
    # for the next index, add the additional option to heap
    for i in range(len(arr)):
        arr[i] = heapq.heappop(heap)
        if i+k+1 < len(arr): heapq.heappush(heap, arr[i+k+1])

k = 3
arr = [2, 6, 3, 12, 56, 8]
k_sorted(arr, k)
print("Following is the sorted arr: ")
print(arr)
