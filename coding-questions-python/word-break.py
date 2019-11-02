'''
Word Break
LC: https://leetcode.com/problems/word-break/

Approach:
  - a recursive approach
  * when you find a word in the dictonary your input_str starts with,
    you can just check if the remaining_str can be made using the words in the dictionary.
    
  - in worst case, (just) recursion results in an exponential time complexity (O(2^n))
  (ex: think of the case "aaaab" with ["a", "aa", "aaa", "aaaa"]
  - so, we use memoization
  
Time and space complexity
(of memoized solution):
  - O(n^2) time complexity because n possibilities for start, and (at most) n end possibilities for each start
  (technically O(N^3) because hashing a string takes O(N) time)
  - O(n) space complexity because the depth of the recursion could go up to n.
'''

def wordBreak(self, s, wordDict):
  return self.wordbreak_recursive(s, set(wordDict), 0, {})
    
def wordbreak_recursive(self, s, word_set, start, cache):
  # the entire input string can be made using the dict words, so return True
  if start == len(s): return True

  # have we already looked at this subproblem before?
  if start in cache: return cache[start]

  ans = False
  # starting from start, explore each end value to check if s[start:end+1] can be made using a word in the dict
  for end in range(start, len(s)):
    # there is a word w in a dict st input_str starts with w
    if s[start:end+1] in word_set:
      # check if the remaining part of input_str can be made using word(s) in the dictionary
      if self.wordbreak_recursive(s, word_set, end + 1, cache): 
        ans = True
        break
  
  # cache the result for the subproblem so it can be used later
  cache[start] = ans
  return ans
  
# all leetcode tests pass as of 2nd Nov 2019
