'''
Continuous Subarray Sum
Lc: https://leetcode.com/problems/continuous-subarray-sum/
Similar to: https://github.com/baghadiya/coding-questions-practice/blob/master/coding-questions-python/subarray-sum-equals-k.py

Approach:
  - similar to Subarray sum equals k
  - only trick is that (a+(n*x))%x is same as (a%x)
  * ex: in case of the array [23,2,6,4,7] the running sum is [23,25,31,35,42] and the remainders are [5,1,1,5,0]
  * we got remainder 5 at index 0 and at index 3
  * That means, in between these two indexes we must have added a number which is multiple of the k
  
Time complexity:
  - O(n) or linear as we traverse the array once
  
Space complexity:
  - the HashMap can contain upto min(n,k)min(n,k) different pairings
  - so, the space complexity is O(min(n,k))
'''

def checkSubarraySum(nums, k):
  # var for running sum, and map to track the index of where that sum occurred
  sum_map, cur_sum = {0:-1}, 0
  for i in range(len(nums)):
    cur_sum += nums[i]
    if k != 0: cur_sum %= k # trick here is to track the running-sum%k

    if cur_sum in sum_map and (i - sum_map[cur_sum]) > 1: return True # sum seen before and the subarray's size is >= 2
    if cur_sum not in sum_map: sum_map[cur_sum] = i # sum not seen before, add it to the map

  # didn't find a subarray of size >=2 that add upto to a multiple of k
  return False
        
# all leetcode tests pass as of 5th Nov 2019
