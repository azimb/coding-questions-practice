'''
LC: https://leetcode.com/problems/goat-latin/

Approach:
  - constraints are clearly defined
  - split and make an array of words
  - for each word:
    * add all chars in the output array
    * if it's the first character and not a vowel, skip that character
    * in the end if the first char was skipped, add that
    
Time and space complexity: #TODO
'''

def toGoatLatin(self, S):
  if not S: return ""
  
  vowels = set(['a', 'e', 'i', 'o', 'u'])
  output, As = [], 1

  for word in S.split():
      for i in range(len(word)):
          if i == 0 and word[i].lower() not in vowels: continue
          output.append(word[i])
      if word[0].lower() not in vowels: output.append(word[0])

      output.append("ma" + ("a"*As) + " ")
      As += 1

  return ("".join(output)).strip()
 
# all leetcode tests pass as of 12th Nov 2019
