'''
LC: https://leetcode.com/problems/random-pick-with-weight/
YouTube (beautifully explained the question and the solution): https://www.youtube.com/watch?v=KAZM4tsH8aI

Clarifications for the question:
  - the idea is that you need to randomly pick an index
  - but the probability of each index getting picked up will depend on it's weight
  - for example: arr = [1,3,4,4]
   so we can visualize something like [w,x,x,x,y,y,y,y,z,z,z,z]
  - probability of picking up y/zz is the probability of picking index 2,3 is highest

Approach:
  - generate a running sum array
  ex: [1,3,4,4] -> [1,4,8,12]
  the final index holds the total weight
  
  - then generate a random number between 1 and running_sum_arr[-1]
  - finally, binary search for the random number (find insert position)
  
Time complexity:
  - O(N) to build the running sum array, and then O(log N) for each call to pickIndex()

Space complexity:
  - O(N) due to the running sum index
'''
class Solution(object):
  def __init__(self, w):
    self.running_weight = self.generate_running_weight(w)

  def pickIndex(self):
    r = random.randint(1, self.running_weight[-1])

    left, right = 0, len(self.running_weight) - 1
    while left <= right:
      mid = left + (right-left)/2
      if self.running_weight[mid] == r: return mid
      elif self.running_weight[mid] > r: right = mid - 1
      else: left = mid + 1

    return left

  def generate_running_weight(self, arr):
    running = [arr[0]]
    for i in range(1, len(arr)):
      running.append(arr[i]+running[i-1])
    return running
    
# all leetcode tests pass as of 7th Nov 2019
