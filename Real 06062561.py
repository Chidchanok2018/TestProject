from networkx import nx
import matplotlib.pyplot as plt
import sys
import math
import operator
import random as ran
import numpy as np
import pandas as pd

fh = open("C:\Users\Kmutt_Wan\PycharmProjects\Book1.txt","r")
#print file.read(fh)
G = nx.read_adjlist(fh)
nx.draw_networkx(G)
plt.savefig("AA.png")
plt.show()
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
#Degr = G.degree()
#Mdegree = sorted([d for n, d in G.degree()], reverse=True)
          #Leanglumdub([won G.degree moveto d],krubdan)
#MDegree = max(Mdegree)#value maksud
#print (MDegree)
#print (Degr)
#-------------------------------------------------------------------------------------------
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
len(cycles)
print (cycles)
#-----------------------------------------------------------------
list3 = []
for node in cycles:
    if len(node)-1 == 3:
        list3.append(node)

tuple3 = tuple(list3)  #
set3 = {frozenset(x) for x in tuple3}
#print(set3)
set3 = list(set3)
listX = []
#for i in range(len(set3)):
    #listX.append(G.degree(set3[i]))
    #print (listX)
    #nx.draw_networkx((G.subgraph(set3[i])))
    #plt.show()











