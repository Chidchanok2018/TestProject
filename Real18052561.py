from networkx import *
import matplotlib.pyplot as plt
import sys
import math
import operator
import random as ran
import numpy as np
import pandas as pd

fh = open("TestLittle","rb")
G = read_adjlist(fh)

plt.figure(1)
draw_networkx(G)

FD =  len(G['C'])
print (FD)

edgeslist = list(G.edges)
H = nx.Graph(edgeslist)
draw_networkx(H)
