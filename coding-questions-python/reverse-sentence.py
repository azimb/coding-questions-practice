'''
Given a sentence represented by a c-string (char array), reverse the sentence in place.
Ex: ['c','s',' ','i','s',' ','a','w','e','s','o','m','e']
    must result in ['a','w','e','s','o','m','e',' ','i','s',' ','c','s']

Idea:
    - reverse the entire c-string
    - then reverse individual words
    - runtime complexity: O(N) where N is the length of the c-string
    - constant ( O(1) ) storage complexity
'''

def reverseSentence(cString):
    #first reverse the entire c-string
    #myReverse(cString, 0, len(cString)-1)

    #reverse the c-string using using the built-in reverse method
    #it reverses the list in place
    cString.reverse()

    # let's now reverse the individual words
    start = end = 0
    while end < len(cString) - 1:
        while cString[end] != ' ':
            end += 1
            if end == len(cString) - 1:
                end += 1
                break

        myReverse(cString, start, end-1)
        start, end = end + 1, end + 1
    return cString

def myReverse(cString, u, v):
    while (u < v):
        cString[u], cString[v]= cString[v], cString[u]
        u,v = u+1, v-1

# tests
import unittest
class TestReverseSentence(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(reverseSentence(['h','e','l','l','o',' ', 'w','o','r','l','d']),
                         ['w','o','r','l','d',' ','h','e','l','l','o'])
        self.assertEqual(reverseSentence(['h', 'e', 'l', 'l', 'o']),
                         ['h', 'e', 'l', 'l', 'o'])
        self.assertEqual(reverseSentence(['h']),['h'])
        self.assertEqual(reverseSentence([]), [])
unittest.main()
