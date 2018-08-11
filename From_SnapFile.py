import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

DataFile1 = open('C:\Users\Kmutt_Wan\PycharmProjects\PPP.txt')
G = nx.read_adjlist(DataFile1)
nx.draw(G , edge_color='b',with_labels=True,edge_label=True)

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

cycles = [[node]+path  for node in G for path in dfs(G, node, node)]
print(len(cycles))

list3 = []
for node in cycles:
    if len(node) - 1 == 3:
        list3.append(node)

tuple3 = tuple(list3)  #
set3 = {frozenset(x) for x in tuple3}

G = nx.Graph()
for item3 in list3:
    count = len(item3)-1
    for i in range(count):
        G.add_edge(item3[i],item3[i+1])
        if i == count-1:
            G.add_edge(item3[i+1],item3[0])

nx.draw(G,edge_color='b',with_labels=True,edge_label=True)
plt.show()

