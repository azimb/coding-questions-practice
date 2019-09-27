'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Leetcode: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
YouTube: https://www.youtube.com/watch?v=RlXtTF34nnE

Approach:
    - the idea here is to do 2 binary searches, for the most optimal solution
    - do a binary search to find the target
    - once you found the target, you have to figure out:
        * am I looking for the first position, and is the target available in left half too?
        (if yes, do a binary search on left half)
        * am I looking for the last position, and is the target avaiable in the right half too?
        (if yes, do a binary search on the right half)
        
        ** if the target you found doesn't appear in it's right or left
            or does appear in it's right half but you are finiding FIRST position
            or does appear in it's left half but you are finding LAST position
            Then return the element
        
    - if the number doesn't equal to target, recursively binary search either left or right half
    (traditional binary search)
    
    - stop a search when the left index is bigger than the right index

Time complexity:
    - the first binary search will take O(log n) time
    - and the second binary search will also take O(log n) time
    - therefore, the space complexity is O(log n)
    
Space complexity:
    - the max depth of recursion will be O(log n)
    - so, the space complexity is O(log n)
'''

def searchRange(self, nums, target):
    left = 0
    right = len(nums) - 1
                            # first position                  # last position
    return [self.BST(nums, left, right, target, 0), self.BST(nums, left, right, target, 1)]

def BST(self, nums, left, right, target, position):
    if left > right: return -1

    mid = left + (right-left)/2

    # found the element we are looking for
    if nums[mid] == target:
        # we are looking for first position, but same element occurs in left half
        if position == 0 and self.is_valid_index(nums, mid - 1) and nums[mid] == nums[mid - 1]:
            # binary search ii -- left half to find starting index
            return self.BST(nums, left, mid - 1, target, position)

        # we are looking at last position, and same element occurs in right half
        if position == 1 and self.is_valid_index(nums, mid + 1) and nums[mid] == nums[mid + 1]:
            return self.BST(nums, mid + 1, right, target, position)

        # else, this is the index you are looking for
        return mid


    elif nums[mid] > target:
        # search in left half
        return self.BST(nums, left, mid - 1, target, position)


    else: # nums[mid] < target:
        # search in right half
        return self.BST(nums, mid + 1, right, target, position)

def is_valid_index(self, arr, index):
    return index >= 0 and index < len(arr)
