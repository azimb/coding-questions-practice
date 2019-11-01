'''
Meeting Rooms II (Premium)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1

Approach:
  - we'll use a priority queue / min heap to keep a track of the meeting ending times
  - for each new meeting:
    * grab the root from min heap, which will indicate the end of the meeting that will end the earliest
    
    * if the cur_meeting's start time is bigger (or equal), we're goood. No conflict and we don't need an additional room 
    for this meeting (so in this case we will just update root's end time to this new end time and put it back in the min heap).
    * else: we need a new room for this conflicting meeting, so we will add it to the min heap
    
  - in the end, the size of the priority queue will tell us how many meeting rooms are required
  
Time and space complexity analysis:
  - O(nlogn) time and O(n) space
'''
import heapq
def minMeetingRooms(intervals):
  # edge case -- no meeting to schedule
  if not intervals: return 0

  # sort the meetings in the increasing order of their start time
  intervals.sort(key = lambda x:x[0])

  # make a min heap, add the first meeting's end time
  minheap = [intervals[0][1]]
  heapq.heapify(minheap)

  # for all the remaining meetings
  for i in range(1, len(intervals)):
    cur_meeting = intervals[i]
    # if this meeting can be scheduled after the earliest meeting ends, we do not need an additional room
    if minheap[0] <= cur_meeting[0]: heapq.heappop(minheap)  
    # add to heap a) the updated end time, or b) the meeting with a new room
    heapq.heappush(minheap, cur_meeting[1])

  # the size of the heap will tell us the min # of rooms required for all the meetings
  return len(minheap)
  
  
# all leetcode tests pass as of 31st Oct 2019
