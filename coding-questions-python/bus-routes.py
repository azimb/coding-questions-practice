'''
LC: https://leetcode.com/problems/bus-routes/
Approach: BFS
Time and space complexity: #TODO
'''

def numBusesToDestination(self, routes, S, T):
  # map each stop to the bus routes nums it's a part of
  map = {}
  for i in range(len(routes)):
    for j in range(len(routes[i])):
        if routes[i][j] not in map: map[routes[i][j]] = [i+1]
        else: map[ routes[i][j] ].append(i+1)

  # this will look something like this
  # {route1: [bus1, bus3], route2: [bus4, bus6], ...}

  queue = deque([(S,0)])
  visited = set([])

  # bfs
  while queue:
    node = queue.popleft()
    stop, num_of_busses = node[0], node[1]
    
    # reached the destination stop
    if stop == T: return num_of_busses

    # for each route that this stop can get to
    for route in map[stop]:
      # have we visited the route?
      if route not in visited:
        # explore all the stop of this bus route
        for stop_on_that_route in routes[route-1]: queue.append((stop_on_that_route, num_of_busses+1))
        # now we have explored this bus route
        visited.add(route)

  # not possible to reach from S to T
  return -1
  
# all leetcode tests pass as of 19th Oct 2019
