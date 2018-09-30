# -*- coding: utf-8 -*-
from networkx import *
import matplotlib.pyplot as plt
import numpy as np
import random
import copy


G = nx.Graph()
# k = Graph
# G = nx.complete_graph(4)  # Fully Graph
# draw_networkx(G, edge_color='skyblue', node_color='red')
# plt.show()
# Sub3 = [c for c in nx.minimum_cycle_basis(G)]
# for h in nx.minimum_spanning_tree(G):
#     h
# print Sub3

# G = nx.balanced_tree(2,3)  # Tree 2 คือกิ่ง 3 คือลำต้น
# G = nx.barbell_graph(3,8)  # 3 คือฟูลลี่ 8 คือสร้อยเชื่อม
# G = nx.complete_multipartite_graph(10,10,30)  # ตัวเลขคือจำนวนโหนด คู่แรกคือความหนาแน่นตรงกลางยิ่งเยอะยิ่งหนาแน่นมาก
# G = nx.cycle_graph(10)  # วง
# G = nx.circular_ladder_graph(10)  # วงล้อ 2 วง
# k = Graph.Erdos_Renyi(n=10, m=10)
# G = nx.gnm_random_graph(50,200)  # ตัวแรกจำนวนโหนด ตัวหลังจำนวนกิ่ง
# G = nx.dense_gnm_random_graph(50,500)
# nx.write_edgelist(G,"C:\Users\Kmutt_Wan\PycharmProjects\Nodes50_500_2.tsv",delimiter=' ',data=True)

fh = open("C:\Users\Kmutt_Wan\PycharmProjects\Nodes50_550.txt", "rb")
G = read_adjlist(fh)

# pos = {0: (100, 100), 1: (20, 30), 2: (40, 30), 3: (30, 10)}
# print 'aaa'
# Node = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print Node
# N1 = 1
# N2 = 101
# i = range(N1, N2)  # list i [1, 1,...,100]
# random.shuffle(i)
# i2 = copy.deepcopy(i)
# random.shuffle(i2)
# pos = {}
# R = []
# p = 0
# for h in i:
#     R3 = []
#     R1 = i[p]
#     R2 = i2[p]
#     R3 = [R1,R2]
#     R3 = tuple(R3)
#     pos[p] = R3
#     p += 1
pos = {}
l = len(G.node)
N1 = 0
N2 = l
i = range(N1, N2)
random.shuffle(i)
i2 = copy.deepcopy(i)
random.shuffle(i2)
p = 0
c = zip(i,i2)
for h in c:
    pos[p] = h
    p += 1
# for h in i:
#     R3 = []
#     R1 = i[p]
#     R2 = i2[p]
#     R3 = [R1,R2]
#     R3 = tuple(R3)
#     pos[p] = R3
#     p += 1

Edges_Graph = [i for i in G.edges]

K = nx.Graph()  # ไม่ให้ทำกับกราฟเก่า
K.add_nodes_from(pos.keys())  # บอกว่าจะเริ่มเพิ่มโหนดตามนี้ โหนดเป็น int
for n, p in pos.iteritems():
    K.node[n]['pos'] = p

for u in Edges_Graph:  # จะเพิ่มกิ่งจากกราฟ G เปลี่ยนเป็น int
    u = list(u)
    K.add_edge(int(u[0]), int(u[1]))

Q = 8  # ตัวเปลี่ยนสีใน colorList
# colorList = ['red','yellow','brown','purple','skyblue','green','Salmon','c','magenta','orange','white','black','y','GreenYellow','cyan']
colorList = ['SeaGreen','yellow','brown','pink','purple','blue','green','Salmon','red','c','magenta','orange','white','black','y','skyblue','GreenYellow','cyan','aqua']
draw_networkx(K, pos, edge_color='skyblue', node_color='black')
draw_networkx(G, edge_color='skyblue', node_color=colorList[Q%len(colorList)])
plt.show()

