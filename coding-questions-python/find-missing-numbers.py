'''
Given two list of numbers, find the missing number in the second list that is present in the first list.

Jumping to approach 3 using maps. This O(N) runtime and O(N) space complexity can be used.

Here we are dealing with numbers, so we can omit additional storage
'''

def findMissingNumbers(listOne, listTwo):
    sum = 0

    for num in listOne:
        sum += num

    for num in listTwo:
        sum -= num

    return sum

print(findMissingNumbers([7,1,2,5,6,3,4], [1,2,3,4,6,7]))
