
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
        response = False
        for node in self.list_nodes:
            if node.name.upper() == name.upper():
                response = True
                break
        return response
