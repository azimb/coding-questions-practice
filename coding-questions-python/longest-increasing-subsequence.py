'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

leetcode: https://leetcode.com/problems/longest-increasing-subsequence/
YouTube: https://www.youtube.com/watch?v=fV-TF4OvZpk

Approach:
    - we will use bottom up dynamic programming using a 1d array
    - dp_arr[i] represents the length of the longest increasing subsequence of the substring original_arr[0:i+1]


    - for each number we look at, we look at the answers to all the subproblems before that number
    visual: [a, b, c, d, e, f, g]
                      ^                         if we are currently solving the subproblem for [a,b,c,d],
                    cur                         we look at sol to subprobs [a], [a,b], [a,b,c]


    - check all indices j for the subproblems solved for the elems before my elem
        * if my number is bigger that the number at j, then let's get the answer to that subprob (at j)
            and add 1 to it (adding 1 because we are appending our elem, so length is increasing by 1)
        -- if the answer is smaller than the answer I already have for my subproblem (for ex: from considering another
            subsequence), then don't change the answer to my subproblem
        -- if it's bigger, update the answer to my subproblem

    - dp_arr[len(nums) - 1] will have the answer to global optimal subproblem

Time complexity:
    - for each index, we are considering all indices j before to try and append our elem to see if the len increases
    - so, 1 + 2 + 3 + 4 + .... + n-1 indices are checked
    - so, the the runtime complexity is O(n^2)

Space complexity:
    - a dp array of size len(nums)
    - so, space complexity is O(n)
'''


def lengthOfLIS(self, nums):
    # corner case for an empty list
    if len(nums) == 0: return 0

    # this variable will keep a running track of the global max length
    max_so_far = 1

    # dynamic programming 1d array for a bottom up approach
    # Each index records the answer to "what is the longest increasing subsequence ending at index i of the original array?"
    subproblems_arr = [1 for x in range(len(nums))]

    # for each index, test for the longest increasing subsequence
    for cur_num_index in range(1, len(nums)):
        # look at the solutins to subproblems for indixes before cur_num_index
        for subprob_index in range(0, cur_num_index):
            # make sure the elem is increasing/greater than the elem at the index we are checking the subproblem for
            if nums[cur_num_index] > nums[subprob_index]:
                # does extending that subsequnce yield us a length longer than what we already have
                subproblems_arr[cur_num_index] = max(subproblems_arr[cur_num_index], 1 + subproblems_arr[subprob_index])

        # update global max length if necessary
        max_so_far = max(max_so_far, subproblems_arr[cur_num_index])

    return max_so_far

# all leetcode tests pass
