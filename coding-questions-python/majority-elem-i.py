'''
Majority Element I
LC: https://leetcode.com/problems/majority-element/

Boyer-Moore Voting Algorithm:
  - intuition: If we had some way of counting instances of the majority element as +1+1 and instances of any other element as -1−1, 
    summing them would make it obvious that the majority element is indeed the majority element
  - we maintain a count, which is incremented whenever we see an instance of our current candidate for majority element and 
    decremented whenever we see anything else
  - whenever count equals 0, we effectively forget about everything in nums up to  the current index and consider the current number 
    as the candidate for majority element
   
Time and space complexity: O(N) and O(1)
'''

def majorityElement(self, nums):
  majority_elem, frequency = None, 0
  
  for num in nums:
      if not frequency: majority_elem, frequency = num, frequency+1  # choose new cadidate
      else: frequency = frequency + 1 if num == majority_elem else frequency - 1  # is the cur_num the same as our candidate?

  return majority_elem  # frequency wouldn't be 0 at the end when the majority elem is our candidate
  
  # all leetcode tests pass as of 12th Oct 2019
