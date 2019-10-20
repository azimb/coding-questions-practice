'''
LC: https://leetcode.com/problems/group-anagrams/

Approach:
  - two strings are anagram if their char counts are same
  (ex: tan, ant -> a:1, n:1, t:1)
  - group strings together in a hashmap beased on their char count

  - keys of hashmaps can't be hashmaps/lists as these types are unhashable
  - use a tuple instead, where (x,x,x,...,x,x) -> (#ofas, #ofbs,...,#ofzs)
            
Complexity analysis:
  - O(NK) time and space complexity
  where N = len of strs, K = len of longest str
'''

def group_anagrams(strs):
  output_map = collections.defaultdict(list) # hashmap to group strs together based on char count
  for word in strs: # for each word
    char_tuple = make_char_tuple(word) # make a tuple that denotes char count
    output_map[char_tuple].append(word) # add word to the appropriate group
  return output_map.values() # get groups from hashmap
    
def make_char_tuple(word):
  char_tuple = [0 for x in range(26)] # 26 chars in a lower-case string
  for char in word: char_tuple[ord(char) - ord('a')]+=1 # increment count at corret index based on char
  return tuple(char_tuple) # return list as a tuple, as lists are not hashable
  
# all leetcode tests pass as of 20th Oct 2019
