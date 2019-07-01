'''
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Approach:
    - start with possible answer = 0
    - if possible answer sqauare is num, return possible answer
    - else increment possible answer with 1, and repeat
    - in the case where possible answer square is greater than num, return possible answer - 1

Time Complexity:
    - iterative: O(root n)
    - recursive: O(root n)

Space Complexity:
    - iterative: O(1)
    - recursive: O(root n)

Optimized approach (binary search):
    - limit the number of searched numbers to O(log N)
    - start is 0 and end is num/2
    - if mid^2 is greater than num, search the left half
    - else, search the right half

Complexities:
    - time: O(log N)
    - space: O(1)
'''

# recursive
def my_sqrt_recursive(num):
    return my_sqrt_recursive_helper(num, 0)

def my_sqrt_recursive_helper(num, possible):
    if possible**2 == num:
        return possible
    elif possible**2 > num:
        return  possible - 1
    else:
        return my_sqrt_recursive_helper(num, possible + 1)

# iterative
def my_sqrt(num):
    possible = 0
    while True:
        if possible ** 2 == num:
            return possible
        elif possible ** 2 > num:
            return possible - 1
        else:
            possible += 1


# optimized
# FINAL APPROACH FOR THIS PROBLEM
def floor_sqrt(num):
    if num == 0 or num == 1: return num

    start = 0
    end = num/2

    while start <= end:
        mid = (start+end)/2

        if mid*mid == num:
            return mid

        elif mid*mid < num:
            start = mid + 1
            ans = mid

        else: # mid^2 is greater then num
            end = mid - 1

    return ans


# tests
import unittest
class TestSqrt(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(my_sqrt(49), 7)
        self.assertEqual(my_sqrt_recursive(49), 7)
        self.assertEqual(floor_sqrt(49), 7)

        self.assertEqual(my_sqrt(143), 11)
        self.assertEqual(my_sqrt_recursive(143), 11)
        self.assertEqual(floor_sqrt(143), 11)

        self.assertEqual(my_sqrt(90), 9)
        self.assertEqual(my_sqrt_recursive(90), 9)
        self.assertEqual(floor_sqrt(90), 9)

        self.assertEqual(my_sqrt(1), 1)
        self.assertEqual(my_sqrt_recursive(1), 1)
        self.assertEqual(floor_sqrt(1), 1)

        self.assertEqual(my_sqrt(0), 0)
        self.assertEqual(my_sqrt_recursive(0), 0)
        self.assertEqual(floor_sqrt(0), 0)

unittest.main()

# optimized approach leetcode testing
# all leetcode tests pass
# Runtime: 8 ms, faster than 99.92% of Python online submissions for Sqrt(x).