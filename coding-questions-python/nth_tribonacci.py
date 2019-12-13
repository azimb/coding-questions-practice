'''
nth tribonacci number is defined as:

    t(n) = t(n-1) + t(n-2) + t(n-3)

    where t(0) = 0, and t(1) and t(2) are 1

Write a function that takes a number n as a parameter, and returns the nth tribonacci number.

Follow up? Can you do this in linear time and constant space complexity?

'''

# First 10 tribonacci numbers
# [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, ...]

# O(N) time and O(N) space complexity
# recursive solution
def nth_tribonacci(n):
    cache = {}
    return nth_tribonacci_recursive(n, cache)

def nth_tribonacci_recursive(n, cache):
    if n == 0: return 0
    if n == 1 or n == 2: return 1

    if n in cache: return cache[n]

    sol = nth_tribonacci_recursive(n-1, cache) + nth_tribonacci_recursive(n-2, cache) + nth_tribonacci_recursive(n-3, cache)
    cache[n] = sol
    return sol

# O(N) time and O(1) space complexity
# iterative solution
def nth_tribonacci_iterative(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1

    most_recent = [0,1,1]

    for i in range(3, n+1):
        current_fibonacci_number = most_recent[0] + most_recent[1] + most_recent[2]
        most_recent[0], most_recent[1], most_recent[2] = most_recent[1], most_recent[2], current_fibonacci_number

    return most_recent[2]


# tests
import unittest
class TestCheckNumEquality(unittest.TestCase):

    def test_general_success_cases(self):
        self.assertEqual(nth_tribonacci(9), 81)
        self.assertEqual(nth_tribonacci(12), 504)

        self.assertEqual(nth_tribonacci_iterative(9),81)
        self.assertEqual(nth_tribonacci_iterative(12), 504)

    def test_base_cases(self):
        self.assertEqual(nth_tribonacci(0), 0)
        self.assertEqual(nth_tribonacci(1), 1)
        self.assertEqual(nth_tribonacci(2), 1)


        self.assertEqual(nth_tribonacci_iterative(0), 0)
        self.assertEqual(nth_tribonacci_iterative(1), 1)
        self.assertEqual(nth_tribonacci_iterative(2), 1)

unittest.main()
