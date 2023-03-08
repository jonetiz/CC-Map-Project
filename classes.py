class Node:
    def __init__(self, info: str):
        self.info = info
        self.connections: list[tuple] = []
    
    def __repr__(self):
        return f'{self.info}'

    def connect(self, other: 'Node', weight: int, omnidirectional = False):
        self.connections.append((other, weight))
        # if we want connection to go both ways, append self to other.connections
        # TODO: find a good way to manage different weights in both directions
        if omnidirectional:
            other.connections.append((self, weight))

    def sort_nodes(self):
        #print(self.connections)
        # sort nodes by weight, with lowest weight first
        self.connections.sort(key = lambda n: n[1])
        #print(self.connections)

    def find_path(self, target):
        """Finds a path to the `target` node."""
        self.sort_nodes()

        # list of known nodes, organized with [node, total_distance, visited, [<all nodes to get here>]]
        known_nodes = [[self, 0, True, [self]]]

        # set our current iterant
        current_node = known_nodes[0]

        def discover_nodes(for_node):
            """Discover the connected nodes and place in the known_nodes list"""
            # for all connections to the node
            for node in for_node[0].connections:
                # known node (blank)
                kn = [None, 1e7, False, []]

                # find out of we already have a connection to this node
                for known_node in known_nodes:
                    if node[0] is known_node[0]:
                        kn = known_node

                # if we have a connection to this node, make sure the new one is shorter than the old one
                if for_node[1] + node[1] < kn[1]:
                    # keep track of the shortest path taken to this node
                    path = for_node[3].copy()
                    # append this current node to the path
                    path.append(node[0])

                    # append this node to known_nodes, along with distance, False (as it's not been visited yet), and the path
                    known_nodes.append([node[0], for_node[1] + node[1], False, path])

        def visit_node(current_node):
            """Visit the next lowest distance node that has not been visited"""
            # list of available nodes
            visitation_candidates = []

            # for each node we have
            for node in known_nodes:
                # ensure the visitation candidates are unvisited and not the current node
                if not node[2] and node is not current_node:
                    visitation_candidates.append(node)

            # sort available nodes by distance
            visitation_candidates.sort(key = lambda n: n[1])

            # set return value to the lowest distance visitation candidate
            cn = visitation_candidates[0]
            # set column 3 to True (as we've now visited it)
            cn[2] = True
            return cn

        found = False
        # we continue while there's something untrue in column two
        while not found:
            # discover nodes with the current_node
            discover_nodes(current_node)
            current_node = visit_node(current_node)
            # if we are at the target, break the loop
            if current_node[0] is target:
                found = True

            # TODO: break loop if all are not true

        #print(known_nodes)
        target_node = [x for x in known_nodes if x[0] is target][0]
        return target_node[3]