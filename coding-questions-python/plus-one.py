'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array
contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Leetcode: https://leetcode.com/problems/plus-one/

Suggested approach:
    - iterate backwards
    - if it's not 9, just increament it by 1 and return the orig list
    - if it's 9, make it 0, and keep going
    - if end of list reached, make a new list, store 1 at index 0, copy all the elements from the orig list,
        and return this new list

Runtime complexity:
    - O(2N) if all 9s, O(N) otherwise

Space complexity:
    - O(N) if all 9s, O(1) otherwise
'''

def plus_one(input_arr):
    for i in range(len(input_arr)-1, -1, -1):
        if input_arr[i] != 9:
            input_arr[i] = input_arr[i] + 1
            return  input_arr
        else:
            input_arr[i] = 0
    newArr = [1]
    for num in input_arr:
        newArr.append(num)
    return newArr if input_arr != [] else []


# tests
import unittest
class TestPlusOne(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(plus_one([2,3,4]), [2,3,5])
        self.assertEqual(plus_one([3,6,9]), [3,7,0])
        self.assertEqual(plus_one([3,9,9]), [4,0,0])
        self.assertEqual(plus_one([9,9,9]), [1,0,0,0])
        self.assertEqual(plus_one([4]), [5])
        self.assertEqual(plus_one([9]), [1,0])
        self.assertEqual(plus_one([]), [])

unittest.main()

# all leetcode tests pass