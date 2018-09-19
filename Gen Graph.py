# -*- coding: utf-8 -*-
from networkx import *
import matplotlib.pyplot as plt
import numpy as np
import random

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
G = nx.dense_gnm_random_graph(50,150)
nx.write_edgelist(G,"C:\Users\Kmutt_Wan\PycharmProjects\Nodes50_150_1.tsv",delimiter=' ',data=True)

# fh = open("C:\Users\Kmutt_Wan\PycharmProjects\Nodes50.txt", "rb")
# G = read_adjlist(fh)
draw_networkx(G, edge_color='b')
plt.show()

