'''
LC: https://leetcode.com/problems/exclusive-time-of-functions/
LC discussion solution by Alex Wice: https://leetcode.com/problems/exclusive-time-of-functions/discuss/105100/Python-Straightforward-with-Explanation

Approach:
  - the idea is called "sweep line"
  - each time you process an event, time - prev_time is the amount of time that has elapsed between this event and the last event
  - basically, the stack is like "layers" of the horizontal lines in the diagram
  - for each one you use the stack to help you know what cpu function had active time during the interval in question
  
Time and space complexity:
  - O(L) time and space where L = len of logs arrays
'''

def exclusiveTime(n, logs):
  # ans[i] will store the exclusive time of function with id i
  ans = [0] * n

  # stack will keep a track of the order of function calls
  # and prev_time will track when the last event "ended"
  stack, prev_time = [], 0

  for log in logs:
    func, type, time = log.split(':')
    func, time = int(func), int(time)

    # starting a new function, so current function "ended"
    #(in the sense that the time span wouldn't be added to it's exclusive time)
    # it's time will incremented by (time right now - when did the function before it "end") 
    if type == "start":
      if stack: 
        ans[stack[-1]] += time - prev_time
      stack.append(func)
      # new function starts, so the time at which the cur_func ends is => time
      prev_time = time

    # cur function ends, so get the time elapsed by cur_func is
    # (the time right now + time when the prev function "ended") + 1
    # adding 1 because when cur function ends, it consumes that full time unit
    else: # type == "end"
      ans[stack.pop()] += time - prev_time + 1
      prev_time = time + 1

  return ans
  
# all leetcode tests pass as of 8th Nov 2019
