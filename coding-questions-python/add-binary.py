'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Leetcode: https://leetcode.com/problems/add-binary/
Approach 1:
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

Approach 2:
    - add binary strings directly
'''

def add_binary(num_one, num_two):
    #approach 1
    #result_dec = bin_to_dec(num_one) + bin_to_dec(num_two)
    #return bin(result_dec)[2:]


    result_array_reversed = []
    num_one_index = len(num_one) - 1
    num_two_index = len(num_two) - 1
    carry = 0
    while num_one_index >=0 and num_two_index >= 0:
        carry += int(num_one[num_one_index]) + int(num_two[num_two_index])
        if carry == 2:
            result_array_reversed.append("0")
        elif carry == 3:
            result_array_reversed.append("1")
        else:
            result_array_reversed.append(str(carry))

        if carry is 0 or carry is 1:
            carry = 0
        else:
            carry = 1

        num_one_index -= 1
        num_two_index -= 1

    if num_one_index >= 0 or num_two_index >= 0:
        add_remaining(num_one, num_one_index, carry, result_array_reversed) if num_two_index < 0 else add_remaining(num_two, num_two_index, carry, result_array_reversed)
        carry = 0

    if carry is 1:
        result_array_reversed.append(str(carry))

    my_reverse(result_array_reversed)
    return "".join(result_array_reversed)

def add_remaining(num, index, carry, result):
    for i in range(index, -1, -1):
        carry += int(num[index])

        if carry == 0 or carry == 1:
            result.append(str(carry))
            carry = 0

        else: #carry is 2
            result.append("0")
            carry = 1

    if carry is 1:
        result.append(str(carry))

def my_reverse(input_python_list):
    start = 0
    end = len(input_python_list) - 1
    while start < end:
        input_python_list[start], input_python_list[end] = input_python_list[end], input_python_list[start]
        start, end = start + 1, end - 1

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
        self.assertEqual(add_binary("111","101"), "1100")
        self.assertEqual(add_binary("1010", "111"), "10001")
        self.assertEqual(add_binary("1", "0"), "1")
        self.assertEqual(add_binary("1", "1"), "10")
        self.assertEqual(add_binary("0", "1"), "1")
        self.assertEqual(add_binary("0", "0"), "0")

unittest.main()

#all leetcode tests pass
#Runtime: 16 ms, faster than 96.36% of Python online submissions for Add Binary. 