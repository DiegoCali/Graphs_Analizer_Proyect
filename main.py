from Graph_Parts import *
from Lists import *
import heapq
from Graph import Graph
import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as msg


def dijkstra_shortest_path(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    predecessors = {node: None for node in graph}
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_node == end:
            path = []
            while curr_node is not None:
                path.append(curr_node)
                curr_node = predecessors[curr_node]
            return curr_dist, list(reversed(path))
        if curr_dist > dist[curr_node]:
            continue
        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                predecessors[neighbor] = curr_node
                heapq.heappush(pq, (distance, neighbor))
    return None


def dijkstra():
    graph = Graph(list_nodes.list_nodes)
    new_graph = graph.create_graph()
    name_init_node = simpledialog.askstring("Initial Node",
                                            "Please write the name of the initial node", parent=window)
    is_in_graph = list_nodes.search_node_by_name(name_init_node)
    if name_init_node is not None and is_in_graph:
        name_end_node = simpledialog.askstring("End Node",
                                               "Please write the name of the last node", parent=window)
        also_in_graph = list_nodes.search_node_by_name(name_end_node)
        if name_end_node is not None and also_in_graph:
            distance, path = dijkstra_shortest_path(new_graph, name_init_node.upper(), name_end_node.upper())
            counter, length = 0, len(path)
            list_edges.reinit_edges(canvas)
            while counter < length - 1:
                name = path[counter] + path[counter + 1]
                list_edges.paint_edge(name, canvas)
                counter = counter + 1
            for node in list_nodes.list_nodes:  # we repaint the nodes so the edges are left behind
                node.paint_node(canvas)
                node.change_color("yellow", canvas)
            msg.showinfo(title=f"The shortest path from {name_init_node.upper()} to {name_end_node.upper()}",
                         message=f"Number of edges: {distance}, Path: {path}")
        else:
            msg.showinfo(title="Error", message=f"There is no node named {name_end_node}")
    else:
        msg.showinfo(title="Error", message=f"There is no node named {name_init_node}")


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


if __name__ == '__main__':
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
    window.mainloop()
