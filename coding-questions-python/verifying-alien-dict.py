'''
Verifying an Alien Dictionary
LC: https://leetcode.com/problems/verifying-an-alien-dictionary/

Approach:
  - we will check each word with it's right neighbour, and verify that the neighbour is bigger
  - to check if b is bigger than a:
    * we'll find the first different char, and assert that b[char] > a[char]
    * if no first difference is found, this means either a->startswith(b) or b->startswith(a)
      in this case, we assert that len(a) < len(b) because a must be lexicographically smaller 
 
Complexity analysis:
  - time complexity is O(N) where N = len(words)
  - space complexity is O(1) # fixme: not sure if this is correct
'''

def isAlienSorted(self, words, order):
  # index of each char in the alien sorted order will be maintained by this hashmap
  order_map = {}
  for i in range(len(order)): order_map[order[i]] = i

  # check whether all adjacent words a and b have the property a<=b
  for i in range(len(words)-1):
    # if the cur word is not smaller than the adjacent word, return False
    word_one, word_two = words[i], words[i+1]
    if not self.smaller(word_one, word_two, order_map): return False

  # checked all words, and didn't return False yet (ie all words follow the property) -- return True
  return True


def smaller(self, word_one, word_two, order_map):
  # compare each character of both words
  for i in range( min( len(word_one), len(word_two) ) ):
    # this is the first difference in the chars
    # make sure that char in word_one is smaller than the char in word_two
    if word_one[i] != word_two[i]: return order_map[word_one[i]] < order_map[word_two[i]]

  # characters matched (ex: app, apple or ex: apple, app)
  # make sure that word_one is shorter, which means it's lexicographically smaller 
  return len(word_one) < len(word_two)

# all leetcode tests pass as of 2nd Nov 2019
