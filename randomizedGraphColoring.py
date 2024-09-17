import random

import matplotlib.pyplot as plt
import networkx as nx

# Randomized Graph Coloring

def randomized_graph_coloring(graph,max_colors):
    colors = [-1] * len(graph)
    for node in range(len(graph)):
        valid_color=[c for c in range(max_colors)
                     if all(colors[n] != c for n in graph[node])]
        colors[node]=random.choice(valid_color)
        visualize(graph, colors)
        plt.pause(1)
    return colors


def visualize(graph,colors):
    G = nx.Graph([(i,j) for i, adj in enumerate(graph) for j in adj])
    nx.draw(G, with_labels=True, node_color=colors,
            cmap=plt.cm.Set3, node_size=500)
    plt.draw()

# Example Graph
graph=[[1,2], [0,2,3], [0,1,3,4], [1,2,4], [2,3]]
plt.ion()
randomized_graph_coloring(graph,3)
plt.ioff()
plt.show()
