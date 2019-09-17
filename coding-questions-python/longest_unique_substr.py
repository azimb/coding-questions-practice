'''
Given a string, find the length of the longest substring without repeating characters.
Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:
    - we will use a sliding window technique for this question
    - the idea is to understand that the current elem will contribute to the length of the longest unique substring
        if it's not already present in the current longest unique substring

    - two pointers start and end will maintain the window
    - the elements of the window will be stored in a HashSet
    - if the elem at end is not present in the window, add it to the window
        and update the length of the longest length (if applicable)
    - if it is, start removing the elements at the "start" until it removes the current element at end
    - keep doing this until end pointer falls off the string

Time complexity:
    - the start pointer will "touch" each element at most once
    - the end pointer will "touch" each element at most once
    - we are doing at most two iterations
    - so, the time complexity is O(n) or linear

Space complexity:
    - the set stores the elems currently present in the window
    - in the worst case, when the entire string is unique, the set will hold all the characters of the string
    - so, the space complexity is O(n) or linear
'''

def length_of_longest_unique_substring(s):
    # start and end pointers are the two boundaries of the window
    start = end = 0

    # this HashSet will record the elements of the current window
    current_substr = set()
    longest_length = 0

    while end != len(s):
        # if the char at end is already in the window
        # remove the chat at start from the window, and increment start
        if s[end] in current_substr:
            current_substr.remove(s[start])
            start += 1

        # if the char at end is not already in the window,
        # add it to window and update max_length if applicable, and increment end
        else:
            current_substr.add(s[end])
            longest_length = max(longest_length, len(current_substr))
            end += 1

    return longest_length

# all leetcode tests pass