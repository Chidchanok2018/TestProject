# -*- coding: utf-8 -*-
from networkx import *
import matplotlib.pyplot as plt
import sys
import math
import operator
import random
import numpy as np
import pandas as pd
import tarfile

#---------------Read Graph From Data------------#
G = nx.Graph()
fh = open("C:\Users\Kmutt_Wan\PycharmProjects\simulated_blockmodel_graph_500_nodes_snowball_2.txt","rb")
#tar = tarfile.open("C:\Users\Kmutt_Wan\PycharmProjects\1facebook.tar.gz", "r:gz")
G = read_adjlist(fh)
   ##---Draw Original Graph---##
#draw_networkx(G,node_color = 'b') #When open will happen multiple graph

#-------Check For Highly Connexted Graph--------#
Number_of_nodes = len(G.nodes)
Number_of_Edges = len(G.edges)
print 'Number Of Nodes_Real', Number_of_nodes
print 'Number Of Edges_Real', Number_of_Edges
  #--------Check Max Degree of Sub3---------------#
Node_Degree = [i for i in G.degree]  #[(u'24', 15), (u'25', 9), (u'26', 16)....
Re_DegreeM = int(max(Node_Degree[1]))  #int25
Re_DegreeM_P1 = int(max(Node_Degree[1]))+1  #int26 +1 for real value
print 'Max Degree of Node', Re_DegreeM_P1
Re_DegreeMi = int(min(Node_Degree[1]))
print 'Min Degree of Node', Re_DegreeMi
##----Complete G.-------------------------------------##
# print 'Complete Graph = (n(n-1)/2)'
# Number_of_Edges_C = (Number_of_nodes*(Number_of_nodes-1)/2)
# if Number_of_Edges_C >= Number_of_nodes:
#     print '= Yes ,', Number_of_Edges_C
# else :
#     print '= NOT', Number_of_Edges_C
##----Solution 1--------------------------------------##
print 'Highly Solution 1 = edge in graph > n / 2'
if Number_of_Edges >= (Number_of_nodes/2):
    print '= Yes ,', (Number_of_nodes/2)
else:
    print '= NOT'
##----Solution 2--------------------------------------##
# print 'Highly Solution 2 = Minimum of edges >= (n/2)+1'
# if Re_DegreeMi >= ((Number_of_nodes/2)+1):
#     print '= Yes ,', ((Number_of_nodes/2)+1)
# else:
#     print '= NOT'
#
#-------------Check Cycles 3 Nodes--------------#
cycles = [c for c in nx.cycle_basis(G) if len(c)==3]
#print('Cycles',cycles)
print 'Number of cycles_Sub3',len(cycles)
#print 'cycles000',cycles[000]
#print('cmp',cmp(cycles[000],cycles[001]))#compare number
k = G.subgraph(cycles[000])
#print('Degree Of Sub',k.degree) #Particular degree subcycle
    ##-----Draw Sub 3----##
#draw_networkx(k)

#-----------Def calculate Subcycles-------------#
##---Need Number_of_Edges_Add,N_C,N,Number_of_Edes_All---###
#def Solution_Inter_Intra (Number_of_Edges_Add,N_C,N,Number_of_Edes_All):
#    inter = Number_of_Edges_Out / (N_C(N-N_C))
#    intra = Number_of_Edes_All / (N_C(N-1)/2)
#    Difference_Density = intra - inter
#    return Difference_Density

#------------Neigborhood Sub cycles-----------------------#
#Start_Cycles = cycles[1]
Another_cluster = []
Result_Cluster = []
Cluster1 = []
Cluster2 = []
Cluster3 = []
Sort_cycles_Nbegin = sorted(cycles)
#Sort_cyles_Nlast = sorted(cycles, key=lambda i: i[-1])

