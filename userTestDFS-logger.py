from src.datadebug import logger, List
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

        logger.add_edge(u, v, display=False)
        # NOTE: Customization to make the single edge appear bidirectional
        logger.customize_edge(u, v, display=True, color="teal", dir="both")

    def DFSUtil(self, v: int, visited: set) -> list[int]:

        logger.add_pointer(v, 'current')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

        # Mark the current node as visited and print it
        visited.add(v)      #BUG: should be at start of call
        print(v, end=' ')

    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)

# Create a graph
g = Graph()



logger.update_controls(pause_time=10.0)

# List([1, 3, 5], display_index=True, label="l[1,3,5]")
# List([0, 2, 4, 6], display_index=True, label="l[0,2,4,6]")

# List([1, 3, 5], display_index=True, label="L[1,3,5]")
List([1, 2, 3, 4, 5], display_index=True, label="L[1,2,3,4,5]")

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
g.DFS(6)



