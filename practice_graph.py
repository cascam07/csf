import networkx as nx
import matplotlib.pyplot as plt

practice_graph = nx.Graph()
practice_nodes = ['a','b','c','d','e','f']
practice_edges = [('a','b'),('a','c'),('b','c'),('b','d'),('c','d'),('c','f'),
                ('d','f'),('d','e')]
practice_graph.add_nodes_from(practice_nodes)
practice_graph.add_edges_from(practice_edges)
nx.draw(practice_graph)
plt.show()