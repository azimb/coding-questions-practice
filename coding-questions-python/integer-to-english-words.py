'''
LC: https://leetcode.com/problems/integer-to-english-words/
Solution inspired by: https://leetcode.com/problems/integer-to-english-words/discuss/70625/My-clean-Java-solution-very-easy-to-understand

Approach:
  - the idea is to grab the last 3 digits and convert it into english using a recursive helper method
  - this recursive method will break down the conversion of 3 digits into three parts:
    * number less than 20 (easy - use the array)
    * number less than 100 (grab the first digit, use the tens array, and then recursively process the second digit)
    * 3 digit number (grab the first digit and use the tens array and add "hundred", and then recursively process the last 2 digits)
 
Space time complexity analysis:
  # TODO
  
'''
class Solution(object):
  def __init__(self):
    self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    self.thousands = ["","Thousand","Million","Billion"]

  def numberToWords(self, num):
    if num == 0: return "Zero"

    # thousands index will track which group of 3 digits we are processing, and words is the result string
    thousands_index, words = 0, ""

    # keep going until there are digits to look at
    while num > 0:
      # grab last three digits, and convert them into english
      # use the correct postfix (ex: "million", "billion") and prepend it to the result
      if num%1000 != 0: words = self.helper(num%1000) + self.thousands[thousands_index] + " " + words
      # get rid of the last three digits, and progress the thousands_index
      num /= 1000; thousands_index+=1

    # get rid any unneccessary white spaces
    return words.strip()
        
        
  def helper(self, num):
    # base case
    if num == 0: return ""

    # num is less than 20, easy - use the array
    elif num < 20: return self.lessThan20[num] + " "

    # num is less than 100 - grab the first digit, use the tens array, and then recursively process the second digit
    elif num < 100: return self.tens[num/10] + " " + self.helper(num%10)
     
    # num is 3 digits - grab the first digit and use the tens array and add "hundred", and then recursively process the last 2 digits
    else: return self.lessThan20[num/100] + " Hundred " + self.helper(num%100)
    
# all leetcode tests pass as of 9th Nov 2019
