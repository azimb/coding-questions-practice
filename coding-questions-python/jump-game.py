'''
LC: https://leetcode.com/problems/jump-game/
Approach:
  - for each index, we check is it's unreachable
  (if it is, we immediately return False)
  - then for the current index, we calculate what's the max distance we can reach from this index
  (if the max_reach is bigger or equal to the last index, we return True)
  Note: not returning anything after for loop means False 

  Complexity analysis: O(N) time and O(1) space

  Alternative solution(s): dynamic programming
  https://leetcode.com/problems/jump-game/solution/
'''
def can_jump(nums):
  max_reach = 0
  for i in range(len(nums)):
    if i > max_reach: return False # index is unreachable
    max_reach = max(max_reach, i+nums[i]) # what's the max reach from current index 
    if max_reach >= len(nums)-1: return True # if max_reach >= last index, we can reach last index

# all leetcode tests pass as of 20th Oct 2019
