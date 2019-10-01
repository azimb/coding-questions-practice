'''
LC: https://leetcode.com/problems/range-sum-query-immutable/
YouTube: https://www.youtube.com/watch?v=ZMOFmHBVEcg
'''

# pre-processing takes O(N) time, but then each call to sumRange is O(1) after that
# space complexity is O(N) due to the cache
class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        # use the helper method to generate a sum cache
        self.sum_cache = self.generate_running_sum_array(self.nums)

    def sumRange(self, i, j):
        # sum cache is indexed at 1, so get the sum at j + 1
        # subtracting sum at i (and not i+1) because i is inclusive, so we want to subtract the sum of nums from 0.. i-1 inclusive
        return self.sum_cache[j + 1] - self.sum_cache[i]

    def generate_running_sum_array(self, nums):
        # cache to store the running sum at each index
        # cache[i] denotes the sum of nums from 0 ... i-1 inclusive
        self.sum_cache = [0 for x in range(len(nums) + 1)]
        for i in range(len(nums)):
            # get the sum of at the previous index, and add the number at the current index
            self.sum_cache[i + 1] = self.sum_cache[i] + self.nums[i]

        return self.sum_cache

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
