'''
LC: https://leetcode.com/problems/kth-largest-element-in-an-array/
YouTube: https://www.youtube.com/watch?v=hGK_5n81drs&t=1519s

O(N) time complexity (avg case), O(1) space complexity
'''

import random

def findKthLargest(self, nums, k):
    # *remember: kth larget elemnt will sit at the index: n - k
    n = len(nums)

    # boundaries of our partition space
    left, right = 0, len(nums) - 1

    while left <= right:
        # choose a random pivot
        choosen_pivot_index = random.randint(left, right)

        # do the partitioning to get back the final index of the pivot
        final_pivot_index = self.partition(nums, left, right, choosen_pivot_index)

        # is the pivot sitting at the index we desire?
        if final_pivot_index == (n-k): return nums[final_pivot_index]

        # kth largest must be in the left parition
        elif final_pivot_index > (n-k): right = final_pivot_index - 1

        # kth largest must be in the right parition
        else: left = final_pivot_index + 1

    # unreachable
    return -1


# parition sub-routine, also used by QuickSort    
def partition(self, nums, left, right, pivot_index):

    # grab the value at the pivot index
    pivot = nums[pivot_index]

    # move the item at the pivot index out of the way
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

    # tail index of elements lesses than the pivot
    tail = left

    # iterate from the left bound to right-1
    for i in range(left, right):
        # if item < pivot, move it to the section of the items less than the pivot
        if nums[i] < pivot:
            nums[tail], nums[i] = nums[i], nums[tail]
            tail += 1

    # after the partioning, make a sandwich by placing the pivot item at the end of the tail
    # as the elems before the tail are the items less than the pivot
    nums[tail], nums[right] = nums[right], nums[tail]

    # return the final index of the pivot
    return tail

# all leetcode tests pass, as of Oct 6th 2019
