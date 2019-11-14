'''
LC: https://leetcode.com/problems/decode-ways/
YouTube: https://www.youtube.com/watch?v=YcJTyrG3bZs

Approach:
  - top down recursion with memoization
  - at each step, we can decode either 1 digit, or 2 digits
  
Time and space complexity: O(N)
'''

def numDecodings(self, s):
  return self.decode_recursive(s, 0, {})

def decode_recursive(self, s, index, cache):
  if index == len(s): return 1

  if index in cache: return cache[index]

  ways = 0
  if s[index] > '0': ways += self.decode_recursive(s, index + 1, cache)

  if index + 1 < len(s) and ( "1" <= s[index: index+2]  <= "26"):
    ways += self.decode_recursive(s, index + 2, cache)

  cache[index] = ways
  return ways
 
# all leetcode tests pass as of 13th Nov 2019
