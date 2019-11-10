'''
LC:

Approach:
  - Our goal is trying to use two colors to color the graph and see if there are any adjacent nodes having the same color.
  - `color` map will track the color of each node. Here are three states for colors[] array:
    * -1: Haven't been colored yet.
    * 0: Blue.
    * 1: Red.
 - for each node:
  * if it hasn't been colored, use a color to color it. Then use the other color to color all its neighbors
  * if it has been colored, check if the current color is the same as the color that is going to be used to color it
  
Time complexity:
  - standard BFS on an adjacency list
  - so the time complexity will be O(|V| + |E|)
  * for detailed explanation, refer to: https://github.com/baghadiya/coding-questions-practice/blob/master/time-complexity-graph-traversal.md
  
Space complexity:
  - at worst, we might need to store all the vertices on the queue
  - so the space complexity is O(|V|)
'''

def isBipartite(self, graph):
  """
  :type graph: List[List[int]]
  :rtype: bool
  """
  if not graph: return False

  # color map will track the color of each node
  color = {}
  for i in range(len(graph)): color[i] = -1

  # for each node, if it's uncolored, perform bfs
  for i in range(len(graph)):
    # node is colored, continue
    if color[i] != -1: continue
    # otherwise, perform bfs to color it
    if not self.bfs(i, graph, color): return False

  return True

def bfs(self, i, graph, color):
  # queue is used for BFS
  queue = deque([i])
  # color the node
  color[i] = 0

  while queue:
    node = queue.popleft()
    cur_color = color[node]

    for neighbor in graph[node]:
      # if neighbor is colored the same, graph is not bipartite
      if color[neighbor] == cur_color: return False

      # if neighbor is not colored
      if color[neighbor] == -1 and color[neighbor] != cur_color:
        # color it with the opposite color
        color[neighbor] = 1 - cur_color
        # enqueue it, so it can be processed later
        queue.append(neighbor)

  # didn't discover bipartite property, so return True 
  return True
  
# all leetcode tests pass as of 10th Nov 2019
