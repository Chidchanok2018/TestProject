# -*- coding: utf-8 -*-
from networkx import *
import matplotlib.pyplot as plt
import sys
import math
import operator
import random
import numpy as np
import pandas as pd
G = nx.Graph()
fh = open("C:\Users\Kmutt_Wan\PycharmProjects\simulated_blockmodel_graph_500_nodes_snowball_2.txt", "rb")
G = read_adjlist(fh)
#-------Original Graph--------#
Number_of_nodes = len(G.nodes)
Number_of_Edges = len(G.edges)
print'Number Of Nodes_Real', Number_of_nodes
print'Number Of Edges_Real', Number_of_Edges
Node_Degree = [i for i in G.degree]
Max_Degree = int(max(Node_Degree[1]))
Max_Degree_Show = int(max(Node_Degree[1]))+1
print 'Max Degree of Node', Max_Degree_Show
Min_Degree = int(min(Node_Degree[1]))
Min_Degree_Show = int(min(Node_Degree[1]))+1
print 'Min Degree of Node', Min_Degree_Show
#----Check Highly Connection----------#
print 'Highly Solution 1 = edge in graph > n / 2'
if Number_of_Edges >= (Number_of_nodes/2):
    print '= Yes ,', (Number_of_nodes/2)
else:
    print '= NOT'
#--------เตรียม Sub cycles เ---------------#
Sub3 = [c for c in nx.cycle_basis(G) if len(c) == 3]
print'Len of Sub3', len(Sub3), 'Cycles'
Sub4 = [c for c in nx.cycle_basis(G) if len(c) == 4]
print'Len of Sub4', len(Sub4), 'Cycles'
Sub_cycle3_sort = sorted(Sub3)
#print'Sub_cycle3_MaDeg', Sub_cycle3_sort
Sub_cycle4_MaDeg = sorted(Sub4)
#------Definition Function-------------#
def Next_Scycle(A_Subcycle,AN_Subcycle):
    Scycle_same2 = []
    for h in A_Subcycle:
        count = len(A_Subcycle) - 1
        for i in range(count):
            print '------------------------------'
            print 'Len i', i
            Start_Scycle = set(h)
            Next_Scycle = set(AN_Subcycle[i + 1])
            print'Len NextScycle', Next_Scycle
            a = Start_Scycle & Next_Scycle
            b = Start_Scycle - Next_Scycle
            if len(a) >= 2.0:
                Merge_Sub = Start_Scycle | Next_Scycle
                Scycle_same2.append(Merge_Sub)
            if Start_Scycle == Next_Scycle:
                print'=='
            if a == set([]):
                print'[]'

        return Scycle_same2

#--------------Main Program----------------
S3 = Next_Scycle(Sub3,Sub_cycle3_sort)
S4 = Next_Scycle(Sub4,Sub_cycle4_MaDeg)
print'Len S3', len(S3)
print'S3', S3
print'Len S4', len(S4)
print'S4', S4
