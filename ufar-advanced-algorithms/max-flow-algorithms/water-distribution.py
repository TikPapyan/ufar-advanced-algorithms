import collections
import matplotlib.pyplot as plt
import networkx as nx

class DinicsAlgorithm:
    def __init__(self, node_count):
        self.node_count = node_count
        self.graph = [[] for _ in range(node_count)]
        self.capacity = {}

    def add_edge(self, u, v, capacity):
        if (u, v) not in self.capacity:
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.capacity[(u, v)] = capacity
            self.capacity[(v, u)] = 0  # Reverse edge for residual graph
        else:
            self.capacity[(u, v)] += capacity

    def bfs_level_graph(self, source, sink):
        self.level = [-1] * self.node_count
        queue = collections.deque([source])
        self.level[source] = 0

        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if self.level[neighbor] == -1 and self.capacity[(current, neighbor)] > 0:
                    self.level[neighbor] = self.level[current] + 1
                    queue.append(neighbor)

        return self.level[sink] != -1

    def dfs_flow(self, current, sink, flow):
        if current == sink:
            return flow
        for neighbor in self.graph[current]:
            if self.level[neighbor] == self.level[current] + 1 and self.capacity[(current, neighbor)] > 0:
                bottleneck = self.dfs_flow(neighbor, sink, min(flow, self.capacity[(current, neighbor)]))
                if bottleneck > 0:
                    self.capacity[(current, neighbor)] -= bottleneck
                    self.capacity[(neighbor, current)] += bottleneck
                    return bottleneck
        return 0

    def max_flow(self, source, sink):
        total_flow = 0

        while self.bfs_level_graph(source, sink):
            flow = float('inf')
            while flow:
                flow = self.dfs_flow(source, sink, float('inf'))
                total_flow += flow

        return total_flow

# Example usage: irrigation network with 6 nodes
node_count = 6
source = 0  # Reservoir
sink = 5    # Farm (sink)
irrigation = DinicsAlgorithm(node_count)

# Adding edges (u, v, capacity)
irrigation.add_edge(0, 1, 16)  # Reservoir to distribution point 1
irrigation.add_edge(0, 2, 13)  # Reservoir to distribution point 2
irrigation.add_edge(1, 3, 12)  # Distribution point 1 to farm A
irrigation.add_edge(2, 1, 4)   # Distribution point 2 to distribution point 1
irrigation.add_edge(2, 4, 14)  # Distribution point 2 to farm B
irrigation.add_edge(3, 2, 9)   # Farm A to distribution point 2
irrigation.add_edge(3, 5, 20)  # Farm A to sink (farm)
irrigation.add_edge(4, 5, 7)   # Farm B to sink (farm)

# Compute max flow
max_flow = irrigation.max_flow(source, sink)
print(f"Maximum water flow from source to sink: {max_flow}")

# Visualization
def visualize_network(irrigation):
    G = nx.DiGraph()

    for (u, v), capacity in irrigation.capacity.items():
        if capacity > 0:
            G.add_edge(u, v, capacity=capacity)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'capacity')

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Irrigation Network")
    plt.savefig("irrigation_network.png")  # Save the plot as an image
    print("Network visualization saved as 'irrigation_network.png'")

visualize_network(irrigation)
