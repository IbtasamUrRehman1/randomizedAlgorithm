import heapq
import random
import networkx as nx
import matplotlib.pyplot as plt

def randomized_dijkstra(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    pq = [(0, source)]  # Priority queue with (distance, node) tuples
    visited = set()

    while pq:
        random.shuffle(pq)
        dist, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        for neighbor, weight in graph[current].items():
            new_distance = dist + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distance

def visualize_graph(graph, shortest_paths=None):
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')
    if shortest_paths:
        for path in shortest_paths:
            nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='red', width=2.0, arrows=True)
    plt.axis('off')
    plt.show()

# Example graph represented as an adjacency list
graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}}
source_node = 'A'

# Randomized Dijkstra's algorithm
shortest_distances = randomized_dijkstra(graph, source_node)

# Generate random shortest paths for visualization
def generate_random_shortest_paths(graph, source, shortest_distances):
    random_shortest_paths = []
    for target, distance in shortest_distances.items():
        path = [target]
        current = target
        while current != source:
            neighbors = [(neighbor, weight) for neighbor, weight in graph[current].items()]
            random.shuffle(neighbors)  # Ensure neighbors are shuffled before selecting the next node
            for neighbor, weight in neighbors:
                if shortest_distances[current] == shortest_distances[neighbor] + weight:
                    path.insert(0, neighbor)
                    current = neighbor
                    break
        random_shortest_paths.append([(path[i], path[i + 1]) for i in range(len(path) - 1)])
    return random_shortest_paths

# Visualize the original graph and random shortest paths
visualize_graph(graph, generate_random_shortest_paths(graph, source_node, shortest_distances))
