'''
Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Ex1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Ex2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Leetcode: https://leetcode.com/problems/merge-intervals/

Approach:
- note that the intervals array is not sorted, that is, you could see something like [[1,4][0,1]]
- so, we will use sort the intervals by the first value `interval[0]`
- this will be done using lambda expressions

- after soring, each set of intervals that can be merged will apper as a contiguous "run" in the sorted list

- for each interval:
    * if it starts after the previous (merged) interval ends, they don't overlap in this case, the interval is appended
    * otherwise, when they overlap, we merge them by updating the end (interval[1]) of the previously merged
        interval if it's less than the end of the current interval

* Python uses Timsort under the hood.

Time complexity:
    - sorting will take O(nlogn) time in worst case
    (and timsort's best case runtime is O(N))
    - one pass through the interval array will take O(n) time
    - so, the time complexity is O(nlogn)

Space complexity:
   - timsort's space complexity is O(N)
   - so, the space complexity is O(N)
'''

def merge_intervals(intervals):
    # uses timsort (similar to merge sort) O(nlogn) time (worst case) and O(n) space
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []

    for cur_interval in intervals:
        # if the current intervals starts after the previously merged interal ends
        if not merged_intervals or merged_intervals[-1][1] < cur_interval[0]:
            merged_intervals.append(cur_interval)

        # there is overlapping -- updating the end of the merged interval is required
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], cur_interval[1])

    return merged_intervals

# all leetcode tests pass
