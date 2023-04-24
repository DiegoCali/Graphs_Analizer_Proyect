from Graph_Parts import *
from Lists import *
from Graph import Graph
import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as msg


def dijkstra_shortest_path(graph, start, end, top_n):
    paths = []

    def dfs(node, path):
        if node == end:
            paths.append(path[:])
        else:
            for neighbor in graph[node]:
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, path)
                    path.pop()

    dfs(start, [start])
    paths.sort(key=lambda x: len(x))
    top_paths = paths[:top_n] if top_n else paths
    return top_paths


def is_connected(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    initial_node = list(graph.keys())[0]
    dfs(initial_node)
    return len(visited) == len(graph)


def dijkstra():
    graph = Graph(list_nodes.list_nodes)
    new_graph = graph.create_graph()
    name_init_node = simpledialog.askstring("Initial Node",
                                            "Please write the name of the initial node", parent=window)
    if name_init_node is not None and is_connected(new_graph):
        is_in_graph = list_nodes.search_node_by_name(name_init_node)
        global_path.clear()
        if name_init_node is not None and is_in_graph:
            name_end_node = simpledialog.askstring("End Node",
                                                   "Please write the name of the last node", parent=window)
            also_in_graph = list_nodes.search_node_by_name(name_end_node)
            if name_end_node is not None and also_in_graph:
                path = dijkstra_shortest_path(new_graph, name_init_node.upper(), name_end_node.upper(), 3)
                counter, length = 0, len(path[0])
                first_path = path[0]
                list_edges.reinit_edges(canvas)
                for paths in path:
                    global_path.append(paths)
                while counter < length - 1:
                    name = first_path[counter] + first_path[counter + 1]
                    list_edges.paint_edge(name, canvas)
                    counter = counter + 1
                for node in list_nodes.list_nodes:  # we repaint the nodes so the edges are left behind
                    node.paint_node(canvas)
                    node.change_color("yellow", canvas)
            else:
                msg.showinfo(title="Error", message=f"There is no node named {name_end_node}")
        else:
            msg.showinfo(title="Error", message=f"There is no node named {name_init_node}")
    else:
        if not is_connected(new_graph):
            msg.showinfo(title="Error", message="The graph is not connected")


def create_node(event):
    x, y = event.x, event.y
    coords = (x, y)
    name = simpledialog.askstring("Name the node",
                                  "Input a name for the node:", parent=window)
    exists = list_nodes.search_node_by_name(name)
    if name is not None and not exists:
        new_node = Node(name.upper(), coords)
        list_nodes.add(new_node)
        new_node.paint_node(canvas)
    elif exists:
        msg.showinfo(title="Error", message=f"The Node {name.upper()} already exists")


def create_edge(event):
    x, y = event.x, event.y
    coords = (x, y)
    is_touching, node_touched = list_nodes.search_node(coords)
    if is_touching:
        node_touched.change_color("red", canvas)
        canvas.bind("<Button-3>", lambda e: finish_edge(e, node_touched))  # we change the right click func


def finish_edge(event, first_node):
    coords_last_node = (event.x, event.y)
    is_touching, last_node = list_nodes.search_node(coords_last_node)
    if is_touching:
        new_edge = Edge("", first_node, last_node)
        new_edge.paint_edge(canvas)  # create a new edge
        list_edges.add(new_edge)
        first_node.add_linked_node(last_node)
        last_node.add_linked_node(first_node)
        for node in list_nodes.list_nodes:  # we repaint the nodes so the edges are left behind
            node.paint_node(canvas)
            node.change_color("yellow", canvas)
    canvas.bind("<Button-3>", create_edge)  # we re-initiate the button event to create another edge


def re_init():
    canvas.delete("all")
    list_nodes.list_nodes = []
    list_edges.list_of_edges = []
    global_path.clear()


actual_path_counter = 1


def refresh():
    global actual_path_counter
    counter, length_global = 0, len(global_path)
    actual_path = []
    if length_global == 0:
        msg.showinfo(title="Error", message="You haven't analyze any graph yet")
    else:
        if actual_path_counter == length_global:
            actual_path_counter = 0
            actual_path = global_path[actual_path_counter].copy()
            actual_path_counter += 1
        else:
            actual_path = global_path[actual_path_counter].copy()
            actual_path_counter += 1
    list_edges.reinit_edges(canvas)
    length_actual = len(actual_path)
    while counter < length_actual - 1:
        name = actual_path[counter] + actual_path[counter + 1]
        list_edges.paint_edge(name, canvas)
        counter = counter + 1
    for node in list_nodes.list_nodes:  # we repaint the nodes so the edges are left behind
        node.paint_node(canvas)
        node.change_color("yellow", canvas)


if __name__ == '__main__':
    global_path = []
    list_nodes = ListNodes()
    list_edges = ListEdges()
    window = tk.Tk()
    window.title("Graphs Theory (Dijkstra)")
    window.resizable(False, False)
    canvas = tk.Canvas(window, width=500, height=500)
    canvas.pack()
    canvas.bind("<Button-1>", create_node)  # if clicked the left click
    canvas.bind("<Button-3>", create_edge)  # if clicked the right click
    button_analyze = tk.Button(window, text="Analyze Graph", command=dijkstra)
    button_analyze.pack()
    button_analyze.place(x=10, y=10)
    button_reinit = tk.Button(window, text="Clear", command=re_init)
    button_reinit.pack()
    button_reinit.place(x=100, y=10)
    button_refresh = tk.Button(window, text="Refresh", command=refresh)
    button_refresh.pack()
    button_refresh.place(x=140, y=10)
    window.mainloop()
