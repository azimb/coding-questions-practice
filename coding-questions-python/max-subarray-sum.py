'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Leetcode: https://leetcode.com/problems/maximum-subarray/

Approach:
    - video: https://www.youtube.com/watch?v=2MmGzdiKR9Y&t=816s
    - Kadane's algorithm -- dynamic programming
    - idea is to calculate the max sub array sum ending at each index
    - this is a bottom up approach

    - for each elem, we have two options:
        * either use the current element to "extend" the max sum ending at the previous index
        * or forget about the the max sum till the previous index, and start the subarray from current index

    - which option is better?
    - you want max sum, so only start the subarray from current elem if it's value is bigger than the sum you get
    by extending/adding the current value to the max sum at previous index

    - a memo can be used to store the max subarray sum at each index
    - or, this can be done in constant space by using just two variables

Time complexity:
    - one pass
    - so, the time complexity is O(n) or linear

Space complexity:
    - just using two extra variables
    - so, the space complexity is O(1) or constant
'''

# constant space complexity solution
def max_subarray_sum(nums):
    # corner case -- no elems, max sum of any subarray is 0
    if len(nums) == 0: return 0

    # the first elem will be the max sum of any subarray ending at that index
    max_so_far = nums[0]
    max_ending_here = nums[0]

    # for each index, find the max sum of a subarray ending at that index
    # options: extend the previous sum by including the cur elem, or discard the prev sum and start fresh
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)

    # max_so_far is the maximum of sums ending at each index
    return max_so_far

# linear space complexity solution
def max_sum_array_sum_discarded(nums):
    memo = [0 for x in range(len(nums))]
    memo[0] = nums[0]

    for i in range(1, len(nums)):
        memo[i] = max(nums[i], nums[i] + memo[i-1])

    return max(memo)

# all leetcode tests pass
