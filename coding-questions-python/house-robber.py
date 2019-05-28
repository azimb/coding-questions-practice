'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security
system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Time complexity = linear?
Space complexity = O(N) where N = len of list
'''

def determineMaxProfit(houseList):
    if len(houseList) == 0:
        return 0
    elif len(houseList) == 1:
        return houseList[0]
    elif len(houseList) == 2:
        return max(houseList[0], houseList[1])
    else:
        return max(
            houseList[0] + determineMaxProfit(houseList[2:]),
            houseList[1] + determineMaxProfit(houseList[3:])
        )