'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

Leetcode: https://leetcode.com/problems/length-of-last-word/

Suggested approach:
    - just stripping, splitting, and getting the length of the last index should be fine
    - however this approach uses additional space that may be unnecessary

Better approach (no additional space):
    - iterate backwards and keep a track of the length until you see the first space that is not at the end of the sentence
    - note that a flag can be used to check if a non space character has been seen before
    - if the sentence contains no spaces (i.e. it's a single word), just return the length

Runtime complexity:
    - linear or O(N), as going through each char once

Space complexity:
    - constant or O(1), just using an integer to track the length
'''

def lengthOfLastWord(s):
    length = 0
    seenLetter = False
    for i in range(len(s)-1, -1, -1):
        if s[i] == " ":
            if seenLetter == True:
                return length
        else:
            seenLetter = True
            length += 1
    return length

# another simple approach -- linear time and constant space complexity
'''
def lengthOfLastWord(self, s):
    # find the first non-space char
    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":    
            # find the first space before this char
            for j in range(i-1, -1, -1): 
                if s[j] == " ": return i - j
            # no space before char(s), that means it's a single word
            return i+1
    # no chars, so len is 0
    return 0
'''

# tests
import unittest
class TestLengthOfLastWord(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(lengthOfLastWord("awesome Python"), 6)  # general case
        self.assertEqual(lengthOfLastWord("Programming"), 11)  # case with only one word
        self.assertEqual(lengthOfLastWord("Coding    "), 6)  # case with single word and spaces at the end
        self.assertEqual(lengthOfLastWord("I love making software     "), 8) # case with mutliple words and spaces at the end
        self.assertEqual(lengthOfLastWord("    "), 0)  # case with just spaces
        self.assertEqual(lengthOfLastWord(""), 0) #emopty string

unittest.main()

#all leetcode tests pass
