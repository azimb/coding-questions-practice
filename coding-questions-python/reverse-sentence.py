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
    cString = myReverse(cString, 0, len(cString)-1)

    # let's now reverse the individual words
    start = 0
    end = 0
    while end < len(cString) - 1:
        while cString[end] != ' ':
            end += 1
            if end == len(cString) - 1:
                end += 1
                break

        cString = myReverse(cString, start, end-1)
        start = end + 1
        end += 1

    return cString

def myReverse(cString, u, v):
    while (u < v):
        temp = cString[u]
        cString[u] = cString[v]
        cString[v] = temp
        u += 1
        v -= 1
    return cString

#print(reverseSentence(['h','e','l','l','o',' ', 'w','o','r','l','d']))

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
