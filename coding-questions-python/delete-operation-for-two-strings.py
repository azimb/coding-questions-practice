'''
LC: https://leetcode.com/problems/delete-operation-for-two-strings/
O(nm) time and space complexity using a 2D dp array
'''

def minDistance(self, word1, word2):
    # bottom up 2d array dynamic programming approach
    # O(mn) tme and space complexity

    # corner case -- both strings are empty
        if not word1 and not word2: return 0
        
        # dp_arr[i][j] will store the solution to subproblem word1[:i] word2[:j]
        dp_arr = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)]

        # min deletions with an empty string
        for i in range(len(dp_arr[0])):
            dp_arr[0][i] = i

        # min deletions with an empty string
        for i in range(len(dp_arr)):
            dp_arr[i][0] = i
        
        # use the solutions to smaller subproblems and go bottom up
        for row in range(1, len(dp_arr)):
            for col in range(1, len(dp_arr[row])):
                # last chars match
                if word2[row-1] == word1[col-1]:
                    # get the solution for the subproblem without these chars
                    dp_arr[row][col] = dp_arr[row-1][col-1]
                # don't match
                else:
                    # get the solutions to subprobelems a) last char of word1 is removed, b) last char of wrod2 is removed
                    # 1 (as we removed it) + min of the subproblems is your answer
                    dp_arr[row][col] = 1 + min( dp_arr[row-1][col], dp_arr[row][col-1] )
        
        # answer to the maximum global problem sits at the last cell
        return dp_arr[-1][-1]
        

        # top down memoization approach
        '''    
            return self.min_distance_recursive(word1, word2, {})


        def min_distance_recursive(self, word1, word2, memo):
            if word1 == word2: return 0

            if not word1: return len(word2)

            if not word2: return len(word1)

            if (word1, word2) in memo: return memo[(word1, word2)]

            # first chars match
            if word1[0] == word2[0]:
                return self.min_distance_recursive(word1[1:], word2[1:], memo)

            # don't match
            else:
                result = 1 + min(self.min_distance_recursive(word1, word2[1:], memo), self.min_distance_recursive(word1[1:], word2, memo))
                memo[(word1, word2)] = result
                return result

        '''
