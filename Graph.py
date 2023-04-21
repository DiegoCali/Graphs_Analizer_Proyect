

class Graph:
    def __init__(self, list_all_current_nodes):
        self.list_nodes = list_all_current_nodes
        self.graph = None

    def create_graph(self):
        names_nodes = []
        linked_nodes = []
        for node in self.list_nodes:
            names_nodes.append(node.name)
            linked_nodes.append(node.get_linked_nodes())
        graph_dict = dict(zip(names_nodes, linked_nodes))
        return graph_dict
