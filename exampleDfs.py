from src.datadebug import logger, class_decorator, List

class Number:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.value)
    
    def __eq__(self, other) -> bool:
        return self.value == other.value
    
    def __lt__(self, other) -> bool:
        return self.value < other.value
    
    def add_child(self, direction, node):

        if direction == 'L':
            self.left = node
        elif direction == 'R':
            self.right = node
        
        logger.add_edge(self, node, display=True)


if __name__ == "__main__":

    G1 = {
        '10': [],
        '20': [['L', '10'], ['R', '30']],
        '30': [],
        '40': [['L', '20'], ['R', '50']],
        '50': [['R', '60']],
    }

    graph1_nodes = list()

    for key, value in G1.items():

        key = int(key)
        temp_node = Number(key)

        if temp_node not in graph1_nodes:
            graph1_nodes.append(temp_node)

        node = graph1_nodes[graph1_nodes.index(temp_node)]

        for direction, value in value:

            temp_target_node = Number(int(value))

            if temp_target_node not in graph1_nodes:
                graph1_nodes.append(temp_target_node)

            neighbor = graph1_nodes[graph1_nodes.index(temp_target_node)]

            node.add_child(direction, neighbor)

    # Example of how their interaction sometimes leads to poor visuals
    # random_list = List(graph1_nodes[3:-1] + graph1_nodes[:3] + graph1_nodes[-1:], display_edges=True, display_index=False, label="RandomList")

    root = graph1_nodes[3]

    dfs_stack = List([root],
                     display_edges=False,
                     display_index=False,
                     label="DFS-Stack")

    while dfs_stack:

        current :Number = dfs_stack.pop()

        if current.right:
            dfs_stack.append(current.right)

        if current.left:
            dfs_stack.append(current.left)

        logger.add_pointer(current, "current", display_once=True)

