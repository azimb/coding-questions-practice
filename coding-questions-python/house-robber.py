'''
LC: https://leetcode.com/problems/house-robber/

For each house:
  a) rob current -- amount = cur_amount + max_profit until i-2
  b) dont't rob -- amount = max_profit at i-1
You want the maximum of the two.
O(n) time, O(1) space
```
def rob(nums):
  prev_max, cur_max = 0, 0
  for amount in nums: prev_max, cur_max = cur_max, max(cur_max, amount + prev_max)
  return cur_max
  
  # all leetcode tests pass
