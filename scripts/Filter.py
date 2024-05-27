import matplotlib.pyplot as plt
import networkx as nx

# Create a new directed graph
G = nx.DiGraph()

# Add nodes with the node for the root and then leaves
G.add_node("Filter")  # Root node
leaves = ["QuickFilter", "SlowFilter", "LogicalFilter"]
for leaf in leaves:
    G.add_node(leaf)
    G.add_edge("Filter", leaf)  # Connect each leaf to the root

# Graph layout settings
pos = nx.spring_layout(G, seed=42)  # For consistent layout

# Drawing the nodes with specific styles
node_colors = ['green' if node == "Filter" else 'skyblue' for node in G.nodes()]
node_sizes = [7000 if node == "Filter" else 5000 for node in G.nodes()]

# Draw nodes and edges with custom settings
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Display the plot
plt.title('Tree Diagram of Filters')
plt.show()
