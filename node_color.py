# -*- coding: utf-8 -*-
from networkx import *
import matplotlib.pyplot as plt
import numpy as np
import random
import copy

def Drawsubgraph(HG, DrawGraph):
    #Draw the graph
    #print HG.nodes()
    pos=nx.spring_layout(HG)
    nx.draw_networkx_edges(HG, pos, alpha=0.4)
    #nx.draw_networkx_labels(HG, pos, font_size=10, font_family='sans-serif')
    i = 0
    colorList = ['SeaGreen','yellow','brown','pink','purple','blue','green','Salmon','red','c','magenta','orange','white','black','y','skyblue','GreenYellow','cyan']#,'aqua'
    for key in DrawGraph.keys():
        nx.draw_networkx_nodes(HG, pos, nodelist=DrawGraph[key], node_size=20,node_color=colorList[i%len(colorList)])
        i = i + 1

    plt.title("Network Community Analysis")
    plt.show()