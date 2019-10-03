'''
LC: https://leetcode.com/problems/generate-parentheses/
YouTube: https://www.youtube.com/watch?v=sz1qaKt0KGQ

Approach:
  - backtracking
  - for each call we decide: 1. choices 2. constraints 3. goal
Time complexity: #TODO
Space complexity: O(n*2) -> O(n)
'''

def generateParenthesis(self, n):
        result = []
        self.generate_paran_recursive(n, n, [], result)
        return result
        
    
    def generate_paran_recursive(self, open, close, cur_str, result):
        # no more right or left brackets left, string is complete so append to result
        if open == 0 and close == 0: result.append("".join(cur_str))
        
        # if I can add a an open parantheses here to the current string
        # recursively call with the updated string, with 1 less number of open paranatheses that can be used
        if open > 0: self.generate_paran_recursive(open-1, close, cur_str[:] + ["("], result)
        
        # if I can add a a closing parantheses here to the current string
        # recursively call with the updated string, with 1 less number of closing paranatheses that can be used
        if close > open: self.generate_paran_recursive(open, close - 1, cur_str[:] + [")"], result)

# all leetcode tests pass
