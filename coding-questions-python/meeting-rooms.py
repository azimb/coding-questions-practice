'''
Meeting rooms (Premium)
LC: https://leetcode.com/problems/meeting-rooms/

Approach:
  - sort the input array, based on the meeting start time
  - then for each meeting starting from second meeting / index 1:
    * check if it it's start time is before the end time of the previous meeting
    (if the start time is smaller than the end time of previous meeting, we cannot attend this meeting as
      we will be attending the previous meeting, and it hasn't finished yet)
      
Time and space complexity: 
  - Python uses Timsort under the hood
  - time complexity: O(nlogn) worst case, and O(n) best case
  - space complexity is O(n)
'''

def canAttendMeetings(self, intervals):
  # sort by start time, using lambda function
  intervals.sort(key = lambda x:x[0])

  for i in range(1, len(intervals)):
    # is the meeting starting before the previous meeting ended?
    if intervals[i][0] < intervals[i-1][1]: return False
    
  # no conflicts occured, we're good
  return True
  
# all leetcode tests pass as of 31st October 2019
