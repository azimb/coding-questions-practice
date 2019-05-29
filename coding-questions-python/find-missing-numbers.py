'''
Given two list of numbers, find the missing number in the second list that is present in the first list.

Jumping to approach 3 using maps. This O(N) runtime and O(N) space complexity can be used.

Here we are dealing with numbers, so we can omit additional storage


Update:
    - working in languages like Java and C++ may cause problems
    - if the numbers are "too large", it could result in an integer overflow
Solution: use bitwise xor

Bitwise xor: if both bits are same, it gives 0. Result is 1 otherwise.
'''

def findMissingNumbers(listOne, listTwo):
    sum = 0

    for num in listOne:
        sum += num

    for num in listTwo:
        sum -= num

    return sum

def findMissingNumbersUsingBitwise(listOne, listTwo):
    sum = 0

    for num in listOne:
        sum = sum ^ num

    for num in listTwo:
        sum = sum ^ num

    return sum

import unittest
#tests

class TestFindMissingNumbers(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(findMissingNumbers([7, 1, 2, 5, 6, 3, 4], [1, 2, 3, 4, 6, 7]), 5)
        self.assertEqual(findMissingNumbers([5, 9, 8, 33, 29, 76, 555, 55], [76, 8, 5, 33, 55, 9, 29]), 555)
        self.assertEqual(findMissingNumbers([1], []), 1)
        self.assertEqual(findMissingNumbers([5, 9, 8, 33, 29, 76, 555, 55], [76, 8, 5, 33, 55, 9, 29]), 555)
        self.assertEqual(findMissingNumbersUsingBitwise([1], []), 1)
        self.assertEqual(findMissingNumbersUsingBitwise([7, 1, 2, 5, 6, 3, 4], [1, 2, 3, 4, 6, 7]), 5)
unittest.main()