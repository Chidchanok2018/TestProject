# -*- coding: utf-8 -*-
from networkx import *
import matplotlib.pyplot as plt
import numpy as np
import random
import copy


G = nx.Graph()
# k = Graph
# G = nx.complete_graph(5)  # Fully Graph
# G = nx.balanced_tree(2,3)  # Tree 2 คือกิ่ง 3 คือลำต้น
# G = nx.barbell_graph(3,8)  # 3 คือฟูลลี่ 8 คือสร้อยเชื่อม
# G = nx.complete_multipartite_graph(10,10,30)  # ตัวเลขคือจำนวนโหนด คู่แรกคือความหนาแน่นตรงกลางยิ่งเยอะยิ่งหนาแน่นมาก
# G = nx.cycle_graph(10)  # วง
# G = nx.circular_ladder_graph(10)  # วงล้อ 2 วง
# k = Graph.Erdos_Renyi(n=10, m=10)
# G = nx.gnm_random_graph(50,200)  # ตัวแรกจำนวนโหนด ตัวหลังจำนวนกิ่ง
# G = nx.dense_gnm_random_graph(50,500)
# nx.write_edgelist(G,"C:\Users\Kmutt_Wan\PycharmProjects\Nodes50_500_1.tsv",delimiter=' ',data=True)

# fh = open("C:\Users\Kmutt_Wan\PycharmProjects\Nodes50_500.txt", "rb")
# G = read_adjlist(fh)

# pos = {0: (100, 100), 1: (20, 30), 2: (40, 30), 3: (30, 10)}

Node = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print Node
N1 = 1
N2 = 101
i = range(N1, N2)  # list i [1, 1,...,100]
random.shuffle(i)
i2 = copy.deepcopy(i)
random.shuffle(i2)
pos = {}
R = []
p = 0
for h in i:
    R3 = []
    R1 = i[p]
    R2 = i2[p]
    R3 = [R1,R2]
    R3 = tuple(R3)
    pos[p] = R3
    p += 1

G.add_nodes_from(pos.keys())
for n, p in pos.iteritems():
    G.node[n]['pos'] = p

Q = 1
colorList = ['SeaGreen','yellow','brown','pink','purple','blue','green','Salmon','red','c','magenta','orange','white','black','y','skyblue','GreenYellow','cyan']
# draw_networkx(G, pos, edge_color='b', node_color="skyblue")
draw_networkx(G, pos, edge_color='b', node_color=colorList[Q%len(colorList)])
plt.show()

