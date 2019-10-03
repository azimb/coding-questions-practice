'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Leetcode: https://leetcode.com/problems/palindrome-number/

Approach:
    - note that a negative number can never be palindromic
    - if the current integer is equal to the reveresed version of the integer (digits are reversed), then it's
        palindromic
    (TODO: double check if integer overflow is possible. And if it is, how to handle it)

Time complexity:
    - as an integer contains log 10 x digits (where x is the integer)
    - the time complexity to reverse the integer is log 10 x
    - so, the time complexity of the function is O(log 10 x)

Space complexity:
    - storing the reversed integer
    - O(log 10 x) -- #FIXME: double check
'''


def palindromic_number(x):
    # negative numbers can't be palindromic
    if x < 0: return False

    # reverse the integer, and check for equality
    rev_x = integer_reverse(x)
    return x == rev_x


def integer_reverse(self, x):
    rev = 0
    # while there are digits left
    while x != 0:
        # grab the last digit, and remove it from x
        pop = x % 10
        x /= 10

        # append the popped digit
        rev *= 10
        rev += pop

    return rev

# all leetcode tests pass