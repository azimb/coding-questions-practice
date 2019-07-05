'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Ex:-
    * input: 5
    * output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
Leetcode problem: https://leetcode.com/problems/pascals-triangle/
'''


def generate(numRows):
    if numRows is 0: return []

    result = [[1]]
    return result if numRows is 1 else generate_helper(numRows, result)

def generate_helper(numRows, result):
    for i in range(2, numRows + 1):
        newLevel = [1]
        prevLevel = result[len(result) - 1]
        for j in range(len(prevLevel) - 1):
            newLevel.append(prevLevel[j] + prevLevel[j + 1])
        newLevel.append(1)
        result.append(newLevel)

    return result