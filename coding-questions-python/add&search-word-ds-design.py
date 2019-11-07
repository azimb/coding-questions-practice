'''
LC: https://leetcode.com/problems/add-and-search-word-data-structure-design/

Approach:
  - if we were to search just for words, we could use a hashset
  - but because we need to do (basic) pattern matching, we will use a trie
  - a trie is an ordered tree which is used to store a dynamic set where the keys are usually strings
  
Design:
  - trie map will store all the nodes that start a sentence
  - a trie with a sigle None child (in our case) denotes end of word
  
Complexity analysis:
# TODO

'''
class WordDictionary(object):
  def __init__(self):
    # init the trie data structure
    self.trie = {}

  def addWord(self, word):
    '''
    For each char, find the children set where it belongs.
    So, a word like abc will look something like this {a:{b:{c:{None:None}}}
    Note that c has a single child 'None' which denotes that c is the end of sentence.
    '''
    node = self.trie
    for char in word:
      if char not in node: node[char] = {}
      node = node[char]
    node[None] = None

  def search(self, word):
    def find(word, node):
      # already reached end of sentence, cannot search further
      if not node: return False
      # if no more chars to look for, verify end of sentence is reached
      if not word: return None in node
    
      # grab the first character, and save the reaminder of the word for recursion
      char, word = word[0], word[1:]
      
      # char is not a dot so it should be found in the set of nodes,
      # and the reaminder word must be made from it's set of children
      if char != ".":
        return char in node and find(word, node[char])

      # char is a dot, so we will look at all possible nodes in this set,
      # and check if reaminder word can be made from the possible node's set of children
      for possible in node:
        if find(word, node[possible]): return True
      # none of the nodes in this set can make the word, return False
      return False

    # initial call will search from entire word, starting from root
    return find(word, self.trie)
    
# all leetcode tests pass as of 7th Nov 2019
