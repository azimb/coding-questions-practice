'''
The description is lengthy, read up on LC.
Leetcode: https://leetcode.com/problems/string-to-integer-atoi/

Approach:
    - discard all leading whitespaces
    - sign of the number
    - overflow
    - invalid input

Time complexity:
    - iterating over the input string once
    - so time complexity is O(N) or linear

Space complexity:
    - log 10 x
    (where x is the result integer)
    TODO: double check space complexity
'''


def string_to_integer(str):
    max_int, min_int = (2 ** 31) - 1, -(2 ** 31)  # will be useful to check overflow
    integer = 0  # integer version of the string, this will be returned
    sign = 1  # will remember if the integer should be negative or positive

    # discard all the leading whitespaces
    p = 0
    while p < len(str) and str[p] == " ": p += 1

    # check for an optional +/- sign
    if p < len(str) and (str[p] == "+" or str[p] == "-"):
        if str[p] == "-": sign = -1
        p += 1

    # keep looping until you encounter digits
    while p < len(str) and "0" <= str[p] <= "9":
        # get the digit and append to the end
        integer *= 10
        integer += int(str[p])
        p += 1

    # make the integer negative if it needs to be, also check for overflow
    integer *= sign
    if integer > max_int or integer < min_int:
        return max_int if sign == 1 else min_int
    return integer

# all leetcode tests pass