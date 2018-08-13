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
def Next_Scycle_N2(A_Subcycle,AN_Subcycle):
    Scycle_same2 = []
    for h in A_Subcycle:
        count = len(A_Subcycle) - 1
        for i in range(count):
            print '------------------------------'
            print 'Len i', i
            Start_Scycle = set(h)
            print'StartScycle', Start_Scycle
            Next_Scycle = set(AN_Subcycle[i + 1])
            print'NextScycle', Next_Scycle
            a = Start_Scycle & Next_Scycle #เอาที่เหมือน
            print'StartAndNext', a
            #b = Start_Scycle - Next_Scycle #เอาที่ไม่เหมือน
            #print'StartOrNext', b
            if len(a) >= 2.0:
                Merge_Sub = Start_Scycle | Next_Scycle
                Scycle_same2.append(Next_Scycle)
            if Start_Scycle == Next_Scycle:
                print'=='
            if a == set([]):
                print'[]'
        return Scycle_same2

def interintra(A_Sub_N2,AN_Sub_N2):
    for o in A_Sub_N2:
        Cluster = []
        Keep = []
        count = len(A_Sub_N2) - 1
        for o1 in range(count):
            Start_Scycle = set(o)
            if len(Cluster) > 3:
                Start_Scycle = Cluster
            Next_Scycle = set(AN_Sub_N2[o1 + 1])
            a = Start_Scycle | Next_Scycle
            F = list(a)
            G.subgraph(F)

            if len(a) >= 2:
                Dif_Den_N2 = 0.00
                Dif_Den_N1 = 0.00
                Re_inter4 = 0.00
                Re_inter5 = 0.00
                Re_intra5 = 0.00
                Re_intra4 = 0.00
                Number_of_Edges_Out = 0.00
                Source = o1 + 1.00
                Number_of_Edes_All = float(len(a)) + Source
                N = float(len(a))
                N_C = float(len(a))
                if (N_C*(N-N_C)) <= 0.00:
                    interN4 = 0.00
                    Re_inter4 = interN4
                elif Number_of_Edges_Out <= 0.00:
                    interN4 = 0.00
                    Re_inter4 = interN4
                else:
                    inter_1 = ((N_C * (N - N_C)))
                    inter_2 = (Number_of_Edges_Out) / inter_1
                    Re_inter4 = round(inter_2, 2)
                print 'inter4', " %+2.2f" % Re_inter4
                if (N_C * (N - 1) / 2) <= 0.00:
                    intra4 = 0.00
                    Re_intra4 = intra4
                elif Number_of_Edes_All <= 0.00:
                    intra4 = 0.00
                    Re_intra4 = intra4
                else:
                    intra_1 = (N_C * (N - 1) / 2)
                    intra_2 = (Number_of_Edes_All) / (N_C * (N_C - 1) / 2)
                    Re_intra4 = round(intra_2, 2)
                print 'Re_intra4', " %+2.2f" % Re_intra4
                Dif_Den_N2 = Re_intra4 - Re_inter4
                print 'Difference Density =',  " %+2.2f" % Dif_Den_N2

            if len(a) < 2:
                Dif_Den_N2 = 0.00
                Dif_Den_N1 = 0.00
                Re_inter4 = 0.00
                Re_inter5 = 0.00
                Re_intra5 = 0.00
                Re_intra4 = 0.00
                Number_of_Edges_Out1 = float(len(G.edges(F))) - 2.00
                Number_of_Edes_All1 = float(len(G.edges(F))) - 1.00
                N1 = float(len((G.nodes(F))))
                N_C1 = float(len((G.nodes(F)))) - 1.00
                if (N_C1 * (N1 - N_C1)) == 0.00:
                    inter5 = 0.00
                    Re_inter5 = inter5
                elif Number_of_Edges_Out1 <= 0.00:
                    inter5 = 0.00
                    Re_inter5 = inter5
                else:
                    inter_1X = ((N_C1 * (N1 - N_C1)))
                    inter_2X = (Number_of_Edges_Out1) / inter_1X
                    Re_inter5 = round(inter_2X, 2)
                print 'Re_inter', Re_inter5
                if (N_C1 * (N1 - 1) / 2) <= 0.00:
                    intra5 = 0.00
                    Re_intra5 = intra5
                elif Number_of_Edes_All1 <= 0.00:
                    intra5 = 0.00
                    Re_intra5 = intra5
                else:
                    intra_1X = (N_C1 * (N1 - 1) / 2)
                    intra_2X = (Number_of_Edes_All1) / (N_C1 * (N_C1 - 1) / 2)
                    Re_intra5 = round(intra_2X, 2)
                print 'Re_intra', " %+2.2f" % Re_intra5

                Dif_Den_N1 = Re_intra5 - Re_inter5
                print 'Difference Density =', " %+2.2f" % Dif_Den_N1

            Dif_Den = Dif_Den_N2+Dif_Den_N1
            if Dif_Den >= 0.15:
                Cluster = Next_Scycle | a
            else:
                Keep.append(Next_Scycle)
        return Cluster

def S3N2interintra2(Re_S3N2_interintra,Compare_Sub,Compare_S3_N2):
    for o in Compare_Sub:
        Scycle_same2 = []
        count = len(Compare_Sub) - 1
        for o1 in range(count):
            Start_Scycle = Re_S3N2_interintra
            print'StartScycle', Start_Scycle
            Next_Scycle = set(Compare_Sub[o1 + 1])
            print'NextScycle', Next_Scycle
            a = Start_Scycle & Next_Scycle  # เอาที่เหมือน
            print'StartAndNext', a
            if len(a) >= 2.0:
                if Next_Scycle not in Compare_S3_N2:
                    Merge_Sub = Start_Scycle | Next_Scycle
                    Scycle_same2.append(Next_Scycle)
            if a == set([]):
                print'[]'
        return Scycle_same2
#--------------Main Program----------------
S3_N2 = Next_Scycle_N2(Sub3, Sub_cycle3_sort)
S3_N2_Sorted = sorted(S3_N2)
S3_S2_interintra = interintra(S3_N2, S3_N2_Sorted)
S3N2_inter = S3N2interintra2(S3_S2_interintra,Sub3,S3_N2)



#--------------Print Result----------------
print'S3_N2', S3_N2
print'Len S3_N2 =', len(S3_N2)
print'S3_N2_interintra =', S3_S2_interintra
print'S3N2_inter =', S3N2_inter
print'Len S3N2_inter =', len(S3N2_inter)
