'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Leetcode: https://leetcode.com/problems/climbing-stairs/

Approach:
    - at each step, you can make a choice
        * either you can take 1 step
        * or you can make take 2 steps
    - so, the number of ways to climb n stairs is just the number of ways to climb n-1 stairs + the number of ways
        to climb n-2 stairs
    - instead of making 2^n recursive calls, we can be more efficient by using a memo
    - or, we can reduce the extra space to O(1) by using just two variables

    - an approach identical to what was used to solve for nth fibonacci number
    - nth fibonacci/tribonacci: https://github.com/baghadiya/coding-questions-practice/blob/master/coding-questions-python/nth_tribonacci.py

Time complexity:
    - bottom up approach, start from 0 and going all the way to n
    - so the time complexity is O(n), or linear

Space complexity:
    - using two variables only
    - so the space complexity is O(1) or constant
'''

def climb_stairs(n):
    # base cases
    if n == 0 or n == 1: return 1

    # two variables to keep a track of climb_stairs(n-1), climb_stairs(n-2)
    one_before_last = 1
    last = 1

    # bottom up approach, go from 2 to n and calculate the cs(n) at each stair using the two previous values
    for i in range(2, n + 1):
        new = one_before_last + last
        one_before_last, last = last, new

    return last

# all leetcode tests pass
