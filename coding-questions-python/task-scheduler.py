'''
LC: https://leetcode.com/problems/task-scheduler/

Approach:
  -  time taken for the tasks to be finished is only dependent on the number of instances of each task and not on the names of tasks
  - the tasks with the currently maximum number of outstanding (pending)instances will contribute to a large number of idle cycles 
    in the future, if not executed with appropriate interleavings with the other tasks
  - so, we need to re-execute such a task as soon as its cooling time is finished
  
Complexity analysis:
  - number of iterations will be equal to resultant time
  - so, O(intervals)

  - queue and programs_arr size will not exceed 26
  - so, O(1) space complexity
'''

def leastInterval(self, tasks, n):
  # for each task, we need how many times it occurs
  # so, we use the hashmap to count it's tasks frequency
  occurence = defaultdict(int)
  for task in tasks: occurence[task] += 1

  # the max_heap will tell the which order to execute the tasks in
  # trick is to execute the tasks in desc order of frequency, in order to avoid being idle as much as possible
  max_heap = []
  heapq.heapify(max_heap)
  for frequency in occurence.values(): heapq.heappush(max_heap, (-1* frequency)) # f*-1 because we need max_heap

  # while there are still tasks to performed
  intervals = 0
  while max_heap:
    # programs array will hold the tasks we will perform in this cycle
    programs = []
    # n+1 because we want to cover the entire cool down period, and avoid being idle if possible
    for i in range(n+1):
      # get the task with the max frequency to execute
      if max_heap: programs.append(heapq.heappop(max_heap))

    # now let's look at the tasks we performed in this cycle
    # and add them back if there are more instances of these tasks left
    for remaining in programs:
      '''
      technically intuition is that
      remaining -= 1 (just finished this task)
      if remaining > 1: ... (more instances of this task left)
      we flipped them because we are using max_heap
      '''
      remaining += 1
      if remaining < 0: heapq.heappush(max_heap, remaining)

    # so the trick here is that if heap is empty, this cycle was the last and # of intervals are the # of tasks we performed
    # these # of the tasks we performed are stored in the programs array
    # otherwise, if there are more tasks to be performed, we went through one full cycle of cool down period
    intervals += n+1 if max_heap else len(programs)

  # this is how many intervals the CPU performed (including idle intervals if relavant)
  return intervals
  
# all leetcode tests pass as of 3rd Nov 2019
