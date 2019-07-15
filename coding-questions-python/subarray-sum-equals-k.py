'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays
    whose sum equals to k.

Leetcode: https://leetcode.com/problems/subarray-sum-equals-k/
'''

def subarray_sum_equals_k(nums, k):
    '''
    The idea is to keep a track of running total.
    Straight forward scenario: running total is equal to k, then just increment the num of subarrays with sum k by 1
    Interesting case: if (cur_sum - k) is in the map, we know that ( (cur_sum - k) - cur_sum ) will give us
        a subarray of sum k. Then increament the counter by the number of times we have seen (cur_sum - k).
    Each of these running totals must be then added to the map (or if it's already in the map, the value must be incremented).

    Runtime complexity is linear (or O(N)) as we are "touching" each element at most once
    Space complexity is linear (or O(N)) in worst case where all elems are unique and all of them are added to the map
    '''

    # TODO: edge case is failing (needs a fix)
    # input : [0,0,0,0,0,0,0,0,0,0], 0
    # expected output: 55, actual output: 10

    # =================================================================================
    # SOLUTION BEGINS HERE
    # =================================================================================

    # cur_sum will keep a track of the running total (or sum after adding each elem)
    # sum_equals_k will keep a track of the # of subarrays equaling k
    cur_sum = sum_equals_k = 0

    # sum_tracker map will store each cur_sum along with the number of times we have seen it
    # this will be useful when we check if (cur_sum - k) is in the map
    # suppose (cur_sum - k) is in the map, then we know that ( (cur_sum - k) - cur_sum ) will give us a subarray of sum k
    sum_tracker = {}

    # iterate over all the elems
    for num in nums:
        cur_sum += num

        # suppose the sum of the elems is k
        if cur_sum == k:
            sum_equals_k += 1

        # suppose(cur_sum - k) is in sum_tracker, it's val will be equal to the num of subarrays of sum k we can make
        # using these two
        elif (cur_sum - k) in sum_tracker:
            sum_equals_k += sum_tracker[cur_sum - k]

        # check if a key for cur_sum exits in sum_tracker
        # suppose it does, then the val will be increment by 1, otherwise val is 1
        if cur_sum in sum_tracker:
            sum_tracker[cur_sum] = sum_tracker[cur_sum] + 1
        else:
            sum_tracker[cur_sum] = 1

    # sum_equals_k is the number of subarrays that add up to k
    return sum_equals_k