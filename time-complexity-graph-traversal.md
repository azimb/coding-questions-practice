### Time complexity of a BFS and DFS of a graph

The Time complexity of both BFS and DFS will be O(V + E), where V is the number of vertices, and E is the number of Edges. 
This again depends on the data strucure that we user to represent the graph. If it is an adjacency matrix, it will be O(V^2). 
If we use an adjacency list, it will be O(V+E). Now , to explain how, lets us consider the difference between a sparsely connected 
graph and a densely connected graph.

Dense graph is a graph in which the number of edges is close to the maximal number of edges. Sparse graph is a graph in which the 
number of edges is close to the minimal number of edges. Sparse graph can be disconnected.

Now, what this means is that, if the graph has so many edges and is still a small graph with only few vertices(for example, a graph 
with 100 vertices but with 4950 edges since it is totally connected( n*(n-1)/2 ), then the number of iterations or recursive calls 
is dominated by the number of edges, because 4950 > 100. Now as n -> very large , this difference matters. This kind of graph is a 
dense graph. Time complexity will be O(E)

Consider an other example , where the number of vertices is very much larger than the number of edges. This kind of graph is a 
sparsely connected graph. And it may or may not be a disconnected graph. Now consider if the graph has 1000 vertices, but only 
100 edges. Here, some of the vertices are disconnected. So, the BFS in this case will be purely dominated by the number of Vertices, 
rather than by the number of Edges. So, the time complexity will be O(V).

So, what does it mean by O(V + E) ? It means , whichever term is bigger will dominate the time complexity. That is why the 
time complexity of BFS is O(V+E).

Quora: https://www.quora.com/What-is-the-time-complexity-of-Breadth-First-Search-Traversal-of-a-graph
