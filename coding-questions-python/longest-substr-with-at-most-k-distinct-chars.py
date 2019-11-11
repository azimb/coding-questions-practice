'''
Longest Substring with at most K distinct Characters (Premium)
LC: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

Approach:
  - an approach very similar to that of Longest Substring with all Unique Characters
    https://github.com/baghadiya/coding-questions-practice/blob/master/coding-questions-python/longest_unique_substr.py
    
  - basically:
    * move sliding window along the string
    * keep not more than k distinct characters in the window
    * and update max substring length at each step
    
Time and space complexity:
  - the start and end pointer will visit each elem at most once
  - so the time complexity is O(N) or linear
  
Space complexity:
  - O(K) space is used for the widow of K distinct characters
'''

from collections import Counter
def lengthOfLongestSubstringKDistinct(self, s, k):
    # two boundaries of the window
    start, end = 0,0
    # hashmap as a window, and max_len to track the result
    window, max_len = Counter(), 0
    
    # try to maximize the window, so until end reaches the last elem
    while end < len(s):
        # add a new elem to the window
        window[s[end]] += 1; end += 1
        
        # if windows size is greater than the # of distinct chars allowed
        if len(window) > k:
            # remove the char at start and reduce the size of the window
            window[s[start]] -= 1
            if window[s[start]] == 0: del window[s[start]]
            
            # increment the start pointer, as the elem at start has been removed
            start += 1

        # update the max length based on the width of the window
        max_len = max(max_len, end - start)

    return max_len
    
# all leetcode tests pass as of 10th Nov 2019
