'''
LC: https://leetcode.com/problems/top-k-frequent-elements/

Approach:
  - inspired by bucket sort
  - we will have buckets 1,2,3,...i that denote the frequency and 
    each bucket will have the elems that appear in the array i many times
  - then we will loop from the end of the array of bucks (we want the most frequent elems)
    and extract k elements
    
  - how do we make the buckets:
    * use a hasmhmap to track frequency of each elem
    * loop through the map and store the elem in the bucket it belongs to
    (remember, bucket[i] is a list of items that appear i many times)
    
Time and space complexity analysis:
  - O(N) time and space complexity
'''

def topKFrequent(self, nums, k):
  # hashmap to track the frequency of each elem
  freq_map = Counter(nums)

  # groups_arr[i] is a list of all elements that has frequency i
  groups_arr = [None] * (len(nums) + 1)
  self.group_numbers(freq_map, groups_arr)

  # result will hold the k most frequent elements
  result = [0] * k
  self.extract_k(groups_arr, result)

  return result

def group_numbers(self, freq_map, groups_arr):
  # for each elem, add it to the list of the elems of the same frequency (or bucket)
  for num, freq in freq_map.items():
    if not groups_arr[freq]: groups_arr[freq] = [] 
    groups_arr[freq].append(num) 

def extract_k(self, groups_arr, result):
  # loop from the end of groups_arr, and grab k items for the result array
  index = len(result) - 1
  for i in range( len(groups_arr) - 1, -1, -1 ):
    if groups_arr[i]:
      for j in range(len(groups_arr[i])):
        if index < 0: break
        result[index] = groups_arr[i][j]
        index -= 1
        
# all leetcode tests pass as of 7th Nov 2019
