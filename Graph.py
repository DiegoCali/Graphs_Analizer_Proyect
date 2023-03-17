

class Graph:
    def __init__(self, list_all_current_nodes):
        self.list_nodes = list_all_current_nodes
        self.graph = None

    def create_graph(self):
        names_nodes = []
        list_of_dicts = []
        for node in self.list_nodes:
            names_nodes.append(node.name)
            list_of_weights = []
            linked_nodes = node.get_linked_nodes()
            for n in linked_nodes:
                list_of_weights.append(1)
            node_dict = dict(zip(linked_nodes, list_of_weights))
            list_of_dicts.append(node_dict)
        graph_dict = dict(zip(names_nodes, list_of_dicts))
        return graph_dict
