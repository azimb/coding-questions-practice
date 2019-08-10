'''
Given a string, find the length of the longest substring without repeating characters.

Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:-
    - we can use a sliding window technique for this problem
    - keep "stretching" the window on the right and store each character in a set
    - update the size of max_length each time you stretch the window to the right
    - whenever you encounter a char that is already in the set, the current "window" doesn't contain a string with all unique characters
    - in this case, just "pull in" the left corner of the window and remove that character from the set

The idea is to:
    - check for unique by checking on the recently added character
    - the set reduces the processes of checking for the same substring multiple times

Rumtime complexity:
    - as the two corners of the "window" will visit each elem at most once
        the runtime complexity is O(N) in worst case

Space complexity:
    - the set will store the characters for the current window
    - suppose all the characters of the string are unique, then we will use O(N) additional space in worst case
'''

def longest_unique_substr(s):
    # corner cases
    if len(s) == 0 or len(s) == 1: return len(s)

    max_length = 0

    # two corner of the window
    start = end = 0

    # this set will store the chars of the current window
    substr_set = set()

    while end != len(s):
        # if the encountered char is unique for the current "window"
        # add it to the set and check for max_length
        if s[end] not in substr_set:
            substr_set.add(s[end])
            end += 1
            max_length = max(max_length, (end - start))

    # else if the encountered character is already present in the current "window"/substring
    # remove the first character from the substring/set
    else:
        substr_set.remove(s[start])
        start += 1

    return max_length

# all leetcode tests pass