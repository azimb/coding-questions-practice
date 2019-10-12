'''
Subarray Sum Equals K
LC: https://leetcode.com/problems/subarray-sum-equals-k/
'''

def subarray-sum-equals-k(nums, k):
  '''
  if the cumulative sum upto two indices, say i and j is at a difference of kk 
  i.e. if sum[i] - sum[j] = k, the sum of elements lying between indices i and j is k
  '''
  subarray_counter = cur_sum = 0
  cum_sum_map = {0:1}
  
  # for each elem in arr, add it to the cumulative sum
  for num in arr:
      cur_sum += num
      # if current cumulative sum - k exists in the map, then the sum of the subarray between these is k
      if cur_sum - k in cum_sum_map: subarray_counter += cum_sum_map[cur_sum-k]
      # have we already seen this cumulative sum before? If yes, increament it's frequency (otherwise default freq)
      if cur_sum in cum_sum_map: cum_sum_map[cur_sum] += 1
      else:cum_sum_map[cur_sum] = 1

  return subarray_counter
  
# all leetcode tests pass as of Oct 12th 2019
