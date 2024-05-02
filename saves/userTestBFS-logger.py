from src.datadebug import logger, List
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

        # LOGGER:
        logger.add_edge(u, v)

    def BreadthFirstSearch(self, root: int):
        """
        Breadth First Search (BFS) is an algorithm for traversing graph data structures.
        It starts at the tree root and explores all the neighbor nodes first,
        before moving to the next level neighbors.
        """

        # Create a set to store visited vertices
        visited = set()
        visit_order = []

        # LOGGER QUEUE:
        bfs_stack = List([root],
                display_edges=False,
                display_index=False,
                label="BFS-Queue")
        
        while bfs_stack:

            current :int = bfs_stack.pop()  #BUG
            visit_order.append(current)

            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    bfs_stack.append(neighbour)

            logger.add_pointer(current, "current", display_once=True)

        return visit_order


# Create a graph
g = Graph()

g.add_edge(6, 2)
g.add_edge(2, 1)
g.add_edge(2, 4)
g.add_edge(4, 3)
g.add_edge(4, 5)
g.add_edge(6, 10)
g.add_edge(10, 8)
g.add_edge(8, 7)
g.add_edge(8, 9)
g.add_edge(10, 11)

print("Following is DFS from (starting from vertex 6)")

result = g.BreadthFirstSearch(6)

bfs_solution = [6, 2, 10, 1, 4, 8, 11, 3, 5, 7, 9]

print("Given Result:   ", result)
print("Expected Result:", bfs_solution)
print("Match:", result == bfs_solution)
