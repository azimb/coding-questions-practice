'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R

Leetcode: https://leetcode.com/problems/zigzag-conversion/

Approach:
    - we can think of this problem as an up and down pattern
    - we have num_rows rows and at each iteration, we will add the current character to the correct (or current) row
    - we will then either go up or down in order to update the row
    - we need to go down num_rows times, and then up num_rows times, and then go down num_rows times and so on
    - we do this until we visit each char in the input string
    - in the end, we just concatenate each row to get the zigzag string

Runtime complexity:
    - we will visit each character exactly once -- O(N) where N is the length of the input string
    - for each of the num_rows rows, we will convert it into a string -- O(num_rows * M) where M is the length of each row
    (or O(N) where N is the length of the string -- this is because the total number of characters in num_rows is N)
    - we will concat each row -- so that is an additional O(N) time

    - so, the overall runtime complexity is linear -- O(N)

Space complexity:
    - no additional space is being used
    - so constant or O(1) space complexity
'''

def zig_zag_convert(input_str, num_rows):
    # edge case -- numRows is 1
    if num_rows == 1: return input_str

    # array of numRows strings
    # each cstring represents a row of the resultant zigzag version of the input string
    zigzag_strings = [[] for x in range(num_rows)]
    down = True
    row = 0

    for char in input_str:
        # append the char to the current cstring
        zigzag_strings[row].append(char)

        # if we reached the first row, we will change the direction to go down
        # or if we reached the last row, we will change the direction to go up
        if row == num_rows - 1: down = False

        # if we reached the first row, we will change the direction to go down
        if row == 0: down = True

        '''
        if row == numRows - 1 or row == 0:
            down = not down
        '''

        # if the direction is down, go the next row
        if down == True:
            row += 1

        # if the direction is up, go the previous row
        else:
            row -= 1

        '''
        row += 1 if (not down) else -1
        '''

    # now that we have each row of the resultant zigzag string stored as a ctsring
    # we need to bring them all together
    result = ""

    # for each cstring/row, convert to a string and append it to the end of result
    for cstring in zigzag_strings:
        result = result + ("".join(cstring))

    return result

# all leetcode tests pass