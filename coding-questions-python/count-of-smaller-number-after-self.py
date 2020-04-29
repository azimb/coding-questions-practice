'''
LC: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

Approach:
    - we will essentially do a merge sort, but tweak the algorithm slightly to track how many smaller 
    numbers are to the right of a number during a merge operation
    - most importantly, we maintain a variable called right_counter during each merge operation
    - this variable denotes the number of elements in *the right sorted part that are smaller 
    than the next element from the left sorted part*
    
    - why are they smaller than the next element from the left sorted part? 
    - this is because they come before (the next element from the left sorted part) in the merged array
    
    - when the next number is merged from the left sorted array, we increase count[ index of the number ] by rightcount
    - this is because we know already know there were previously 'rightcount' number of elements that are smaller than it
    
    
Complexity analysis:
    - same as merge sort: O(n log(n)) time and O(n) space complexity 
    
Refer to the post and comments on the following to better understand the approach:
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76583/11ms-JAVA-solution-using-merge-sort-with-explanation

Refer to the post (old version) to look at a coding example:
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
'''

def countSmaller(nums):
    # edge case -- empty list
    if len(nums) == 0: return []
    
    # we need this array because we need to remember the original index of each elem
    nums_with_index = []
    for i in range(len(nums)): nums_with_index.append((nums[i], i))
    
    # count[i] = # of elems to the right of nums[i] that are smaller than nums[i]
    count = [0 for _ in range(len(nums))]
    
    # this variation of merge sort populates the count array
    custom_sort(nums_with_index, count)
    return count


def custom_sort(arr, cnt):
    # base case -- a list of size 1 is already merged
    if len(arr) == 1: return arr

    # recursively sort left and right half
    mid = (len(arr)+1)/2
    left = custom_sort(arr[:mid], cnt)
    right = custom_sort(arr[mid:], cnt)
    
    # merge the left and the right half
    # variation: keeping a track of "how many elems from right are smaller than next elem in left "
    merged = []
    left_p = right_p = right_counter = 0
    
    # while there is at least one elem to be merged
    while left_p < len(left) or right_p < len(right):
        # pointer fell off right list or elem in left list is smaller than right list's elem
        if right_p == len(right) or (left_p < len(left) and left[left_p][0] <= right[right_p][0]):
            merged.append(left[left_p])
            # appending the next elem from left
            # we already have a track of how many elems to the right are smaller than this elem
            index = left[left_p][1]
            cnt[index] += right_counter
            left_p += 1
            
        # pointer fell off left list or elem in right list is smaller than left list's elem
        else:
            merged.append(right[right_p])
            # another smaller item "to the right of" the next elem from left
            right_counter += 1
            right_p += 1
    
    # merged the two sorted half, return this to be used by the parent call (regular mergesort)
    return merged
    
# all leetcode tests pass as of 29th April 2020