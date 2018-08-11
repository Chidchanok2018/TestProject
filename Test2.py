from networkx import *
import matplotlib.pyplot as plt
import sys
import math
import operator
import random as ran
import numpy as np
import pandas as pd
import tarfile
G = nx.Graph()
fh = open("C:\Users\Kmutt_Wan\PycharmProjects\simulated_blockmodel_graph_500_nodes_snowball_1.txt","rb")
#tar = tarfile.open("C:\Users\Kmutt_Wan\PycharmProjects\1facebook.tar.gz", "r:gz")
G = read_adjlist(fh)
#plt.figure(1)
#draw_networkx(G)
# nx.draw(G, edge_color='b', with_labels=True, edge_label=True, pos=spectral_layout(G, weight='1', scale=1.0, center=None))
# draw_spectral(G)
nx.draw(G, pos=nx.spring_layout(G))
cycles = [c for c in nx.cycle_basis(G) if len(c)==3]
cy = [h for h in nx.degree(G) if len(h)==1]
print 'Number of cycles_Sub3',len(cycles)
print 'cy',len(cy)
print 'Nodes',len(G.nodes)
print 'Edges',len(G.edges)
plt.savefig("PICsimulated1000_Edges_Py")
plt.show()