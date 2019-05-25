'''
Given two strings, find the missing character in the second string that is present in the first string.

Naive approach:
- iterate over the first string, and try to find that char in the second
- if that char is found, continue
- if not, return that char

This is an inefficient solution, runtime complexity is O(N*M)
    where N = len of string onen and M = len of string two

Updated algo:
    - use a hash set to store all chars in string one
    - iterate over string two -- for each char:
        . if it's there in the set, remove it and continue
        . if not, return that char
    - this reduces the runtime to O(N)
Only problem -- this only works for unique characters

Approach 03:
    - use a hashmap instead,
    - if the char is found, decrease it's count
    - when count is 0, remove that char


'''

def findMissingUnique(strOne, strTwo):
    strOneSet = set(strOne)

    for char in strTwo:
        if strOneSet.__contains__(char):
            strOneSet.remove(char)
            continue
        return char

def findMissing(strOne, strTwo):
    mapStrOne = {}
    for char in strOne:
        if char in mapStrOne:
            mapStrOne[char] = mapStrOne[char] + 1
            continue
        else:
            mapStrOne[char] = 1

    for char in strTwo:
        mapStrOne[char] = mapStrOne[char] - 1
        if mapStrOne[char] == 0:
            mapStrOne.pop(char)

    for key in mapStrOne.keys():
        return key

#tests
import unittest


class TestFindMissingStrings(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(findMissingUnique("what up", "whats up"), "s")
        self.assertEqual(findMissingUnique("azim", "b azim"), "b")
        self.assertEqual(findMissingUnique("  ", "k"), "k")
        self.assertEqual(findMissingUnique("  ", "k"), "k")
        self.assertEqual(findMissing("?hello?", "?olleh"), "?")
        self.assertEqual(findMissing("racecar is sfast", "is racecar fast"), "s")
unittest.main()