'''
LC: https://leetcode.com/problems/clone-graph/

Time complexity: O(|V| + |E|)
Space complexity: O(|V|)
'''

from collections import deque
def clone_graph(node):
    '''
            Usual breadth first search using a queue.
            However, each time we pop a node, we want to make sure it's clone exists in the map.

            Now, for each of node's neighbors, we want to have _their_ (neighbors') clones added to the
            list of neighbors of the (current) node's clone.

            So for each neighbor, we ensure that there is a mapping to it's clone.
            This mapping can then be used to add neighbor_clone to current clone's neighbour list.

            As usual, to avoid computing the same node more than once, we will maintain a "seen" hashset.
            '''

    # edge case -- null node
    if not node: return None

    # usual breadth first search using a queue
    # and a hashset seen to keep a track of already visited nodes
    queue = deque([node])
    seen = set([])

    # hashmap to keep to create a mapping for each node with it's clone
    clone_mapping = {}

    while queue:
        # FIFO queue, so get the first node
        cur_node = queue.popleft()

        # have we already seen this node? If yes, skip
        if cur_node in seen:
            continue
        else:
            seen.add(cur_node)

        # if there is no node-to-clone mapping for this node, create one
        if cur_node not in clone_mapping:
            clone = Node(cur_node.val, [])
            clone_mapping[cur_node] = clone

        # now explore all of cur_node's neighbors
        # for each neighbor, create a neighbor_clone if needed, and add it as a neighbors to
        # cur node's clone neighbor list
        neighbors = cur_node.neighbors
        for n_node in neighbors:
            # add it to the queue to explore it later
            queue.append(n_node)

            # is there a clone mapping available for this neighbour
            # if yes, grab it. Otherwise, create one
            if n_node in clone_mapping:
                n_node_clone = clone_mapping[n_node]
            else:
                n_node_clone = Node(n_node.val, [])
                clone_mapping[n_node] = n_node_clone

            # take the cur_node's clone, and add neighbor's clone to _it's_ (cur node's clone's) neighbours list
            clone_mapping[cur_node].neighbors.append(n_node_clone)

    # input node's clone is the new deep copied graph
    return clone_mapping[node]

# all leetcode tests pass
