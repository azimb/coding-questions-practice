'''
LC: https://leetcode.com/problems/backspace-string-compare/
'''

# alternative solution uses two stacks, one for each string
# while the time complexity is the same, this auxiliary storage leads to a O(m+n) space complexity

# O(m+n) time, and O(1) space complexity solution
'''
When writing a character, it may or may not be part of the final string depending on how many backspace keystrokes
occur in the future.
If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen, 
and therefore whether the result includes our character.
Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped.
If a character isn't skipped, it is part of the final answer.
'''
def backspace_string_compare(S, T):
  skipS = skipT = 0
        i, j = len(S) - 1, len(T) - 1
        
        # while there are chars in S or T
        while i >= 0 or j >= 0:
            # find position of next possible char in S
            while i >= 0:
                if S[i] =='#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else: break
            
            # find the position of next possible char in T
            while j >= 0:
                if T[j] =='#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else: break
            # do the two actual characters match?
            if i >= 0 and j >= 0 and S[i] != T[j]: return False
            
            # comparing a char with nothing?
            if (i >= 0) != (j >= 0): return False
            
            i -= 1
            j -= 1
        
        return True
        
# all leetcode tests pass
