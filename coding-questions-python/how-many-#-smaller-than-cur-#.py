'''
LC: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Approach:
    - we are already told the range of the given numbers is between 1 and 100
    - so we can easily count each number and sum their prefix and dump

Complexity Analysis:
    - O(n) time and space complexity
'''

def smallerNumbersThanCurrent(nums):
    # we are given the range 1-100
    # so this array counts how many times each number appears in the nums array    
    count = [0] * 101
    for num in nums: count[num] += 1
        
    # running sum - count[i] will be equal to number of numbers less than or equal to i
    for i in range(1, len(count)): count[i] += count[i-1]

    # for each num in nums, count[num-1] = # of elems less than or equal to num-1
    # this is the same as # of elems less than num
    result = []
    for num in nums: result.append( count[num-1] if num else 0 )
    return result   
        
# all leetcode tests pass as of 29th April 2020