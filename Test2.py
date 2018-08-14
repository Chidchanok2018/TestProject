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
#fh = open("C:\Users\Kmutt_Wan\PycharmProjects\simulated_blockmodel_graph_500_nodes_snowball_1.txt","rb")
#tar = tarfile.open("C:\Users\Kmutt_Wan\PycharmProjects\1facebook.tar.gz", "r:gz")
#G = read_adjlist(fh)
#plt.figure(1)
#draw_networkx(G)
# nx.draw(G, edge_color='b', with_labels=True, edge_label=True, pos=spectral_layout(G, weight='1', scale=1.0, center=None))
# draw_spectral(G)
F1 = [11,65,79]
F2 = [65,79,22]
F3 = [33,65,79]
F4 = [7,65,79]
F5 = [7,65,79]
F = F1+F2+F2+F3+F4+F5
H = F1-F2
print'F', F
print'H', H
# G.add_cycle(F1)
# G.add_cycle(F2)
# G.add_cycle(F3)
# G.add_cycle(F4)
G.add_cycle(F)
nx.draw(G, with_labels=True)
print'Len', len(G.degree)
#cycles = [c for c in nx.cycle_basis(G) if len(c)==3]
#cy = [h for h in nx.degree(G) if len(h)==1]
#print 'Number of cycles_Sub3',len(cycles)
#print 'cy',len(cy)
#print 'Nodes',len(G.nodes)
#print 'Edges',len(G.edges)
plt.savefig("PICsimulated1000_Edges_Py")
plt.show()