class ListNodes:
    def __init__(self):
        self.list_nodes = []

    def add(self, node):
        self.list_nodes.append(node)

    def show(self):
        for node in self.list_nodes:
            print(node.name + ", ", end="")
        print("")

    def search_node(self, coords):
        x, y = coords[0], coords[1]
        is_a_node = False
        node_touched = None
        for node in self.list_nodes:
            if (node.coords[0] - 12) < x < (node.coords[0] + 12):
                if (node.coords[1] - 12) < y < (node.coords[1] + 12):
                    is_a_node = True
                    node_touched = node
                    break
        return is_a_node, node_touched

    def search_node_by_name(self, name):
        response_node = False
        for node in self.list_nodes:
            if node.name.upper() == name.upper():
                response_node = True
                break
        return response_node


class ListEdges:
    def __init__(self):
        self.list_of_edges = []

    def add(self, edge):
        self.list_of_edges.append(edge)

    def reinit_edges(self, c):
        for edges in self.list_of_edges:
            edges.change_color("black", c)

    def paint_edge(self, name, c):
        painted_edge = None
        for edge in self.list_of_edges:
            if edge.name.upper() == name.upper():
                painted_edge = edge
                break
            if edge.second_name.upper() == name.upper():
                painted_edge = edge
                break
        painted_edge.change_color("red", c)

