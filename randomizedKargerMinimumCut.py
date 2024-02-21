import random
import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest):
        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def contract(self, v, u):  # Merge the vertex v into verterx u and remove v
        self.graph[u].extend(self.graph[v])
        del self.graph[v]

        # Replace all occurence of v with u
        for vertex in self.graph:
            self.graph[vertex] = [u if x == v else x for x in self.graph[vertex]]
        # Remove the self-loops
        self.graph[u] = [x for x in self.graph[u] if x != u]

    def min_cut(self):
        while len(self.graph) > 2:  # Randomly select and edge (u,v)
            u = random.choice(list(self.graph.keys()))
            v = random.choice(self.graph[u])

            # Contract the edge (u,v)
            self.contract(u, v)

        # Return the remaining edges which representes the cut
        return len(self.graph[list(self.graph.keys())[0]])

    def visualize(self, ax):
        G = nx.Graph()
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                G.add_edge(vertex, neighbor)
        nx.draw(G, ax=ax, with_labels=True, font_weight='bold')


if __name__ == "__main__":  # Create a graph
    graph = Graph()
    graph.add_edge(2, 4)

    # Perform the karger's min-cut algorithm
    min_cut = graph.min_cut()

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Display the original grapgh
    axs[0].set_title('Original Graph')
    graph.visualize(axs[0])

    # Display the min-cut graph
    axs[1].set_title('Min-Cut Graph')
    axs[1].add_patch(plt.Circle((0.5, 0.5), 0.3, color='white', zorder=0))
    axs[1].text(0.5, 0.5, '4', ha='center', va='center', fontsize=12, fontweight='bold')
    axs[1].text(0.8, 0.5, '2', ha='center', va='center', fontsize=12, fontweight='bold')
    axs[1].plot([0.5, 0.8], [0.5, 0.5], color='black', zorder=1)

    # print the min-cut in the terminal
    print("Min-Cut: ", min_cut)

    plt.show()
