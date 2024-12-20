import networkx as nx
import matplotlib.pyplot as plt

# create a graph

graph = nx.Graph()
graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (2, 4)])

# calculate shortest path

shortest_path = nx.shortest_path(graph, source=1, target=4)

# calculate centrality metrics

degree_centrality = nx.degree_centrality(graph)
betweenness_centrality = nx.betweenness_centrality(graph)

# visualize the graph

plt.figure(figsize=(8, 6))
nx.draw(graph, with_labels=True, node_color='lightblue', node_size=700, edge_color='gray')
plt.title('Graph Visualization')
plt.show()

# save results

with open("C:/puredata/graph_theory_results.txt", "w") as f:
    f.write("Shortest Path (1 to 4):\n")
    f.write(f"{shortest_path}\n\n")
    f.write("Degree Centrality:\n")
    f.write(f"{degree_centrality}\n\n")
    f.write("Betweenness Centrality:\n")
    f.write(f"{betweenness_centrality}\n")
