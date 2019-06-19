'''
Given k sorted arrays of possibly different sizes, merge them and print the sorted output.

Approach:
- first merge arrays into groups of 2
- after first merging, we have k/2 arrays
- we again merge arrays in groups, now we have k/4 arrays
- we keep doing it unit we have one array left

The time complexity of this solution would O(nk Log k) where n is the length of sorted lists.
'''

def merge_sorted_lists(sorted_lists):
    if not sorted_lists:
        return sorted_lists
    if len(sorted_lists) == 1:
        return sorted_lists[0]
    result = merge_first_two(sorted_lists)
    return merge_sorted_lists(result)

def merge_first_two(sorted_lists):
    updated = []
    for i in range(0, len(sorted_lists), 2):
        #odd length
        if i == len(sorted_lists) - 1:
            result = sorted_lists[i]
        #even lengths
        else:
            result = merge(sorted_lists[i], sorted_lists[i+1])
        updated.append(result)
    return updated

def merge(list_one, list_two):
    result = []
    u = v = 0
    while u < len(list_one) and v < len(list_two):
        if list_one[u] <= list_two[v]:
            result.append(list_one[u])
            u += 1
        else:
            result.append(list_two[v])
            v += 1

    for i in range(v, len(list_two)):
        result.append(list_two[i])

    for i in range(u, len(list_one)):
        result.append(list_one[i])

    return result

import unittest
class TestMergeKSortedLists(unittest.TestCase):

    def test_addition(self):
        self.assertEqual( merge_sorted_lists([[1,3,5,7],[2,4,6,8],[10,12,14,16],[9,11,13,15]]),
                          [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) #general case
        self.assertEqual( merge_sorted_lists([[3,5,7],[6,8],[10,12,14,16],[9,11,13]]),
                          [3,5,6,7,8,9,10,11,12,13,14,16]) #even len with diff sizes
        self.assertEqual( merge_sorted_lists([[3,5,7],[6,8],[10,12,14,16],[9,11,13], [21,22]]),
                          [3,5,6,7,8,9,10,11,12,13,14,16,21,22]) #odd case
        self.assertEqual( merge_sorted_lists([[],[10,20], [30,40], []]),
                          [10,20,30,40]) #case involving empty lists
        self.assertEqual(merge_sorted_lists([]),[]) #singleton
        self.assertEqual(merge_sorted_lists(None), None) #edge case -- None
unittest.main()