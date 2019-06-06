'''
Question:-
    - you are reading numbers of an array, one after the other.
    - need a method called getMedian that gets the 'current median'.
    (current median is the median of the numbers thus fars)
    - after each number is read, append the current median to the resultant list

Recall:
    - median is in the middle when the list is in sorted order
    - if there are twi midpoints, then median is the average of those two values

Idea:
    - use a max heap for the lower part of the numbers
    - and a min heap for the upper part of the numbers
    - max difference in size allowed = 1
    - diagram available: https://drive.google.com/file/d/1M3TlpQvmJIfh1P_ohJYzyRQY7lBWlnY3/view?usp=sharing

Approach:
    - if different sizes -- max of lowers or min of highers
    - if same size -- average lowers.max and highers.min

Complexities:
    - runtime complexity: O(N log N) as each of N insertions takes log N time
    - space complexity is O(N) as we are storing at most O(N) storage
'''

import heapq

def get_medians(arr):
    lowers = []
    highers = []
    medians = []

    for num in arr:
        add_number(num, lowers, highers)
        rebalance(lowers, highers)
        medians.append(get_median(lowers, highers))

    return medians

def add_number(number, lowers, highers):
    if len(lowers) == 0 or number < lowers[0]:
        heapq.heappush(lowers, number)
    else:
        heapq.heappush(highers, -1 * number)

def rebalance(lowers, highers):
    if len(highers) > len(lowers):
        bigger = highers
        smaller = lowers
    else:
        bigger = lowers
        smaller = highers

    if len(bigger) - len(smaller) >= 2:
        heapq.heappush(smaller, heapq.heappop(bigger))

def get_median(lowers, highers):
    if len(highers) > len(lowers):
        bigger = highers
        smaller = lowers
    else:
        bigger = lowers
        smaller = highers

    if len(bigger) == len(smaller):
        #note that `abs` is used as maxheap stores the negation of the numbers
        #also note that `float` is used python2 forces integer division
        #if using python3, just using (...)/2 should work as intended
        return (abs(bigger[0]) + abs(smaller[0]))/float(2)
    else:
        return abs(bigger[0])

# tests
import unittest
class TestGetMedian(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(get_medians([]), [])
        self.assertEqual(get_medians([6]), [6])
        self.assertEqual(get_medians([10, 15]), [10, 12.5])
        self.assertEqual(get_medians([8, 2, 4, 6]), [8, 5, 4, 5])

unittest.main()

#TODO: confirm complexities