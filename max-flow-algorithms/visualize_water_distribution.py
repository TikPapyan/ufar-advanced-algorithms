import os
import plotly.graph_objects as go
import networkx as nx

from dinics_algorithm import DinicsAlgorithm

def save_visualization(irrigation, title, filename):
    G = nx.DiGraph()
    
    for (u, v), capacity in irrigation.capacity.items():
        if capacity > 0:
            flow = capacity - irrigation.capacity[(v, u)]
            G.add_edge(u, v, capacity=capacity, flow=flow)
    
    pos = nx.spring_layout(G, seed=42)
    
    edge_x = []
    edge_y = []
    edge_text = []
    
    for u, v, data in G.edges(data=True):
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_text.append(f"Flow: {data['flow']}/{data['capacity']}")

    node_x = []
    node_y = []
    node_text = []
    for node, (x, y) in pos.items():
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"Node {node}")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=2, color='gray'),
        hoverinfo='text',
        text=edge_text,
        mode='lines',
        showlegend=False
    ))

    fig.add_trace(go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        text=node_text,
        marker=dict(size=20, color='lightblue'),
        textposition="bottom center",
        showlegend=False
    ))

    fig.update_layout(
        title=title,
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        hovermode='closest'
    )

    if not os.path.exists('visualization'):
        os.makedirs('visualization')
    fig.write_image(f"visualization/{filename}.png")

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

save_visualization(irrigation, "Initial Irrigation Network", "irrigation_network_initial")

max_flow = irrigation.max_flow(source, sink)
print(f"Maximum water flow from source to sink: {max_flow}")

save_visualization(irrigation, "Final Irrigation Network", "irrigation_network_final")
