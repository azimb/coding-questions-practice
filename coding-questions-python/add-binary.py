
'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Leetcode: https://leetcode.com/problems/add-binary/
Approach:
    - convert each bin string to a decimal
    - add the decimals together
    - convert the sum into a bin string
Runtime complexity:
    - bin str to dec -- O(N)
    - (dec) sum to bin -- O(N)
    - total runtime -- O(N)
Space complexity:
    - constant, except the bin string that is being returned
#TODO: try implementing your own 'bin' function
'''

def add_binary(num_one, num_two):
    result_dec = bin_to_dec(num_one) + bin_to_dec(num_two)
    return bin(result_dec)[2:]

def bin_to_dec(bin_str):
    result = 0
    for i in range(len(bin_str) - 1, -1, -1):
        if bin_str[i] == '1':
            result += (2**(len(bin_str) - 1 - i))
    return result

# tests
import unittest
class TestAddBinary(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add_binary("1010", "111"), "10001")
        self.assertEqual(add_binary("1", "0"), "1")
        self.assertEqual(add_binary("1", "1"), "10")
        self.assertEqual(add_binary("0", "1"), "1")
        self.assertEqual(add_binary("0", "0"), "0")
unittest.main()

#all leetcode tests pass
#Runtime: 16 ms, faster than 96.36% of Python online submissions for Add Binary. 