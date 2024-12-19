import matplotlib.pyplot as plt
import networkx as nx
import os

from dinics_algorithm import DinicsAlgorithm

def visualize_network(irrigation, filename, title, show_flow=False):
    G = nx.DiGraph()

    for (u, v), capacity in irrigation.capacity.items():
        if capacity > 0 or show_flow:
            flow = f"{capacity}" if not show_flow else f"{capacity - irrigation.capacity[(v, u)]}/{capacity}"
            G.add_edge(u, v, capacity=flow)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'capacity')

    edge_colors = []
    for (u, v) in G.edges():
        if show_flow:
            flow_used = capacity - irrigation.capacity[(v, u)]
            edge_colors.append('red' if flow_used == capacity else 'orange' if flow_used > 0 else 'gray')
        else:
            edge_colors.append('gray')

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color=edge_colors, arrowsize=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(title)
    if not os.path.exists("visualization"):
        os.makedirs("visualization")
    plt.savefig(f"visualization/{filename}")
    plt.close()

node_count = 6
source = 0
sink = 5
irrigation = DinicsAlgorithm(node_count)

irrigation.add_edge(0, 1, 16)
irrigation.add_edge(0, 2, 13)
irrigation.add_edge(1, 3, 12)
irrigation.add_edge(2, 1, 4)
irrigation.add_edge(2, 4, 14)
irrigation.add_edge(3, 2, 9)
irrigation.add_edge(3, 5, 20)
irrigation.add_edge(4, 5, 7)

visualize_network(irrigation, "irrigation_network_initial.png", "Irrigation Network - Initial State", show_flow=False)

max_flow = irrigation.max_flow(source, sink)
print(f"Maximum water flow from source to sink: {max_flow}")

visualize_network(irrigation, "irrigation_network_final.png", "Irrigation Network - Final State", show_flow=True)
