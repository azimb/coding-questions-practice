'''
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
    without changing the relative order of the remaining characters.
    (eg, "ace" is a subsequence of "abcde" while "aec" is not).
    A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Leetcode: https://leetcode.com/problems/longest-common-subsequence/
YouTube: https://www.youtube.com/watch?v=ASoaQq66foQ

Approach:
    - the idea is to solve smaller subproblems optimally, and then use their answers to get the global optimal solution
    - a 2d array is used as a cache to store the sols to subproblems for substrings of different sizes of both strings

    visualization:
        ""  c1  c2  c3  c4 ...
        ""  0   x   x   x   x
        c1  0   x   x   x   x
        c2  0   x   x   x   x
        .   0   x   p   x   x   P is is the LCS("c1...c3", "c1...c2")
        .

        if two chars cn and cm match:
            -- solve 1 + LCS(cn removed from first str, cm removed from second str)
            -- that's your answer

        if they dont:
            -- solve for (cn removed from first str, second string as is)
            -- solve for (first string as is, cm removed from second str)
            -- max of them is your answer (you want the longest)

Runtime complexity:
    (n = length of str1, m = len of str2)
    - we will solve all the subproblems, and there are n*m subproblems
    - so, the time complexity is O(nm)

Space complexity:
    - we are caching n*m subproblems
    - so, the space complexity is O(nm)
'''

def longest_common_subsquence(text1, text2):
    # a 2d array that will cache all the subproblems
    # subprob_arr[x][y] stores "what is the longest common subsequence for c1, c2, ... x from str2 and
    #                                                                       c1, c2, ... y from str1
    subprob_arr = [[0 for x in range(len(text1) + 1)] for y in range(len(text2) + 1)]

    # longest common subsequence between any string and "" is 0
    # these are redundant, as the array was already initialized with 0s
    for i in range(len(subprob_arr)): subprob_arr[i][0] = 0 # code added for explaining that lcs("", anything) = 0
    for i in range(len(subprob_arr[0])): subprob_arr[0][i] = 0 # code added for explaining that lcs(anything, "") = 0


    # for substrings of diff lengths, try to match the last character
    # if the characters match, sol is 1 + answer to subprob(last char removed from both)
    # if the characters don't match, sol is the max of two subprobs:
    #   a) last char removed from str1, b) last char removed from str2
    for row in range(1, len(subprob_arr)):
        for col in range(1, len(subprob_arr[row])):
            # last characters match
            if text2[row - 1] == text1[col - 1]:
                subprob_arr[row][col] = 1 + subprob_arr[row - 1][col - 1]

            # last characters don't match don't match
            else:
                # subprob with char from str2 removed, char from str1 removed, respectively
                subprob_arr[row][col] = max(subprob_arr[row - 1][col], subprob_arr[row][col - 1])

    # global optimal solution
    return subprob_arr[-1][-1]

# all leetcode tests pass
