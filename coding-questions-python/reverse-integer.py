'''
Given a 32-bit signed integer, reverse digits of an integer.
Note:
    - assume we are dealing with an environment which could only store integers within the 32-bit signed integer range
    - range: [−231,  231 − 1]
    - for the purpose of this problem, assume that your function returns 0 when the reversed integer overflows

Leetcode: https://leetcode.com/problems/reverse-integer/

Approach:
    - assume the number is represented as x
    - we can grab at the last digit by doing x%10
    - we can "pop" x's last digit by doing x/10

    - "appending" a digit to the resultant number is just:
        new_int *= 10
        new_int =+ popped_digit

    - while appending each digit, check if the new_int has overflown
    - at the end, multiple new_num with -1 if new_num should be negative
    - also check for overflow

Time complexity:
    - as there are log 10 (x) digits in an integer
    - time complexity is log 10 (x)

Space compelxity:
    - O(1) or constant
'''

def reverse_integer(x):
    # this is the constraint defined in the question, to check for integer overflow
    int_max = (2 ** 31)

    # is the param negative?
    neg = x < 0

    # if it's neg, make it positive to make it easy to deal with
    if neg: x = x * -1

    # this will be the new reversed integer
    rev = 0

    # loop until there are no more digits left
    while (x != 0):
        # grab the last digit and store it into pop, and then get rid of it from x
        pop = x % 10
        x /= 10

        # "append" the popped digit to the new reversed_integer
        rev = rev * 10 + pop

        # check for integer overflow
        if rev > (int_max - 1): return 0

    # if the reversed integer is supposed to be negative, make it negative
    if neg: rev *= -1

    # check for integer overflow
    if rev < (-1 * int_max): return 0

    # otherwise, return the reversed integer
    return rev

# all leetcode tests pass