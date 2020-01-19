'''
LC: https://leetcode.com/problems/excel-sheet-column-number/

Approach:
  - this problem is basically asking you to convert from base 26 to base 10
  - for ex: "BE" just corresponds to 2 * (26**1) + 5 * (26**0)
  - to make things simpler, we will reverse the string and start with power 0
  
Time complexity:
  - we will do a single pass on the input/column name
  - so the time complexity is linear of O(N) where N = # of chars in the input string

Space complexity:
  - we are reversing the string, so the space complexity is linear or O(N)
'''

 def titleToNumber(self, s):
  # reversing the column name to make things simpler
  col_name, col_num = s[::-1], 0
  # enumerate adds counter to iterable, ex: "BE" -> B as 0, and E as 1 
  for exp, char in enumerate(col_name):
      # subtracting ord('A') and adding 1 because we want numbers 1, 2, ... , 26
      col_num += (26 ** exp) * (ord(char) - ord('A') + 1)
  return col_num

  # this method generates and 
  '''
  alphabets = dict(zip(string.ascii_uppercase, range(1,27)))
  col_name, col_num = s[::-1], 0
  for i in range(len(col_name)): col_num += alphabets[col_name[i]] * (26**i)
  return col_num

  '''

# all leetcode tests pass as of 18th Jan 2020
