import json
import networkx as nx
import matplotlib.pyplot as plt

# Load knowledge graph
with open("data/knowledge_graph.json", "r") as f:
    graph_data = json.load(f)

G = nx.DiGraph()

# Add nodes
for node in graph_data["nodes"]:
    G.add_node(node["id"], type=node["type"])

# Add edges
for edge in graph_data["edges"]:
    G.add_edge(edge["source"], edge["target"], relation=edge["relation"])

# Layout
pos = nx.spring_layout(G, k=0.5)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# Draw edges
nx.draw_networkx_edges(G, pos, arrows=True)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("GitHub Knowledge Graph")

plt.savefig("data/graph_visualization.png", dpi=300)

plt.show()

print("Graph image saved to data/graph_visualization.png")