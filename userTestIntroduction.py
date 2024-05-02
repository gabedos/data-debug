from src.datadebug import logger, List

# create node
logger.create_node(5)
logger.create_node(6)

# create edge
logger.add_edge(5, 6)

# create label
logger.add_pointer(5, "top", display_once=False)

# create list
l = List(["data", "vis"], display_edges=True, display_index=True, label="List")

# visualize (useful for updating list visuals)
logger.visualize()

l[1] = 10

logger.visualize()