'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
    this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Leetcode: https://leetcode.com/problems/zigzag-conversion/

Approach:
    - this approach is known as sort by row
    - we iterate over the string, and determine which row in the zigzag string each character belongs to
    - the appropriate row is determined using two variables, current_row and current_direction
    - the current direction changes when we have moved up to the first row, or moved down to the last row
    - current_row changes based on the direction

Time complexity:
    - as are iterating over the string once, we are visiting each character at most once
    - so the time complexity is O(n) or linear
    (where n is the length of the input_str)

Space complexity:
    - we are making a new string of the same size
    - so the space complexity if O(n) or linear
'''

def zigzag_converstion(input_str, num_rows):
    # edge case, where the num_rows in the zigzag string is 1
    if num_rows == 1: return input_str

    # variables to track the current row and the current direction
    down, current_row = False, 0

    # result array, consisting of num_rows rows
    rows = [[""] for y in range(num_rows)]

    # for each char, determine the appropriate row
    for char in input_str:
        rows[current_row].append(char)
        if current_row == 0 or current_row == num_rows - 1: down = not down
        current_row = (current_row + 1) if down else (current_row - 1)

    # all the rows are stored as arrays, we need to make one signle string for the result
    result_array = []
    for row in rows:
        result_array += row

    return "".join(result_array)

# all leetcode tests pass