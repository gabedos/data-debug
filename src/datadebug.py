import abc
from collections import defaultdict
import time
import os
import uuid
import pygraphviz as pgv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backend_bases import KeyEvent

class DataDebug:
    """
    Log data and display it in a graph
    """

    def __init__(self) -> None:

        self.process = str(uuid.uuid4())[:4]

        # Graph
        self.graph = pgv.AGraph(directed=True,
                                rank='max',
                                ranksep='0.75',
                                )
        self.builtins: List[Builtin] = []

        # Image log
        self.images = []
        self.current_index = -1
        self.folder_name = "log_snapshot"
        os.makedirs(self.folder_name, exist_ok=True)

        # Args
        self.display = True
        self.pause_time = 3.0
        self.counter = 0

        # Display
        self.fig, self.ax = plt.subplots()
        self.ax.axis('off')  # Turn off axis labels

        self.should_pause = True

        # Allow change between images
        self.fig.canvas.mpl_connect('key_press_event', self.__on_key_press)

    """
    Image navigation start:
    """
    def __on_key_press(self, event: KeyEvent):
        if event.key == 'right':
            self.__next_image()
        elif event.key == 'left':
            self.__prev_image()
        elif event.key == 'up':
            self.__speed_up()
        elif event.key == 'r':
            print("R")
            self.snapshot()
    
    def __next_image(self):
        self.current_index = (self.current_index + 1) % len(self.images)
        self.__display_image(self.pause_time)

    def __prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.images)
        self.__display_image(self.pause_time)

    def __speed_up(self):
        self.current_index = len(self.images) - 1
        self.should_pause = False
    """
    Image navigation end:
    """

    def __display_image(self, pause_time=1.0):

        if len(self.images) == 0:
            print("No images to display")
            return

        self.ax.clear()
        self.ax.axis('off')
        self.ax.imshow(self.images[self.current_index])
        self.ax.set_title(f'Image {self.current_index + 1}/{len(self.images)}')
        self.fig.canvas.draw()

        self.fig.show()

        end_time = time.time() + pause_time
        pause_interval = 0.5
        self.should_pause = True

        # Allows for pausing to be cancelled
        while self.should_pause:

            plt.pause(pause_interval)

            if time.time() > end_time:
                break

    def update_controls(self, **kwargs):
        """
        Update the controls for the visualization:

            display = bool

            pause_time = float
        """

        if 'display' in kwargs:
            self.display = kwargs['display']

        if 'pause_time' in kwargs:
            self.pause_time = kwargs['pause_time']

    def create_node(self, node, display=True):
        """
        Create a node on the graph
        """

        # Create node on graph
        self.graph.add_node(node)

        if display:
            self.visualize()

    def delete_node(self, node, display=True):
        """
        Delete a node on the graph
        """

        # Remove node on graph
        self.graph.remove_node(node)

        if display:
            self.visualize()

    def add_edge(self, node_from, node_to, display=True):
        """
        Add an edge between two nodes
        """

        # Append the new edge
        self.graph.add_edge(node_from, node_to)

        if display:
            self.visualize()

    def delete_edge(self, node_from, node_to, display=True):
        """
        Delete an edge between two nodes
        """

        try:

            # Remove the edge
            self.graph.remove_edge(node_from, node_to)

            if display:
                self.visualize()

        # If the edge does not exist, ignore Exception
        except TypeError as e:
            pass

    def clear_edges(self, node, display=True):
        """
        Clear all edges from a node
        """

        # Clear all edges from node
        self.graph.remove_edges_from(node)

        if display:
            self.visualize()


    def customize_node(self, node, display=False, **kwargs):
        """
        Customize the node's attributes:
            color = {'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black', 'white'}

            fillcolor

            fontcolor

            label = str

            labelfontsize = float
        """

        node :pgv.Node = self.graph.get_node(node)
        node.attr.update(kwargs)

        if display:
            self.visualize()

    def customize_edge(self, node_from, node_to, display=False, **kwargs):
        """
        Customize the edge's attributes:
            color = {'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black', 'white'}

            fillcolor

            fontcolor

            label = str

            labelfontsize = float
        """

        edge :pgv.Edge = self.graph.get_edge(node_from, node_to)
        edge.attr.update(kwargs)

        if display:
            self.visualize()

    def add_pointer(self, node, pointer_name, display_once=True, clear_repeated=True):
        """
        Add a pointer label to the node
            node: the node to add the pointer to

            pointer_name: the name of the pointer (eg. head, tail, next, prev)
        """

        if clear_repeated:
            self.__clean_repeated_pointers([pointer_name])

        graph_node = self.graph.get_node(node)

        prev_label = graph_node.attr['xlabel']
        graph_node.attr['xlabel'] = pointer_name

        prev_style = graph_node.attr['style']
        graph_node.attr['style'] = 'filled'

        if display_once:
            self.visualize()
            graph_node = self.graph.get_node(node)
            graph_node.attr['xlabel'] = prev_label or ''
            graph_node.attr['style'] = prev_style or ''

    def add_pointers(self, nodes, pointers, display=True, save_pointers=True, clear_repeated=True):
        """
        Add a pointer label to the node at the same time
            nodes: the nodes to add the pointer to

            pointer_names: the name of the respective pointers (eg. head, tail, next, prev)

            display: whether to display the graph after adding the pointers

            save_pointers: whether to save the pointers after displaying the graph

            clear_repeated: whether to clear previously repeated pointers
        """

        if clear_repeated:
            self.__clean_repeated_pointers(pointers)

        record = {}

        for node, name in zip(nodes, pointers):
            graph_node = self.graph.get_node(node)
            prev_label = graph_node.attr['xlabel'] or ''
            graph_node.attr['xlabel'] = name
            prev_style = graph_node.attr['style'] or ''
            graph_node.attr['style'] = 'filled'

            record[node] = (prev_label, prev_style)

        if display:
            self.visualize()

        if not save_pointers:
            for node in nodes:
                graph_node = self.graph.get_node(node)
                graph_node.attr['xlabel'] = record[node][0]
                graph_node.attr['style'] = record[node][1]

    def __clean_repeated_pointers(self, pointers):

        pointers = set(pointers)
        for node in self.graph.nodes():
            if 'xlabel' in node.attr:
                if node.attr['xlabel'] in pointers:
                    node.attr['xlabel'] = ''


    def visualize(self):
        """
        Render the graph visualization on the GUI
        """

        filename = f"{self.folder_name}/array_graph_log.png"

        current_graph = self.graph.copy()

        curr_nodes = current_graph.nodes()
        current_graph.add_subgraph(curr_nodes, rank='max')

        for builtin in self.builtins:
            builtin.convert_and_add(current_graph)

        # Save the graph visualization as an image file
        current_graph.layout(prog='dot')
        current_graph.draw(filename)

        # Read the saved image
        img = mpimg.imread(filename)
        self.images.append(img)

        self.current_index += 1
        self.__display_image(self.pause_time)

    def snapshot(self):
        """
        Save the current graph as an image file
        """

        # current_graph = self.graph.copy()

        # curr_nodes = current_graph.nodes()
        # current_graph.add_subgraph(curr_nodes, rank='max')

        # for builtin in self.builtins:
        #     builtin.convert_and_add(current_graph)

        # current_graph.layout(prog='dot')
        # current_graph.draw(f"{self.folder_name}/{self.process}-img{self.counter}.png")

        # Saves the currently selected image in the GUI
        mpimg.imsave(
            f"{self.folder_name}/{self.process}-img{self.counter}.png",
            self.images[self.current_index]
        )

        self.counter += 1

