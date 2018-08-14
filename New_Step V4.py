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

# -------Original Graph--------#
Number_of_nodes = len(G.nodes)  # หาจำนวนโหนดทั้งหมด
Number_of_Edges = len(G.edges)  # หาจำนวนกิ่งทั้งหมด
print'Number Of Nodes_Real', Number_of_nodes  # พิมพ์จำนวนโหนดทั้งหมด
print'Number Of Edges_Real', Number_of_Edges  # พิมพ์จำนวนกิ่งทั้งหมด
Node_Degree = [i for i in G.degree]  # ระบุจำนวนก่งในกราฟ
Max_Degree = int(max(Node_Degree[1]))  # หากิ่งที่มีดีกรีสูงสุดในกราฟ V.pro
Max_Degree_Show = int(max(Node_Degree[1])) + 1  # หากิ่งที่มีดีกรีสูงสุด V.Show
print 'Max Degree of Node', Max_Degree_Show  # พิมพ์กิ่งที่มีดีกรีสูงสุด
Min_Degree = int(min(Node_Degree[1]))  # หากิ่งที่มีดีกรีน้อยที่สุดในกราฟ V.pro
Min_Degree_Show = int(min(Node_Degree[1])) + 1  # หากิ่งที่มีดีกรีน้อยที่สุด V.Show
print 'Min Degree of Node', Min_Degree_Show  # พิมพ์จำนวนกิ่งที่มีดีกรีน้อยที่สุด

# ----Check Highly Connection----------#
print 'Highly Solution 1 = edge in graph > n / 2'
if Number_of_Edges >= (Number_of_nodes / 2):  # เช็คว่ากราฟเป็น Highly Con. หรือไม่
    print '= Yes ,', (Number_of_nodes / 2)  # ถ้าใช้เป็น Yes
else:
    print '= NO'  # ถ้าไม่ใช่เป็น No

# --------เตรียม Sub cycles เ---------------#
Sub3 = [c for c in nx.cycle_basis(G) if len(c) == 3]  # หา Sub = 3 โหนดในกราฟ List
print'Len of Sub3', len(Sub3), 'Cycles'  # พิมพ์จำนวน cycle3 ในกราฟ
Sub4 = [c for c in nx.cycle_basis(G) if len(c) == 4]  # หา Sub = 4 โหนดในกราฟ List
print'Len of Sub4', len(Sub4), 'Cycles'  # พิมพ์จำนวน cycle4 ในกราฟ
Sub_cycle3_sort = sorted(Sub3)  #  เรียง Sub3 ใหม่จากน้อยไปมาก
# print'Sub_cycle3_MaDeg', Sub_cycle3_sort  # พิมพ์ Sub3
Sub_cycle4_MaDeg = sorted(Sub4)  # เรียง Sub4 ใหม่จากน้อยไปมาก

# ------Definition Function-------------#
def Next_SubN2(Start, Compare):  # Function หา Sub รอบๆ sub แรกที่เหมือนกัน 2 โหนด
    Scycle_same2 = []  # กำหนด type ให้
    for h in Start:  # แต่ละตัวใน A_Subcycle (ตัวตั้งต้น)
        count = len(Start) - 1  # นับจำนวนแต่ละตัวใน A_Subcycle (ตั้งต้น)
        for i in range(count):  # แต่ละตัวใน A_Subcycle จำนวนรอบเท่ากับ count
            print '-------Next_Scycle---------------'
            print 'Len i', i
            Start_Scycle = set(h)  # ให้ Start_Scycle คือตัวแรกใน Start
            print'StartScycle', Start_Scycle
            Next_Scycle = set(Compare[i + 1])  # ให้ Next คือลำดับที่ 1 ของ AN_Subcycle
            print'NextScycle', Next_Scycle
            a = Start_Scycle & Next_Scycle  # ให้ a คือตัวที่ แตกต่าง กันของ Start กับ Next
            print'StartAndNext', a
            # b = Start_Scycle - Next_Scycle #เอาที่ไม่เหมือน
            # print'StartOrNext', b
            if len(a) >= 2.0:  # ถ้า จำนวนของ a มากกว่าเท่ากับ 2
                Merge_Sub = Start_Scycle | Next_Scycle  # ให้ Mearge_Sub เท่ากับ Start U Next
                Scycle_same2.append(Next_Scycle)  # ให้ เพิ่ม Next ใน Scycle_same2
            if Start_Scycle == Next_Scycle:  # ถ้า Start = next
                print'=='  # พิมพ์ ==
            if a == set([]):  # ถ้า a เป็น set([])
                print'[]'  # ให้พิมพ์ []
        return Scycle_same2  # ส่งค่า Scycle_same2 [set([],[],...)]

def interintra(Start, Compare):  # Function หาค่า interintra ของ Sub ที่เอามาต่อแบบ 2 โหนดเท่านั้น
    for o in Start:  # แต่ละตัวใน Start (ตัวตั้งต้น)
        Cluster = []  # กำหนด type ให้ Cluster [list]
        Keep = []  # กำหนด type ให้ Keep [list]
        count = len(Start) - 1  # นับจำนวนแต่ละตัวใน Start
        for o1 in range(count):  # แต่ละตัวใน Start จำนวนรอบเท่ากับ count
            print'-----------inter-intra----------------'
            G = nx.Graph()
            Start_Sub = list(o)  # Start ให้เป็น list
            if len(Cluster) >= 3:
                Start_Sub = a
            Next_Sub = list(Compare[o1 + 1])
            a = Start_Sub + Next_Sub
            G.add_cycle(a)
            p = len(G.degree(a))
            b = set(Start_Sub) & set(Next_Sub)
            if len(b) >= 2:  # ถ้า จำนวนของ a มากกว่าเท่ากับ 2
                Dif_Den_N2 = 0.00  # ให้หมดนี่เท่ากับ 0.00
                Dif_Den_N1 = 0.00
                Re_inter4 = 0.00
                Re_inter5 = 0.00
                Re_intra5 = 0.00
                Re_intra4 = 0.00
                Number_of_Edges_Out = 0.00
                Source = o1 + 1.00  # จำนวนรอบหมุนเพิ่ม 1
                Number_of_Edes_All = float(len(G.edges(a)))  # จำนวนกิ่งทั้งหมดของ F1
                N = float(len(G.nodes(a)))
                N_C = float(len(G.nodes(a)))
                if (N_C * (N - N_C)) <= 0.00:
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
                print 'Difference Density =', " %+2.2f" % Dif_Den_N2
            if Dif_Den_N2 >= 0.50:
                Cluster = a
        return Cluster

# --------------Main Program----------------
S3N2 = Next_SubN2(Sub3, Sub_cycle3_sort) # [set([u'11', u'65', u'79'])
S3N2_Sorted = sorted(S3N2)
S3N2_Sorted_inter = interintra(S3N2, S3N2_Sorted)

# --------------Print Detail----------------
print'Sub_AroundN2 =', S3N2
print'Len_Sub_AroundN2 =', len(S3N2)
print'S3N2_Sorted_inter =', S3N2_Sorted_inter

# --------------Draw Graph-----------------
G = nx.Graph()
G.add_cycle(S3N2_Sorted_inter)
nx.draw(G, with_labels=True)
plt.show()