for h in sorted(Sort_cycles_Nbegin):
    count = len(cycles)-1
    for i in range(count):
        print '-------------------------------------------------'
        print 'Len i', i
        Start_Scycle = set(h)
        if Start_Scycle not in Another_cluster:
            if Start_Scycle not in Result_Cluster:
                Result_Cluster.append(Start_Scycle)
            if len(Result_Cluster) >= 2:
                Start_Scycle = Start_Scycle | Merge_Sub
                #print 'Start_Scycles_Re =', Start_Scycle
        print 'Start_Scycles =', Start_Scycle
        Next_Scycle = set(Sort_cycles_Nbegin[i+1])
        print 'Next_Scycle', Next_Scycle
        a = Start_Scycle & set(Sort_cycles_Nbegin[i+1])
        print 'Len a', len(a)
        if Start_Scycle == Next_Scycle:
            print 'Start = Next'
        elif Start_Scycle & Next_Scycle:  #Intersection, One of set has same
            Merge_Sub = Start_Scycle | Next_Scycle
            Dif_sub = Start_Scycle ^ Next_Scycle
            #print 'Merge_Sub',Merge_Sub
#-----------------------------------------------------------------------#
            F = list(Merge_Sub)
            # print 'List of Merge_Sub', F
            # print 'Len_List of Merge_Sub', len(F)
            G = G.subgraph(Merge_Sub)
#-----------------------------------------------------------------------#
            if len(a) >= 2:
                Dif_Den_N4 = 0.0
                Dif_Den_N5 = 0.0
                Re_inter4 = 0.0
                Re_inter5 = 0.0
                Re_intra5 = 0.0
                Re_intra4 = 0.0
                Number_of_Edges_Out = 0.0
                Number_of_Edes_All = float(len(G.edges(F))) - 1.0
                N = float(len((G.nodes(F))))
                N_C = float(len((G.nodes(F))))
                if (N_C*(N-N_C)) <= 0.0:
                    interN4 = 0.0
                    Re_inter4 = interN4
                elif Number_of_Edges_Out <= 0.0:
                    interN4 = 0.0
                    Re_inter4 = interN4
                else:
                    inter_1 = ((N_C * (N - N_C)))
                    inter_2 = (Number_of_Edges_Out) / inter_1
                    Re_inter4 = round(inter_2, 2)
                print 'inter4', " %+2.2f" % Re_inter4
                if (N_C * (N - 1) / 2) <= 0.0:
                    intra4 = 0.0
                    Re_intra4 = intra4
                elif Number_of_Edes_All <= 0.0:
                    intra4 = 0.0
                    Re_intra4 = intra4
                else:
                    intra_1 = (N_C * (N - 1) / 2)
                    intra_2 = (Number_of_Edes_All) / (N_C * (N_C - 1) / 2)
                    Re_intra4 = round(intra_2, 2)
                print 'Re_intra4', " %+2.2f" % Re_intra4
                Dif_Den_N5 = 0.0
                Dif_Den_N4 = Re_intra4 - Re_inter4
                print 'Difference Density =',  " %+2.2f" % Dif_Den_N4

                if Dif_Den_N4 > 0.5:
                    Result_Cluster.append(Next_Scycle)
                else:
                    Another_cluster.append(Next_Scycle)
