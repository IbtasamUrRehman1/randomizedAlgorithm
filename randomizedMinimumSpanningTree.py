import random
import matplotlib.pyplot as plt
import networkx as nx


def prim(graph, start_vertex):
    # Initialize sets to keep track of visited and unvisited vertices
    visited = set()
    unvisited = set(graph.keys())

    # Initialize minimum spanning tree and total weight
    mst = []
    total_weight = 0

    # Add the starting vertex to the visited set
    visited.add(start_vertex)
    unvisited.remove(start_vertex)

    # Iterate until all vertices are visited
    while unvisited:
        min_edge = None
        min_weight = float('inf')

        # Iterate over visited vertices
        for vertex in visited:
            # Iterate over adjacent vertices
            for neighbor, weight in graph[vertex]:
                # If the neighbor is unvisited and the edge weight is smaller than the current minimum
                if neighbor in unvisited and weight < min_weight:
                    min_edge = (vertex, neighbor)
                    min_weight = weight

        # Add the minimum edge to the minimum spanning tree
        mst.append(min_edge)
        total_weight += min_weight

        # Update visited and unvisited sets
        visited.add(min_edge[1])
        unvisited.remove(min_edge[1])

    return mst, total_weight


def visualize_graph(graph, mst_edges):
    G = nx.Graph()
    for vertex in graph:
        G.add_node(vertex)
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # positions for all nodes

    plt.figure(figsize=(8, 6))

    # Draw the original graph
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)},
                                 font_color='black')

    # Highlight the minimum spanning tree edges
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=2.0, alpha=0.7, edge_color='red')

    plt.title("Minimum Spanning Tree Visualization")
    plt.axis('off')
    plt.show()


# Example usage
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2)]
}

start_vertex = 'B'  # Starting vertex

mst_edges, total_weight = prim(graph, start_vertex)
print("Minimum Spanning Tree Edges:", mst_edges)
print("Total Weight:", total_weight)

# Visaulize the graph and minimum spanning tree
visualize_graph(graph, mst_edges)