import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_node('A2')
g.add_nodes_from(['A3', 'A4', 'A5'])

g.add_edge('A2', 'A3')
g.add_edges_from([('A3', 'A4'), ('A4', 'A5')])

for i in range(2, 6):
    g.add_edge(f'B{i}', f'C{i}')
    if 2 < i < 5:
        g.add_edge(f'B{i}', f'B{i+1}')
    if i < 5:
        g.add_edge(f'C{i}', f'C{i+1}')

print(f'{g.number_of_edges()} nodes.')
print(f'{g.number_of_edges()} edges.')
print(f'adjacent nodes to C3: {list(g["C3"])}')
print(f'edges adjacent to C3: {list(g.edges("C3"))}')

nx.draw_networkx(g)
plt.savefig('./img/undirected_graph.png')