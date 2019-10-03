'''
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Leetcode: https://leetcode.com/problems/coin-change-2/

Approach:
    - a dynamic programming bottom up approach
    - idea is to use a 2d array as a memo
    - cols will be amounts from 0..given_amount
    - each row will add a new coin to the list of coins being considered. ex: [], [c1], [c1,c2], [c1,c2,c3], ...
    - memo[row][col] = ways to make amount col, given the coins coins_arr[0:row-1]

Time complexity:
    - computing the ways for each each new addition of the coin
    - for each coin, computing the unique ways for each amount from 0..given amount
    - so, the time complexity is O(AC)

Space complexity:
    - a 2d array with A+1 cols and len(coins)+1 rows
    - so, the space complexity is O(AC)

YouTube video: https://www.youtube.com/watch?v=DJ4a7cmjZY0&t=66s
'''

def coin_change_ii(amount, coins):
    # dynamic programming using a 2d array
    '''
    cache visualization
             amount ...
     []      0 0 0 0 0
    [c1]     1 x x x x
  [c1,c2]    1 x x x x   P is number of ways to make amount 2, given [c1,c2,c3]
     .       1 x P x x
     .
     .

    For each row (ie for each new coin, you can decide if you want to use that coin or not)
    Number of ways to make amount a with the given coins [c1, c2, c3, ... cn] is
        (use coin cn)                                    +                 (don't use coin cn)
        (ways to make a-cn using [c1, c2, .. cn])        +    (ways to make a using [c1,c2, ... cn-1])

    '''

    # corner cases
    if amount == 0: return 1
    if len(coins) == 0: return 0

    # initialize the 2d array for dynamic programming
    # cols are the amounts from 0, 1, ... amount
    # rows are [], [c1], [c1,c2], [c1,c2,c3], [c1,c2,c3,...,cn]
    subproblems_arr = [[0 for x in range(amount + 1)] for y in range(len(coins) + 1)]

    # there is only 1 way to make amount 0, no matter what coins are given
    for i in range(len(subproblems_arr)):
        subproblems_arr[i][0] = 1

    # there is 0 ways to make any amount, when no coins are given
    for i in range(len(subproblems_arr[0])):
        subproblems_arr[0][i] = 0

    # for each new addition of coin to the list of coins, visit each amount from 0 to given_amount
    # there are two choices: include the coin, or exclude the coin
    # if the coin is excluded, get the subproblem for the same amount, with the current coin removed from the list of coins
    # if the coin in included, get the subproblem for amount-value_of_coin with the same list of coins
    # the addition of these two subproblems i
    for row in range(1, len(subproblems_arr)):
        for col in range(1, len(subproblems_arr[row])):

            # don't include this coin
            # ie, same amount, previous row (remove current coin from list of coins)
            ways_one = subproblems_arr[row - 1][col]
            ways_two = 0

            # include this coin
            # amount will be current_amount-coin's amount; and same row (keep current coin in the list of coins)
            if col >= coins[row - 1]:
                # print "looking at coin"
                # print coins[row-1]
                ways_two = subproblems_arr[row][col - coins[row - 1]]

            total_ways = ways_one + ways_two
            subproblems_arr[row][col] = total_ways

    # global optimal solution sits in the right most corner of the dp table
    return subproblems_arr[-1][-1]

# all leetcode tests pass