logger = DataDebug()

# For each list visualize
# 1. Save the graph with regular edges
# 2. Convert all of the lists to graph
# 3. Restore graph to original state

class Builtin(abc.ABC):

    @abc.abstractmethod
    def convert_and_add(self, graph: pgv.AGraph):
        """
        Convert the builtin to a graph and add it to the graph
        """
        pass

class List(list):
    """
    Custom list class to visualize the list:

    Converts the list into a graph during each rendering
    """

    def __init__(self, data,
                 label = 'Head',
                 display_edges = True,
                 display_index = False,
                 ) -> None:
        
        super().__init__(data)

        # Log for customizations
        self.customizations = defaultdict(dict)

        # Record the list in the graph
        logger.builtins.append(self)

        # Visualization parameters
        self.label = label
        self.display_edges = display_edges
        self.display_index = display_index

        logger.visualize()

    def customize_node(self, node, display_once=True, **kwargs):

        # Go through the entire kwargs and make the keys tuples that include the display_once variable
        for key in kwargs.keys():
            self.customizations[node][key] = (kwargs[key], display_once)

    def __clean_one_time_customizations(self):
        for node in self.customizations:
            for key in list(self.customizations[node].keys()):
                if self.customizations[node][key][1]:
                    del self.customizations[node][key]

    def convert_and_add(self, graph: pgv.AGraph):
        """
        Convert the list to a graph and add it to the graph
        """

        nodes = []

        graph.add_node(self,
                       label=self.label,
                       color='darkblue',
                       shape='box'
                       )
        nodes.append(self)

        """
        Note: important to create ListNodes to avoid colisions
        between nodes with the same index value in different lists

        Graphviz uses the object's string to identify the nodes and
        unique objects will have different default representations.
        """
        class ListNode:
            def __init__(self, value) -> None:
                self.value = value
                self.id = str(uuid.uuid4())

            @property
            def label(self):
                return f"{self.value}"
            
            # Required: to avoid colisions between nodes with the same index value in different lists
            def __str__(self) -> str:
                return f"{self.id}"

        # Create list from 0 to n-1
        last_node = self
        for i in range(len(self)):

            # Create dummy list node
            node = ListNode(i)
            nodes.append(node)

            default_node_kwargs = {
                'color': 'darkblue',
                'shape': 'box',
                'width': '0.5',
                'height': '0.5',
                'group': 'main',
                'id': node.id,
                'label': str(i) if self.display_index else str(self[i]),
            }

            additional_node_kwargs = self.customizations.get(i, {})
            cleaned_additional_node_kwargs = {key: value[0] for key, value in additional_node_kwargs.items()}

            final_node_kwargs = {**default_node_kwargs, **cleaned_additional_node_kwargs}

            # Add to graph with customizations
            graph.add_node(node, **final_node_kwargs)

            # Connect to actual node self[i]
            if self.display_edges:
                graph.add_edge(node, self[i],
                            color='darkblue',
                            style='dashed',
                            arrowsize='0.75'
                            )
            

            # Connect dummy nodes in list
            graph.add_edge(last_node, node, 
                           arrowsize='0.5',
                           )

            last_node = node

        # Keeps the list nodes in a main subgraph line
        graph.add_subgraph(nodes, rankdir='LR', rank='same')

        self.__clean_one_time_customizations()


def class_decorator(cls):
    """
    Decorator for classes to log their instantiation
    """

    orig_init = cls.__init__

    def new_init(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)
        logger.create_node(self)

    cls.__init__ = new_init
    return cls
