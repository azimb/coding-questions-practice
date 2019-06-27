'''
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Approach:
    - start with possible answer = 0
    - if possible answer sqauare is num, return possible answer
    - else increment possible answer with 1, and repeat
    - in the case where possible answer square is greater than num, return possible answer - 1

#TODO: verify
Time Complexity:
    - iterative: O(root n)
    - recursive: O(root n)

#TODO: verify
Space Complexity:
    - iterative: O(1)
    - recursive: O(root n)
'''


#recursive
def my_sqrt_recursive(num):
    return my_sqrt_recursive_helper(num, 0)

def my_sqrt_recursive_helper(num, possible):
    if possible**2 == num:
        return possible
    elif possible**2 > num:
        return  possible - 1
    else:
        return my_sqrt_recursive_helper(num, possible + 1)

#iterative
def my_sqrt(num):
    possible = 0
    while True:
        if possible ** 2 == num:
            return possible
        elif possible ** 2 > num:
            return possible - 1
        else:
            possible += 1


# tests
import unittest
class TestSqrt(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(my_sqrt(49), 7)
        self.assertEqual(my_sqrt_recursive(49), 7)

        self.assertEqual(my_sqrt(143), 11)
        self.assertEqual(my_sqrt_recursive(143), 11)

        self.assertEqual(my_sqrt(90), 9)
        self.assertEqual(my_sqrt_recursive(90), 9)

        self.assertEqual(my_sqrt(1), 1)
        self.assertEqual(my_sqrt_recursive(1), 1)

        self.assertEqual(my_sqrt(0), 0)
        self.assertEqual(my_sqrt_recursive(0), 0)

unittest.main()

#FIXME: both approahces result in "time exceeded" error on leetcode