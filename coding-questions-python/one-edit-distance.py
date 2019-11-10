'''
One Edit Distance (premium)
LC: https://leetcode.com/problems/one-edit-distance/

Given two strings s and t, determine if they are both one edit distance apart.
Note: 
There are 3 possiblities to satisify one edit distance apart:
Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t

Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Example 2:
Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.

Example 3:
Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.

Appraoch:
  - if the difference in the lengths of the two strings is more than one, then they couldn't be one edit away strings
  - assume that s is smaller than t
  
  - if there is no differences between the first len(s) characters, only two situations are possible :
    * the strings are equal
    * the strings are one edit away distance
    
  - what if there is a different character so that s[i] != t[i]
    * if the strings are of the same length, all next characters should be equal to keep one edit away distance
        To verify it, one has to compare the substrings of s and t both starting from the i + 1th character
    * if t is one character longer than s, the additional character t[i] should be the only difference between both strings
        To verify it, one has to compare a substring of s starting from the ith character and a substring of t 
        starting from the i + 1th character
   
Time complexity:
  - O(N) in the worst case where the lengths of the string are almost equal
  - O(1) in the best case where len t - len s > 1
  
Space complexity:
  - O(N) as slicing strings (strings are immuatable in Python)
  # TODO: verify this
'''

def isOneEditDistance(self, s, t):
  sn, tn = len(s), len(t)

  # ensure that s is shorter than t
  if sn > tn: return self.isOneEditDistance(t,s)

  # strings cannot be 1 edit distance away if the len difference is more than 1
  if tn - sn > 1: return False

  for i in range(sn):
    # char mismatch
    if s[i] != t[i]:
      # if lens are same, remaining chars from both strings must match (replace)
      if sn == tn: return s[i+1:] == t[i+1:]
      # t is longer, so skip one char in t and compare remaining chars (add/remove)
      else: return s[i:] == t[i+1:]

  # no char mismatch -- verify that t is 1 char longer than s
  return tn == sn+1
  
# all leetcode tests pass as of 9h Nov 2019
