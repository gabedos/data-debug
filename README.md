# DataDebug API Documentation

`DataDebug` is a Python package designed for visual debugging of data structures. Leveraging `matplotlib` and `pygraphviz`, it provides an intuitive interface for visualizing and interacting with data structures as graphs. To use this library, import the _logger_ from src/datadebug and start debugging your data structures.

## GUI Controls

### `Left arrow: next`

Advances to previous snapshot of the underlying data structures. Pauses GUI updates for default of 3 seconds.

### `Right arrow: previous`

Advances to next pre-recorded snapshot of the underlying data structures. Pauses GUI updates for default of 3 seconds.

### `Up arrow: speed up`

Cancels the GUI pause, allowing for quick rendering of the next state.

## Logger Class Methods

### `create_node(node, display=True)`

Creates a new node in the graph.

- **Parameters:**
  - `node`: Identifier for the new node.
  - `display` (optional): Whether to display the graph after adding the node. Defaults to `True`.

### `delete_node(node, display=True)`

Deletes a node from the graph.

- **Parameters:**
  - `node`: Identifier for the node to delete.
  - `display` (optional): Whether to display the graph after deleting the node. Defaults to `True`.

### `add_edge(node_from, node_to, display=True)`

Adds an edge between two nodes in the graph.

- **Parameters:**
  - `node_from`: Identifier for the source node.
  - `node_to`: Identifier for the destination node.
  - `display` (optional): Whether to display the graph after adding the edge. Defaults to `True`.

### `delete_edge(node_from, node_to, display=True)`

Deletes an edge between two nodes in the graph.

- **Parameters:**
  - `node_from`: Identifier for the source node.
  - `node_to`: Identifier for the destination node.
  - `display` (optional): Whether to display the graph after deleting the edge. Defaults to `True`.

### `clear_edges(node, display=True)`

Clears all edges connected to a specific node.

- **Parameters:**
  - `node`: Identifier for the node whose edges will be cleared.
  - `display` (optional): Whether to display the graph after clearing the edges. Defaults to `True`.

### `customize_node(node, display_once=True, **kwargs)`

Customizes the appearance of a node.

- **Parameters:**
  - `node`: Identifier for the node to customize.
  - `display_once` (optional): Whether to apply customization for the current state only. Defaults to `True`.
  - `**kwargs`: Additional styling parameters (e.g., color, shape).

### `customize_edge(node_from, node_to, display=False, **kwargs)`

Customizes the appearance of an edge.

- **Parameters:**
  - `node_from`: Identifier for the source node.
  - `node_to`: Identifier for the destination node.
  - `display` (optional): Whether to display the graph after customizing the edge. Defaults to `False`.
  - `**kwargs`: Additional styling parameters (e.g., color, label).

### `add_pointer(node, pointer_name, display_once=True, clear_repeated=True)`

Adds a pointer label to a node.

- **Parameters:**
  - `node`: The node to add the pointer to.
  - `pointer_name`: The name of the pointer (e.g., head, tail).
  - `display_once` (optional): Whether to display the pointer for the current state only. Defaults to `True`.
  - `clear_repeated` (optional): Whether to clear repeated pointers before adding the new one. Defaults to `True`.

### `add_pointers(nodes, pointers, display_once=True, clear_repeated=True)`

Adds multiple pointer labels to nodes at the same time.

- **Parameters:**
  - `nodes`: The nodes to add pointers to.
  - `pointers`: The names of the respective pointers (e.g., head, tail).
  - `display_once` (optional): Whether to display the pointers for the current state only. Defaults to `True`.
  - `clear_repeated` (optional): Whether to clear repeated pointers before adding new ones. Defaults to `True`.

### `visualize()`

Renders and displays the current graph.

### `snapshot()`

Takes a snapshot of the current graph state. Saves in specified folder (default: ./log_snapshot)

## List

To directly visualize a list, the List class can be leveraged by users. It automatically connects to the underlying graph and captures all changes onto the graph. However, the user must manually direct the library to re-visualize the data structure when updates to the List want to be rendered & seen on the interface.

## List Class Methods

### `__init__(self, data, label = 'Head', display_edges = True, display_index = False)`

Creates a list using the data and records structure in graph.

- **Parameters:**
  - `data`: The data to initialize the list.
  - `label`: The name of the list pointer (e.g., head, tail).
  - `display_edges` (optional): Whether to display edges from the nodes in the list to pre-existing nodes in the graph. Defaults to `True`.
  - `display_index` (optional): Whether to display the index of the items in the list or their true values. Defaults to `False`.

This documentation aims to provide a clear overview of how to interact with the `DataDebug` package. For further details, including examples and advanced usage, please refer to the package's official documentation or source code.