#-----------------------------------------------------------------------#
            elif len(a) < 2:
                Dif_Den_N4 = 0.0
                Dif_Den_N5 = 0.0
                Re_inter4 = 0.0
                Re_inter5 = 0.0
                Re_intra5 = 0.0
                Re_intra4 = 0.0
                Number_of_Edges_Out1 = float(len(G.edges(F))) - 2.0
                Number_of_Edes_All1 = float(len(G.edges(F))) - 1.0
                N1 = float(len((G.nodes(F))))
                N_C1 = float(len((G.nodes(F)))) - 1.0
                if (N_C1*(N1-N_C1)) == 0.0:
                    inter5 = 0.0
                    Re_inter5 = inter5
                elif Number_of_Edges_Out1 <= 0.0:
                    inter5 = 0.0
                    Re_inter5 = inter5
                else:
                    inter_1X = ((N_C1*(N1-N_C1)))
                    inter_2X = (Number_of_Edges_Out1) / inter_1X
                    Re_inter5 = round(inter_2X, 2)
                print 'Re_inter', Re_inter5
                if (N_C1 * (N1 - 1) / 2) <= 0.0:
                    intra5 = 0.0
                    Re_intra5 = intra5
                elif Number_of_Edes_All1 <= 0.0:
                    intra5 = 0.0
                    Re_intra5 = intra5
                else:
                    intra_1X = (N_C1 * (N1 - 1) / 2)
                    intra_2X = (Number_of_Edes_All1) / (N_C1 * (N_C1 - 1) / 2)
                    Re_intra5 = round(intra_2X, 2)
                print 'Re_intra', " %+2.2f" % Re_intra5

                Dif_Den_N5 = Re_intra5 - Re_inter5
                print 'Difference Density =', " %+2.2f" % Dif_Den_N5

                if Dif_Den_N5 > 0.5:
                    Result_Cluster.append(Next_Scycle)
                else:
                    Another_cluster.append(Next_Scycle)
            else:
                print 'DD'
        elif a == set([]):
            print 'Set[]'
            if Next_Scycle not in Result_Cluster:
                if Next_Scycle not in Another_cluster:
                    Another_cluster.append(Next_Scycle)
        else:
            print'Out of Loop'

#print 'Result_Cluster', Result_Cluster
# print 'Another_cluster', Another_cluster
#def Neighborhood (start_cycles,Sub1,Sub2,Sub3):
#--------------Draw Cycles 3 nodes--------------#
# G = nx.Graph()
# for item3 in cycles: #each of cycle list
#     count = len(item3)-1 #Check size sub
#     for i in range(count):
#         G.add_edge(item3[i],item3[i+1])
#         if i == count-1:
#             G.add_edge(item3[i+1],item3[0])

#draw_networkx(G,edge_color='b',with_labels=True,edge_label=True) #nodes_green
#----------------Detail of Graph---------------#
# print 'Nodes =', len(G.nodes)
# print 'Edges =', len(G.edges)
#---------Measure of Cluster---------------------#
# N_Nodes_AF_C = len(G.nodes)
# N_Edges_AF_C = len(G.edges)
# Coverage = float(N_Nodes_AF_C) / float(N_Edges_AF_C)
# print 'Coverage =', Coverage

#plt.savefig('SubCyclesimulated100_Edges_Py1')
plt.figure(1)
# draw_networkx(G)  #When open will happen multiple graph#
plt.show()

#----------------Not to use-------------------#
#res =[c for c in nx.Graph(G)]
#pos = nx.spring_layout(G)
#k = G.subgraph(res)
#plt.figure()
#nx.draw(k, pos=pos,edge_color='b', with_labels=True, edge_label=True)
#plt.savefig("Sub1_testfile")
#print(len(k.nodes))
#print(len(k.edges))

#plt.figure(1)
#draw_networkx(G)
#nx.draw(G, edge_color='b', with_labels=True, edge_label=True)
#plt.savefig("PICFacebook1_Py")

#for item3 in Node_Degree:
#    count = len(item3)-1
#    for i in range(count):
        #cmp(item3[i], item3[i + 1])
        #GG = item3[i]>item3[i+1]
        #if i == count - 1:
        #    G.add_edge(item3[i + 1], item3[0])

#for i in Node_Degree:
#    #print i[1] #degree
#    if i[1] == int(max(Node_Degree[1])):
#        print('i')
#MA = [i for i in Node_Degree if i == max(Node_Degree[1])]
#print('Ma',MA)
#indexes = [index for index in range(len(Node_Degree)) if Node_Degree[index] == DDD]
#print('indexs',indexes)

#if Node_Degree>=DDD:
#    print('FF')
#else:print('NotFF')
#print('Node_Degree',Node_Degree)
