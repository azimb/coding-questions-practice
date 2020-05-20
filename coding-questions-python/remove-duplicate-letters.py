'''
LC: https://leetcode.com/problems/remove-duplicate-letters/

Approach:
    - we are essentially building the answer as a stack
    - for each new character we see, we only append it to the string if we have not already used it
    (as we want unique characters only)

    - IMP: before appending:
    If the character(s) before this character c are bigger, and they appear again later in the string_input,
    we pop them off.
    * we want the lexicographically smallest, so smaller character must appear before the bigger ones
    * we can add them later when they reappear

Complexity analysis:
    - since each character is explored at most twice (once when we push to stack, and one if we pop form stack),
    the time complexity of this algorithm is O(N)

    - worst case scenario: all characters are unique, the stack and answer array will take O(N) spoace
    - so, the space complexity of this algorithm is O(N)

Video explanation for the same: https://www.youtube.com/watch?v=zhU7yshJvb0
More details on the same approach: https://leetcode.com/problems/remove-duplicate-letters/discuss/76769/Java-solution-using-Stack-with-comments
'''


from collections import Counter
def removeDuplicateLetters(s):
    '''
    # O(n log n) time
    # return "".join( sorted( list( set( s ) ) ) )
    '''

    freq = Counter(s)  # occurrence frequency of each unique character
    used = set([])  # hashtable to track the used characters
    result = []  # stack that will eventually build the answer

    for char in s:
        if char in used:
            freq[char] -= 1  # looked at the character, reduce it's frequency
            continue  # character already used

        # for characters that appear before the current character
        # if their larger and can appear later (freq  > 0), pop them for now, and mark as unused
        # this will ensure we have the lexicographically smallest answer
        while result and result[-1] > char and freq[result[-1]] > 0: used.remove(result.pop())

        result.append(char)  # append the character to the answer stack
        used.add(char)  # mark the character as used
        freq[char] -= 1  # looked at the character, reduce it's frequency

    return "".join(result)  # convert the stack into a string and return

# all leetcode tests pass as of May 19 2020
