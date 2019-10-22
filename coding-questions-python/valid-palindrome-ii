'''
LC: https://leetcode.com/problems/valid-palindrome-ii/
Complexity analysis: O(n) time complexity and O(1) space complexity
'''

def validPalindrome(self, s):
  def is_palindrome(s, i, j):
    while i < j:
      if s[i] != s[j]: return False
      i+=1; j-=1
    return True

  left, right = 0, len(s) - 1
  while left < right:
    if s[left] != s[right]: return is_palindrome(s,left+1,right) or is_palindrome(s,left,right-1)
    left += 1; right -= 1
  return True
  
  # all leetcode tests pass as of 21st Oct 2019
