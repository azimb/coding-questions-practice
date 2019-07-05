'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Leetcode problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Possible approach:
    - create a maximum tracker -- index i will store the max price of the stock from day i to the end
    - iterate backwards to record the maximum price so far in this maximum tracker
    - for each price, calculate profit by using the maximum selling price if sold in the remaining days
      (fetch this from the maximum tracker)

Runtime complexity:
    - two full iterations on the prices array
    - so O(N) runtime complexity

Space complexity:
    - storing an additional buffer (max_tracker) of size N
    - so O(N) storage complexity
'''

def maxProfit(prices):
    if not prices or len(prices) == 1: return -1
    max_profit = 0
    current_min = prices[0]

    for price in prices:
        current_min = min(current_min, price)
        current_profit = price - current_min
        max_profit = max(max_profit, current_profit)

    return max_profit

# all leetcode tests pass
# Runtime: 48 ms, faster than 79.95% of Python online submissions for Best Time to Buy and Sell Stock.

'''
#dynamic programming approach
def maxProfit(prices):

        # index i will store the max price of the stock from day i to the end
        max_tracker = [0 for x in range(len(prices))]

        # iterate backwards to record the maximum price so far
        current_max = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > current_max:
                current_max = prices[i]
            max_tracker[i] = current_max

        # for each price, calculate profit by using the maximum selling price if sold in the remaining days
        max_profit = 0
        for j in range(len(prices) - 1):
            current_profit = max_tracker[j + 1] - prices[j]
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
'''