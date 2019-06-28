'''
Approach (recursion):
    - at each step, look at all combinations, i.e. 1 and 2
    - size of the recursion tree will be 2^n
    - so time complexity will be O(2^n)
    - space complexity is O(n) as the dept of recursion can go up to n

Approach (recursion + memoization):
    - same approach as above
    - along with maintaining a dict to store + reuse results
    - size of the recursion tree can go upto n #TODO: understand this
    - so time complexity will be O(n)
    - space complexity is also O(n) as the dept of recursion can go up to n

Dynamic Programming Approach:
    - this problem contains the optimal substructure property
    (optimal solution can be constructed from optimal sols of it's subproblems)
    - one can reach ith step by doing:
        * taking a step step from (i-1)th step
        * taking two steps from (i-2)th step
    - so, total number of ways to reach ith step is the sum of ways to reach
        (i-1)th step and ways to reach (i-2)th step
    - if step[i] denotes the number of ways to reach the ith step, then
        step[i] = step[i-1] + step[i-2]
    - TODO: time and space complexity
'''


def climb_stairs(n):
    return climb_stairs_r(n, {})

def climb_stairs_r(n, memo):
    if n is 0 or n is 1 or n is 2:
        return n
    if n in memo:
        return memo[n]
    result = climb_stairs_r(n-1, memo) + climb_stairs_r(n-2, memo)
    memo[n] = result
    return result

def climb_stairs_dp(n):
    if n is 0 or n is 1 or n is 2:
        return n

    ways = [0 for x in range(n+1)]
    for i in range(3):
        ways[i] = i

    for i in range(3, n+1):
        ways[i] = ways[i-1] + ways[i-2]
    return ways[n]


#tests

#all leetcode tests pass
#Runtime: 8 ms, faster than 98.92% of Python online submissions for Climbing Stairs.
