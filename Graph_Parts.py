from Figures import *


class Node:
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
        self.visited = False
        self.circle = Circle(self.name, 20, self.coords, "yellow")
        self.linked_nodes = []

    def change_color(self, color, c):
        self.circle.change_color(color, c)

    def paint_node(self, c):
        self.circle.paint(c)

    def add_linked_node(self, node):
        self.linked_nodes.append(node)

    def get_linked_nodes(self):
        linked_nodes_names = []
        for node in self.linked_nodes:
            linked_nodes_names.append(node.name)
        return linked_nodes_names


class Edge:
    def __init__(self, weight, node_init, node_end):
        self.weight = weight
        self.node_init = node_init.name
        self.node_end = node_end.name
        self.node_init_coords = node_init.coords
        self.node_end_coords = node_end.coords
        self.line = Line(self.weight, self.node_init_coords, self.node_end_coords, "black")

    def paint_edge(self, c):
        self.line.paint(c)
