'''
Coin change I (dp)

You are given coins of different denominations and a total amount of money amount. Write a function to compute the
    fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
    combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Approach:
    - a bottom up, dynamic programming approach
    - the idea is to solve subporblems optimally, so that the results of those subproblems can be used to solve
        the global optimal solution
    - we will use a 1d array as a memo, memo[i] = min number of ways to make to make amount i

    - the trick is to first calculate the fewest # of coins to make amount = 0 using the list of coins given
    - then compute the minimum # of coins to make amount=1, then amount=2, etc. until we reach amount = given_amount

    - for each amount, loop through the available coins
    - for each coin, you have two choices:
        * either don't take the coin (subproblem for same amount, excluding the coin)
        * or take the coin ( 1 + subproblem for give_amount - value of coin)
        (we add 1 because we are using the current coin)

    - the minimum of these subproblems is the answer to our problem for the given amount

Time complexity:
    - Given amount A and number of coins C
    - for each amount 0...A, we try all coins C
    - so, the time complexity is O(AC)

Space complexity:
    - 1d array as a memo, memo[i] = min number of ways to make to make amount i
    - size of array will be amount + 1
    - so, the space complexity is O(A)
'''

def coin_change_i(coins, amount):
    # dynamic programming
    # [subproblem for amount = 0, subproblem for amount = 1, 2, 3, 4, ...]

    # initializing with amount+1 at each index so that we can correct use the min function for the first coin
    subproblem_arr = [amount + 1 for x in range(amount + 1)]

    # min number of ways to make amount 0 is 0
    subproblem_arr[0] = 0

    # for eahc amount, consider all given coins
    for i in range(len(subproblem_arr)):

        # for each coin, explore the two option
        for coin in coins:
            # if the value of the coin is bigger than the current amount, skip the coin
            if i < coin: continue
            new_amount = i - coin

            # case where are are including the coin
            coins_one = 1 + subproblem_arr[i - coin]

            # case where we are excluding the coin
            coins_two = subproblem_arr[i]

            # min of the two options is what you want for your current amount
            min_coins_for_subproblem = min(coins_one, coins_two)
            subproblem_arr[i] = min_coins_for_subproblem

    # check if it's possible to make amount using the given coins
    possible = subproblem_arr[-1]
    if possible == amount + 1: return -1
    return possible

# all leetcode tests pass
