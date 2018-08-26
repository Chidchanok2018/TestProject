# -*- coding: utf-8 -*-
from networkx import *
import matplotlib.pyplot as plt
import copy
import sys
import math
import operator
import random
import numpy as np
import pandas as pd

G = nx.Graph()
fh = open("C:\Users\Kmutt_Wan\PycharmProjects\simulated_blockmodel_graph_500_nodes_snowball_1.txt", "rb")
G = read_adjlist(fh)
# draw_networkx(G, edge_color='b')
# plt.figure(1)
# plt.show()
# -------Original Graph--------#
Number_of_nodes = len(G.nodes)  # จำนวนโหนดทั้งหมด int
Number_of_Edges = len(G.edges)  # จำนวนกิ่งทั้งหมด int
print'Number Of Nodes_Real', Number_of_nodes  # พิมพ์จำนวนโหนดทั้งหมด
print'Number Of Edges_Real', Number_of_Edges  # พิมพ์จำนวนกิ่งทั้งหมด
Node_Degree = [i for i in G.degree]  # ระบุจำนวนกิ่งในกราฟ list[('24',5)]
Max_Degree = int(max(Node_Degree[1]))  # หากิ่งที่มีดีกรีสูงสุดในกราฟ int
Max_Degree_Show = int(max(Node_Degree[1])) + 1  # หากิ่งที่มีดีกรีสูงสุด int
print 'Max Degree of Node', Max_Degree_Show  # พิมพ์กิ่งที่มีดีกรีสูงสุด
Min_Degree = int(min(Node_Degree[1]))  # หากิ่งที่มีดีกรีน้อยที่สุดในกราฟ int
Min_Degree_Show = int(min(Node_Degree[1])) + 1  # หากิ่งที่มีดีกรีน้อยที่สุด int
print 'Min Degree of Node', Min_Degree_Show  # พิมพ์จำนวนกิ่งที่มีดีกรีน้อยที่สุด

# ----Check Highly Connection----------#
print 'Highly Solution 1 = edge in graph > n / 2'
if Number_of_Edges >= (Number_of_nodes / 2):  # เช็คว่ากราฟเป็น Highly Con. หรือไม่
    print '= Yes ,', (Number_of_nodes / 2)  # ถ้าใช้เป็น Yes
else:
    print '= NO'  # ถ้าไม่ใช่เป็น No

# --------เตรียม Sub cycles เ---------------#
Sub3 = [c for c in nx.cycle_basis(G) if len(c) == 3]  # Sub = 3 list[['65','79','24']]
# print'Len of Sub3', len(Sub3), 'Cycles'  # พิมพ์จำนวน cycle3 ในกราฟ
Sub_cycle3_sort = sorted(Sub3)  # เรียง Sub3 ใหม่จากน้อยไปมาก list[['11','80','79']]


# print'Sub_cycle3_MaDeg', Sub_cycle3_sort  # พิมพ์ Sub3

# ------Definition Function-------------#
# ใช้งาน 1
def Next_SubN2(Start, Compare):  # เอาเหมือนรอบๆ 2 โหนด
    # Start ใส่ list[['65','79','24']], Next ใส่ list[['11','80','79']]
    Scycle_same2 = []
    Keep = []
    for h in Start:
        count = len(Start) - 1  # นับจำนวนแต่ละตัวใน Start
        for i in range(count + 1):  # แต่ละตัวใน Start รอบ+1 เพื่อจะได้เอา [0]
            Start_Scycle = set(h)  # แต่ละตัวใน Start set(['24','65','24'])
            if i == count:  # เอาตำแหน่ง [0]
                Next_Sub = set(Compare[0])  # set
            if i < count:  # เอาตำแหน่งมากกว่า [0]
                Next_Sub = set(Compare[i + 1])  # set
            a = Start_Scycle & Next_Sub  # ที่แตกต่าง กันของ Start กับ Next set([])
            # b = Start_Scycle - Next_Scycle # เอาที่ไม่เหมือน
            if len(a) == 2.0:  # ถ้า จำนวนของ a มากกว่าเท่ากับ 2
                Merge_Sub = Start_Scycle | Next_Sub  # เอามารวมกัน
                Scycle_same2.append(Next_Sub)  # เพิ่ม Next ใน Scycle_same2
            else:
                Keep.append(Next_Sub)  # set(['95','14','53'])
        return Scycle_same2  # ส่งค่า Scycle_same2 [set([],[],...)]

# ใช้งาน 2
def interintra(Start, Compare):  # Interintra 2 Sub เหมือนกันมากกว่า 2 โหนด
    # Start ใส่ list[set(['11','65','79']), Next ใส่ list[['11','80','79']]
    for o in Start:  # แต่ละตัวใน Start (ตัวตั้งต้น)
        Cluster = []
        Keep = []
        count = len(Start) - 1
        for o1 in range(count + 1):  # แต่ละตัวใน Start รอบ+1 เพื่อจะได้เอา [0]
            # print'-----------inter-intra----------------'
            # print'Round =', o1
            G = nx.Graph()
            Start_Sub = list(o)  # เปลี่ยน Start ให้เป็น list
            if len(Cluster) >= 3:  # ถ้า Start_sub มากกว่าเท่ากับ 3 โหนด
                Start_Sub = a  # ให้ Start_Sub = ผลลัพท์ที่รวมแล้ว
            if o1 == count:
                Next_Sub = list(Compare[0])
            if o1 < count:
                Next_Sub = list(Compare[o1 + 1])  # เปลี่ยน Next ให้เป็น list
            a = Start_Sub + Next_Sub
            G.add_cycle(a)
            p = len(G.degree(a))
            b = set(Start_Sub) & set(Next_Sub)
            Dif_Den_N2 = 0.00  # ให้หมดนี่เท่ากับ 0.00
            if len(b) >= 2:  # ถ้า จำนวนของ a มากกว่าเท่ากับ 2
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
                # print 'inter4', " %+2.2f" % Re_inter4
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
                # print 'Re_intra4', " %+2.2f" % Re_intra4
                Dif_Den_N2 = Re_intra4 - Re_inter4
                # print 'Difference Density =', " %+2.2f" % Dif_Den_N2

            if Dif_Den_N2 >= 0.80:  # กำหนดคุณภาพของ Dif เท่าเดิมแหละ
                Cluster = a
            else:
                Keep = a
        return Cluster

# ใช้งาน 3
def Next_SubN2N1(Start, Compare):  # หา Sub รอบที่ 2 ที่โหนดเหมือน 2
    # Start ใส่ list[.,.,.], Compare หมุนใส่ list[set([],[])]
    Merge = []  # กำหนด type ให้ตัว Return
    Keep = []
    for h in Compare:  # Compare เป็นตัวหมุน
        count = len(Compare) - 1  # จำนวน Start-1
        for i in range(count + 1):  # จำนวนรอบใน count
            # print '-------Next_Scycle---------------'
            # print 'Len Round =', i
            Start_Sub = set(Start)  # ให้ Start เป็น set
            # print'StartScycle', Start_Sub
            if len(Merge) >= 1:
                Start_Sub = Start_Sub | b  # รวมไม่เอาที่ซ้ำ (set)
            if i == count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = set(Compare[0])  # list
            if i < count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = set(Compare[i + 1])  # เปลี่ยน Next ให้เป็น list
            # print'NextScycle', Next_Sub
            a = Start_Sub & Next_Sub  # บอกจำนวนที่แตกต่างของ Start,Next
            if len(a) == 2:  # กำหนดจำนวนโหนดของ Sub ที่จะเอามาต่อ
                b = Start_Sub | Next_Sub
                Merge.append(Next_Sub)
            else:
                Keep.append(Next_Sub)
        return Merge

# ใช้งาน 4
def interintra2(Start, Compare):  # หาค่า interintra แบบเหมือนกัน 1,2,3 โหนด
    # Start ใส่ list[.,.,.], Next ใส่ list[set([],[])]
    for o in Compare:  # แต่ละตัวใน Compare (ตัวตั้งต้น)
        Cluster = []  # กำหนด type ให้ Cluster [list]
        Keep = []
        count = len(Compare) - 1  # นับจำนวนแต่ละตัวใน Compare
        for o1 in range(count + 1):  # หมนุนรอบ Compare
            # print'-----------inter-intra----------------'
            # print'Round =', o1
            G = nx.Graph()
            Start_Sub = Start  # list[.,.,.] ตั้งต้น
            if len(Cluster) >= 3:  # ถ้า Start_sub มากกว่าเท่ากับ 3 โหนด
                Start_Sub = a  # ให้ Start_Sub = ผลลัพท์ที่รวมแล้ว
            if o1 == count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = list(Compare[0])  # list
            if o1 < count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = list(Compare[o1 + 1])  # เปลี่ยน Next ให้เป็น list
            a = Start_Sub + Next_Sub  # list
            G.add_cycle(a)
            p = len(G.degree(a))
            b = set(Start_Sub) & set(Next_Sub)
            # เหมือนกัน 2,3 โหนด
            if len(b) >= 2:  # ถ้า จำนวนของ a มากกว่าเท่ากับ 2 เหมือนกัน 1,2,3 โหนด
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
                # print 'inter4', " %+2.2f" % Re_inter4
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
                # print 'Re_intra4', " %+2.2f" % Re_intra4
                Dif_Den_N2 = Re_intra4 - Re_inter4
                # print 'Difference Density =', " %+2.2f" % Dif_Den_N2
            # เหมือนกันแค่ 1 โหนด
            if len(b) < 2:
                Dif_Den_N2 = 0.0
                Dif_Den_N1 = 0.0
                Re_inter4 = 0.0
                Re_inter5 = 0.0
                Re_intra5 = 0.0
                Re_intra4 = 0.0
                Dif_Den = 0.00
                Number_of_Edges_Out1 = 2.00
                Source = (o1 * 2) + 4.00
                Number_of_Edes_All1 = float(len(G.edges(a)))
                N1 = float(len(G.nodes(a)))
                N_C1 = float(len(G.nodes(a)))
                if (N_C1 * (N1 - N_C1)) == 0.0:
                    inter5 = 0.0
                    Re_inter5 = inter5
                elif Number_of_Edges_Out1 <= 0.0:
                    inter5 = 0.0
                    Re_inter5 = inter5
                else:
                    inter_1X = ((N_C1 * (N1 - N_C1)))
                    inter_2X = (Number_of_Edges_Out1) / inter_1X
                    Re_inter5 = round(inter_2X, 2)
                # print 'Re_inter', Re_inter5
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
                # print 'Re_intra', " %+2.2f" % Re_intra5
                Dif_Den_N1 = Re_intra5 - Re_inter5
                # print 'Difference Density =', " %+2.2f" % Dif_Den_N1
            Dif_Den = Dif_Den_N2 + Dif_Den_N1
            if Dif_Den >= 0.80:  # กำหนดคุณภาพของ Dif
                Cluster = a
            else:
                Keep = a
        return Cluster

# ใช้งาน 5
def CutSub(Start, Compare):  # เอา Start ที่ต่างกับ Compare
    # Start ใส่ list[.,.,.], Next ใส่ list[set([],[])]
    for o in Compare:  # แต่ละตัวใน Compare (ตัวตั้งต้น)
        Start
        Scycle_same2 = []  # เป็น list ว่าง
        Keep = []  # ใส่ที่เหลือไว้เช็ค
        count = len(Compare) - 1  # นับจำนวนแต่ละตัวใน Compare
        for o1 in range(count):  # หมนุนรอบ Compare
            # print'-----------inter-intra----------------'
            # print'Round =', o1
            if Start == [[]]:
                Start_Sub = set()
            else:
                Start_Sub = set(Start)  # เอา Set
            Next_Sub = set(Compare[o1 + 1])  # เอา set
            # ลบออก เหมือนไม่เอา
            a = Start_Sub & Next_Sub  # มีอะไรต่างกัน
            if a == set([]):  # เอาที่ต่างกัน
                Scycle_same2.append(Next_Sub)
            else:
                Keep.append(Next_Sub)
        return Scycle_same2

# ใช้งาน 6
def MergeSubToCluster1(Sub, Sub_sort):  # ตั้งต้นการหาครัสเตอร์1 โหนด 2
    Cluster = []
    Keep = []
    count = len(Sub) - 1
    for h in range(1):
        # หา Sub ที่มีโหนดรอบๆ 2 โหนด
        N2_R0 = Next_SubN2(Sub, Sub_sort)
        if N2_R0 is None:  # ไม่เจอ Sub เหมือนกันแล้ว
            Cluster = Cluster
        elif len(N2_R0) == 0:
            Cluster.append(N2_R0)
        elif len(N2_R0) > 0:
            N2_Sort = sorted(N2_R0)  # Sorted Sub 2
            # คำนวน interintra จาก Sub ที่หามา
            N2_inter_R0 = interintra(N2_R0, N2_Sort)  # Cal inter Sub 2
            if N2_inter_R0 is None:
                print'N2_inter_R0 is None'
            # ได้ผลลัพท์เป็นก้อนยาวๆ
            # ------ หมุนๆ
            Count_Node = len(N2_R0)  # นับจำนวนโหนดที่ได้จากครั้งแรก
            r = 0
            while Count_Node > 0:  # หมุนจนกว่าโหนดที่ได้จาก Count จะเป็น 0
                # หา Sub ที่มีโหนดรอบๆ 2,1 โหนด
                if N2_inter_R0 <= 0:
                    Cluster = Cluster + N2_inter_R0
                if len(N2_inter_R0) >= 1:  # ถ้าคำนวนinterแล้วมี Sub ออกมา
                    # หา Sub รอบๆอีกครั้ง ที่โหนด 2,1
                    N2N1_R1 = Next_SubN2N1(N2_inter_R0, Sub)  # เอา Sub มาต่อเข้า
                    # print 'โหนดที่ใช้ไป', len(N2N1_R1)
                    if len(N2N1_R1) < 1:  # ไม่มีซับเหลือแล้ว
                        Cluster = Cluster + N2_inter_R0
                    if len(N2N1_R1) == 1:  # ไม่มีซับเหลือแล้ว
                        Cluster = Cluster + N2_inter_R0
                    # คำนวน interintra กับ Sub ที่หามา
                    if len(N2_R0) >= 1:  # มี Sub ให้เอาไปคำนวนต่อ
                        N2_inter_R1 = interintra2(N2_inter_R0, N2N1_R1)  # คำนวน interintra
                        # print 'N2_inter_R1', N2_inter_R1
                        if N2_inter_R1 is None:  # Sub ไม่ผ่าน interintra
                            print 'N2_inter_R1 is None'
                            Count_Node = 0
                        else:
                            Cluster = Cluster + N2_inter_R1  # รวมให้เป็นครัสเตอร์
                            # print 'Cluster =', Cluster

                            # เอารอบมาใช้
                            if r == 0:
                                Count_Node = len(N2N1_R1)
                            if r > 0:
                                Count_Node = len(N2N1_R1) - Count_Node
                                # print 'Count_Node1 =', Count_Node
                            r = r + 1



    return Cluster  # S3N2_inter_R0


def MakeCluster(Sub, Sub_Sorted):
    N2_inter_R0 = MergeSubToCluster1(Sub, Sub_Sorted)  # หา Cluster ก้อนแรก
    ClusterS = []
    ClusterS.append(N2_inter_R0)  # เพิ่ม ก้อนแรก ลงใน List
    # ---------Round 2---------
    Rest_S3N2_R0 = CutSub(N2_inter_R0, Sub)  # ตัด Cluster ก้อนแรกออกจาก sub3
    # print'Sub ที่เหลือจากการใช้ครั้ง 2 =', len(Rest_S3N2_R0), 'Cycles'  # จำนวนที่ยังเหลือ
    Count = len(Rest_S3N2_R0)  # ให้ Count คือจำนวนที่ยังเหลือ
    Rest_S3N2_R0_Sorted = sorted(Rest_S3N2_R0)  # จัดเรียงใหม่เพื่อนให้ไม่ซ้ำ
    N2_inter_R1 = MergeSubToCluster1(Rest_S3N2_R0, Rest_S3N2_R0_Sorted)  # ได้ก้อน 2
    ClusterS.append(N2_inter_R1)  # เพิ่ม ก้อน 2 ลงใน List
    r = 0
    while Count > 0:  # หมุนจนกว่า
        if Count >= 1:
            # ---------Round 3---------
            if r == 0:
                N2_inter_R1S = N2_inter_R0 + N2_inter_R1  # บวกก้อน 1 กับก้อน 2
            if r >= 1:
                N2_inter_R1S = N2_inter_R1S + N2_inter_R2
            Rest_S3N2_R1 = CutSub(N2_inter_R1S, Sub)  # ตัด cluster 1 ออกจาก sub3
            # print'Sub ที่เหลือจากการใช้ครั้ง 3 =', len(Rest_S3N2_R1), 'Cycles'  # นับจำนวน
            Count = len(Rest_S3N2_R1)  # ให้ Count คือจำนวนที่ยังเหลือ
            Rest_S3N2_R1_Sorted = sorted(Rest_S3N2_R1)
            N2_inter_R2 = MergeSubToCluster1(Rest_S3N2_R1, Rest_S3N2_R1_Sorted)  # รวมขั้นตอนเป็น 1 Cluster ยาวๆ
            if N2_inter_R2 == [[]]:
                Count = 0
                ClusterS
            else:
                ClusterS.append(N2_inter_R2)
            r = r + 1
            # print'จำนวนครัสเตอร์ในกราฟ =', r
        else:
            print'หมด'

    return ClusterS


# def TerminalInCluster(Terminal):  # จำนวนกิ่งในแต่ละก้อน เฉพาะเทอมินอล
#     M_CV = []
#     G = nx.Graph()
#     for j in Terminal:  # แต่ละก้อนเทอมินอลในก้อนครัสเตอร์
#         G.add_path(j)
#         L_C1 = float(len(G.edges))  # จำนวนกิ่งเทอมินอล
#         M_CV.append(L_C1)
#         plt.show()
#     return M_CV  # จำนวนกิ่งในครัสเตอร์แต่ละครัสเตอร์

def NodesInCluster(Cluster_G):  # โหนดทั้งหมดในทุกก้อนครัสเตอร์
    M_CV = []
    G = nx.Graph()
    for j in Cluster_G:  # แต่ละก้อนครัสเตอร์
        G.add_cycle(j)  # ทำให้ก้อนแรกเป็นกราฟ
        L_C1 = float(len(G.nodes))  # จำนวนโหนดในกราฟ
        # print'โหนดในแต่ละก้อนครัสเตอร์ =', L_C1
        # draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
        # plt.savefig('Snowball2_Test1')
        # plt.figure(1)
        M_CV.append(L_C1)
        plt.show()
    return M_CV  # จำนวนกิ่งในครัสเตอร์ บวกอัตโนมัติแหะ

# ใช้ 11
def MeargeCToList(Cluster_A):  # ทำ [[.....],[...]] เป็น [.........]
    A = []
    for i in Cluster_A:
        A += i
    return A

# ใช้ 12, T1 มี 2 cycles
def RestSub_setTolist(Start):  # ทำ set(['','',''],['','','']) เป็น list[[],[]]
    T1 = []
    for i in Start:
        T = list(i)
        T1.append(T)
    return T1


def TerminalNodesOneCluster(A, B):  # หากิ่งที่ก้อนต่อแบบ 1 ต่อ 1 แล้วรวมเข้ากับก้อนนั้นๆ
    Terminal = []
    keep = []
    h = A
    Start = set(h)
    for j in B:  # แต่ละตู่กิ่งในกิ่งทั้งหมด
        Next = set(j)
        a = Start & Next  # โหนดที่มีซ้ำกัน
        if len(a) == 1:  # ถ้ามีเหมือนกัน 1 โหนด
            a = list(Next)  # เปลี่ยนเป็น list
            b = h + a  # รวมกิ่งที่เพิ่มเข้ามา list
            Start = Start | Next
            Terminal = b
        else:
            keep.append(Next)  # นอกนั้นยัดไว้ใน keep

    return Terminal


def FindTerminalNodesGraph(A, B):  #
    Cluster = []
    for h in A:  # แต่ละก้อนในครัสเตอร์
        if h != []:
            Start = h  # ก้อนครัสเตอร์ก้อนแรก
            inter_Con = TerminalNodesOneCluster(Start, B)
            Cluster.append(inter_Con)
    return Cluster


def TerminalNodesOneCluster_Terminal(A, B):  # หากิ่งที่ก้อนต่อแบบ 1 ต่อ 1 เอาเฉพาะเทอมินอล
    Terminal = []
    keep = []
    h = A
    Start = set(h)
    for j in B:  # แต่ละคู่กิ่งในกิ่งทั้งหมด
        Next = j
        a = Start & Next  # โหนดที่มีซ้ำกัน
        if len(a) == 1:  # ถ้ามีเหมือนกัน 1 โหนด
            c = list(Next)  # เปลี่ยนเป็น list
            # b = h + a  # รวมกิ่งที่เพิ่มเข้ามา list
            # Start = Start | Next
            Terminal.append(c)
        else:
            keep.append(Next)  # นอกนั้นยัดไว้ใน keep
    return Terminal


def FindTerminalNodesGraph_Terminal(A, B):  # เอาเฉพาะเทอมินอล
    Terminal = []
    for h in A:  # แต่ละก้อนในครัสเตอร์
        if h != []:
            Start = h  # ก้อนครัสเตอร์ก้อนแรก
            inter_Con = TerminalNodesOneCluster_Terminal(Start, B)
            Terminal.append(inter_Con)
    return Terminal

# ใช้งาน 7
def Find_terminal(Start, Compare):  # หา  Terminal ที่โหนดเหมือนกัน 1 โหนด
    # Start ใส่ list[.,.,.], Compare หมุนใส่ list[set([],[])]
    Start
    Merge = []  # กำหนด type ให้ตัว Return
    Keep = []
    for h in Compare:  # Compare เป็นตัวหมุน
        count = len(Compare) - 1  # จำนวน Start-1
        for i in range(count + 1):  # จำนวนรอบใน count
            # print '-------Next_Scycle---------------'
            # print 'Len Round =', i
            if Start == [[]]:
                Start_Sub = set()
            else:
                Start_Sub = set(Start)  # ให้ Start เป็น set
            # print'StartScycle', Start_Sub
            # if len(Merge) >= 1:
            # Start_Sub = Start_Sub | b  # รวมไม่เอาที่ซ้ำ (set)
            if i == count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = set(Compare[0])  # list
            if i < count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = set(Compare[i + 1])  # เปลี่ยน Next ให้เป็น list
            # print'NextScycle', Next_Sub
            a = Start_Sub & Next_Sub  # บอกจำนวนที่แตกต่างของ Start,Next
            if len(a) == 1:  # กำหนดจำนวนโหนดของ Sub ที่จะเอามาต่อ
                # b = Start_Sub | Next_Sub
                Merge.append(Next_Sub)
            else:
                Keep.append(Next_Sub)
        return Merge

def Find_termina2(Cluster, Edges):  # หาเทอมินอลโหนดที่มีกิ่งเหมือนกันแต่ละก้อน
    Result = []
    Result1 = []
    Keep = []
    for i in Cluster:
        count = len(Edges)
        # count1 = len(Cluster)
        for h in range(count - 1):
            Start = set(i)
            if Start == set([]):
                Next = i
            if h == 0:
                Next = Edges[h]
            if h > 0:
                Next = Edges[h+1]
            a = Start & set(Next)
            if len(a) == 1:
                Result.append(Next)
                R = len(Result)
            else:
                if a != set([]):
                    Keep.append(Next)
                    K = len(Keep)
        # R1 = copy.deepcopy(Result)
        # K1 = copy.deepcopy(Keep)
        # b = set(R1) & set(K1)
        # Result1.append(R)
        # G.add_edges_from(Result1)
        # draw_networkx(G, edge_color='b')
        # plt.savefig('Snowball2_Test1')
        # plt.figure(1)
        # plt.show()
        return Result

def InsidePlus(A):
    for i in A:
        Start = i
        count = len(A)
        for h in range(count - 1):
            Next = A[h + 1]
            Re = Start + Next
            Start = Re
        return Start

# ใช้งาน 16 intra
def Keep_intra(Cluster_ALL):  # intra
    Result = []
    # ต้องส่งทีละก้อนครัสเตอร์ให้
    for i in Cluster_ALL:  # แต่ละก้อนครัสเตอร์ไซเคิลดั้งเดิม ไม่ต่อโหนดเหลือ
        intra_CE = EdegsInCluster(i)  # จำนวนกิ่งภายในแต่ละก้อนไซเคิล intra
        # print 'จำนวนกิ่งภายในครัสเตอร์ ', i, '=', intra_CE, 'กิ่ง'
        Result.append(intra_CE)
        # for h in Edges_inter.values():  # จำนวนกิ่งภายนอกของแต่ละก้อนครัสเตอร์ inter
        #     inter_CE = h
        #     print 'จำนวนกิ่งภายนอกครัสเตอร์ ', h, '=', inter_CE
        #     NC = float(len(set(i)))
        #     print 'จำนวนโหนดในครัสเตอร์ ', h, '=', NC
        #     for j in Dic_Cluster_RestNodes.values():
        #         N = float(len(set(j)))
        #         print 'จำนวนโหนดทั้งหมดของครัสเตอร์ ', h, '=', N
    return Result  # intra

# ใช้งาน 17  N
def Keep_N(AA):  # Dic_Cluster_RestNodes N
    Result1 = []
    for v in AA.values():
        N = len(set(v))
        Result1.append(N)

    return Result1  # []

# ใช้งาน 18 iner
def Keep_inter(BB):
    Result2 = []
    for k in BB.values():
        Result2.append(k)
    return Result2

# ใช้งาน 19
def Keep_NC(CC):
    Result3 = []
    for j in CC:
        NC = len(set(j))
        Result3.append(NC)
    return Result3

# ใช้งาน 14
def Find_Edges_between_C(Start):  # หาโหนดที่อยู่ระหว่างครัสเตอร์ (Dic_Cluster_RestNodes)
    Result = {}  # คือ Dict ของครัสเตอร์ที่ต่อโหนดที่เหลือแล้ว
    Start  # Dic_Cluster_RestNodes
    p = int(0)
    Edges_inter = {}
    for h in Start.values():  # values ก้อนที่ 0
        count = (len(Start)) - 1
        p += 1
        for j in range(count):
            if j == 0:
                Start_CL = set(h)  # ก้อนแรก
            Next_CL = set(Start[j+1])  # ก้อนสอง
            a = Start_CL & Next_CL
            b = len(a)
            Result[j] = b
        c = Result.values()
        c = sum(c)
        Edges_inter[p] = c

    return Edges_inter

# ใช้งาน 17
def EdegsInCluster(Cluster_G):  # จำนวนกิ่งในแต่ละก้อน เฉพาะครัสเตอร์ list 1 หน่วย
    # M_CV
    G = nx.Graph()
    p = int(0)
    G.add_cycle(Cluster_G)  # ทำให้ก้อนแรกเป็นกราฟ
    L_C1 = float(len(G.edges))  # จำนวนกิ่งในกราฟ
    # print'กิ่งในแต่ละก้อนครัสเตอร์ =', L_C1
    p += 1
    M_CV = L_C1
    # M_CV[p] = L_C1
    # draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
    # plt.savefig('Snowball2_Test1')
    # plt.figure(1)
    plt.show()
    G.clear()
    return M_CV  # จำนวนกิ่งในครัสเตอร์แต่ละครัสเตอร์

# ใช้งาน 8
def Shortinterintra(Cluster):  # รับแบบเป็นกราฟ list +++ เฉพาะไซเคิล
    G = nx.Graph()
    G.add_cycle(Cluster)
    Dif_Den_N2 = 0.0
    Dif_Den_N1 = 0.0
    Re_inter4 = 0.0
    Re_inter5 = 0.0
    Re_intra5 = 0.0
    Re_intra4 = 0.0
    Dif_Den = 0.00
    Number_of_Edges_Out1 = 1.00
    Number_of_Edes_All1 = float(len(G.edges(Cluster)))
    N1 = float(len(G.nodes(Cluster))) + 1.0
    N_C1 = float(len(G.nodes(Cluster))) + 1.0
    if (N_C1 * (N1 - N_C1)) == 0.0:
        inter5 = 0.0
        Re_inter5 = inter5
    elif Number_of_Edges_Out1 <= 0.0:
        inter5 = 0.0
        Re_inter5 = inter5
    else:
        inter_1X = ((N_C1 * (N1 - N_C1)))
        inter_2X = (Number_of_Edges_Out1) / inter_1X
        Re_inter5 = round(inter_2X, 2)
    # print 'Re_inter', Re_inter5
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
    # print 'Re_intra', " %+2.2f" % Re_intra5
    Dif_Den = Re_intra5 - Re_inter5
    return Dif_Den


# ใช้งาน 9
def Make_Dic_Cluster(Start, Compare):
    All_Graph = {}
    i = 0
    for h in Compare:
        All_Graph[i] = h
        i += 1
    return All_Graph  # เก็บครัสเตอร์ไว้เป็น Dic 0:[],1:[]

# ใช้งาน 10
def TorRestNodes(Start, Compare):   # inter_C1, Cluster_ALL2
    Result = []
    Start  # กิ่ง
    Compare_Cluster = Compare
    # Dic_Graph = Make_Dic_Cluster(Start, Compare)
    Dic_Graph_R = Make_Dic_Cluster(Start, Compare_Cluster)
    Dic_DD_CL = {}
    # เอากิ่งมาต่อ
    for i in Start:  # แต่ละรอบของกิ่ง
        count = len(Compare_Cluster)
        for h in range(count - 1):  # แต่ละรอบของครัสเตอร์
            if h == 0:  # รอบแรก
                Start_edges = list(i)  # กิ่ง
                Next_CL1 = Dic_Graph_R[h]  # ครัสเตอร์
                # a = Start_edges + Next_CL1  # รวมกันเพื่อเอาไปใช้อะไร list
                # Dic_Graph[h] += Start_edges  # บวกกิ่งเข้าไปที่ i:ก้อนเดิม+Start_edges
                D1 = Shortinterintra(Next_CL1)  # คำนวนค่า interintra
                Dic_DD_CL[D1] = h
            if h > 0:
                Start_edges = list(i)  # กิ่ง
                Next_CL2 = Dic_Graph_R[h]  # ครัสเตอร์ก้อนต่อไป
                # b = Start_edges + Next_CL2  # รวมกันเพื่อเอาไปใช้อะไร list
                # Dic_Graph[h] += Start_edges  # บวกกิ่งเข้าไปที่ i:ก้อนเดิม+Start_edges
                D2 = Shortinterintra(Next_CL2)  # คำนวนค่า interintra
                Dic_DD_CL[D2] = h

        max_value = max(Dic_DD_CL.values())  # ยังไม่ได้ใช้งาน
        sort_value = max(Dic_DD_CL.items())  # หาค่า Max ของครัสเตอร์
        # print'dd'
        p = 0
        # for j in sort_value:
        # print j
        count = len(sort_value)  # ได้ Tuple ของ DD:ตน.ครัสเตอร์
        for l in range(count):
            if l == 1:  # ตน.ครัสเตอร์อยู่รอบที่ l = 1
                f = sort_value[1]  # ให้ f คือตำแหน่งของครัสเตอร์ใน sort_value
                Dic_Graph_R[f] += Start_edges  # เพิ่มกิ่งที่ถูกต้องในครัสเตอร์ตน. f
            else:
                p += 1  # ยังไม่ได้ใช้งาน
        Dic_DD_CL.clear()  # เคลียร์ Dict ที่เก็บค่า DD

    return Dic_Graph_R


def Cal_DiffDen(intra, inter, NC, N, ClusterA2):
    Result4 = {}
    count = len(ClusterA2)
    for i in range(count - 1):
        if i == 0:
            print 'ครัสเตอร์ก้อนที่ =', i
            intra1 = 0.00
            inter1 = 0.00
            NC1 = 0.00
            N1 = 0.00
            inter_R1 = 0.00
            intra_R1 = 0.00
            DD1 = 0.00
            intra1 = intra[i]
            print 'ค่า intra of edges ', i, '=', intra1
            inter1 = float(inter[i])
            # inter1 = float(N[i]) - float(NC[i])
            print 'ค่า inter of edges ', i, '=', inter1
            NC1 = float(NC[i])
            print 'ค่า inside Nodes of cluster ', i, '=', NC1
            N1 = float(N[i]) - float(NC[i])
            print 'ค่า all Nodes of cluster ', i, '=', N1
            # inter cluster density
            inter_1 = NC1 * (N1 - NC1)
            if inter_1 == 0:
                inter_R1 = 0
            else:
                inter_R1 = inter1 / inter_1
            # intra cluster density
            intra_1 = ((NC1 - 1)/2) * NC1
            if intra_1 ==0:
                intra_R1 = 0
            else:
                intra_R1 = intra1 / intra_1
            DD1 = intra_R1 - inter_R1
            Result4[i] = DD1
        if i > 0:
            print 'ครัสเตอร์ก้อนที่ =', i
            intra2 = 0.00
            inter2 = 0.00
            NC2 = 0.00
            N2 = 0.00
            inter_R2 = 0.00
            intra_R2 = 0.00
            DD2 = 0.00
            intra2 = intra[i]
            print 'ค่า intra of edges ', i, '=', intra2
            inter2 = inter[i]
            print 'ค่า inter of edges ', i, '=', inter2
            NC2 = NC[i]
            print 'ค่า inside Nodes of cluster ', i, '=', NC2
            N2 = N[i]
            print 'ค่า all Nodes of cluster ', i, '=', N2
            # inter cluster density
            inter_2 = NC2 * (N2 - NC2)
            if inter_2 == 0:
                inter_R2 = 0
            else:
                inter_R2 = inter2 / inter_2
            # intra cluster density
            intra_2 = ((NC2 - 1) / 2) * NC2
            if intra_2 == 0:
                intra_R2 = 0
            else:
                intra_R2 = intra2 / intra_2
            DD2 = intra_R2 - inter_R2
            Result4[i] = DD2

    return Result4

def pontang(Cluster3, Cluster2):  # (Cluster_ALL3, Cluster_ALL2)
    Result = []
    C = int()
    count = len(Cluster2)
    for i in range(count - 1):
        if i == 0:
            C3 = len(set(Cluster3[i]))  # จาก 114 เหลือ 20
            C2 = len(set(Cluster2[i]))  # จาก 380 เหลือ 49
            C = C2 - C3
            Result.append(C)
        if i > 0:
            C33 = len(set(Cluster3[i]))  #
            C22 = len(set(Cluster2[i]))  #
            C = C22 - C33
            Result.append(C)
    return Result

def Make_LchunkToSchunk(Cluster_ALL, Sub3):
    Result = []
    Result1 = []
    Keep = []
    for i in Cluster_ALL:
        count = len(Sub3)
        for h in range(count):
            Start = i
            if Start == []:
                Next = i
            if h == 0:
                Next = Sub3[h]
            if h > 0:
                Next = Sub3[h]
            a = set(Start) & set(Next)
            if len(a) == 3:
                Result.append(Next)
            else:
                Keep.append(Next)
        Result1.append(Result)
    return Result1

print'------เริ่มทำการหาครัสเตอร์---Snow ball 2---------------'
print'จำนวนโหนดทั้งหมดในกราฟ ', Number_of_nodes, 'โหนด'
print'จำนวน Sub3 ทั้งหมด', len(Sub3), 'โหนด'
Node_Graph = [i for i in G.nodes]  # ก้อนยาวๆ
# print'Node_Graph =', Node_Graph
Edges_Graph = [i for i in G.edges]  # ก้อนสั้นๆ
# print'Edges_Graph =', Edges_Graph

# ได้เป็นก้อนๆครัสเตอร์ list
Cluster_ALL = MakeCluster(Sub3, Sub_cycle3_sort)
# print'หน้าตาครัสเตอร์ =', Cluster_ALL
print'จำนวนครัสเตอร์ภายในกราฟก่อนต่อกิ่ง =', len(Cluster_ALL) - 1
# print'Cluster_ALL =', Cluster_ALL
Cluster_ALL1 = copy.deepcopy(Cluster_ALL)  # Deep Copy


C_G = MeargeCToList(Cluster_ALL1)  # กราฟทุกก้อน [[......],[.....]]
# เช็ค cycle หลงเหลือจาก Sub3 ###ไม่ควรเอาไปต่อเลยนะ เอาไปต่อตอน
T1 = CutSub(C_G, Sub3)  # ได้ก้อนสั้นๆ list[set(['98','63','71'])]
T2 = MeargeCToList(T1)  # ['98','63','71']  ##มาเป็นโหนดเดี่ยวๆได้นะถ้า T1 เหลือ 2 cycles
T3 = RestSub_setTolist(T1)  # ทำเป็น [[],[],[]]
Cluster_ALL3 = copy.deepcopy(Cluster_ALL1)
# A = set(Cluster_ALL3[0])
# print'A', A
# B = set(Cluster_ALL3[1])
# print 'B', B
if len(T1) == 0:
    Cluster_ALL2 = Cluster_ALL1
else:
    Cluster_ALL2 = Cluster_ALL1 + T3  # cycle ที่เหลือเข้าไป

# ทำให้ [[........],[........]] เป็น [(1,2,3),(4,5,6)]
Chunk_Cluster = Make_LchunkToSchunk(Cluster_ALL2, Sub3)

# หาเทอมินอลโหนดมาต่อ เช็คมีโหนดเหมือนกัน 1 โหนดแล้วมาคำนวน inter-intra ในแต่ละก้อน
C_G1 = MeargeCToList(Cluster_ALL2)  # ก้อนยาวๆ + T2

Rest_Edges = CutSub(C_G1, Edges_Graph)  # กิ่งในกราฟที่ไม่เหมือนในครัสเตอร์ทั้งหมด
# print'CC =', Rest_Edges
inter_C1 = Find_terminal(C_G1, Edges_Graph)  # เจอเทอมินอลที่เหมือนกับ set(C_G1)
inter_C2 = Find_termina2(Cluster_ALL, Edges_Graph)  # หาเทอมินอลที่มีโหนดเหมือบกัับแต่ละก้อนครัสเตอร์ [(),(),...]
# print'inter_C', inter_C1 ออกมาเป็น [set(['',''])]
# ทำให้ set(['',''])] เป็น [[],[]]
inter_C11 = RestSub_setTolist(inter_C1)
# print 'inter_C11 =', inter_C11

J = Cluster_ALL[0] + inter_C2
# G.add_cycle(Cluster_ALL[0])
# G.add_edges_from(J)
draw_networkx(G, edge_color='b')
# plt.savefig('Snowball2_Test1')
plt.figure(1)
plt.show()


# ต่อโหนดที่เหลือเข้าครัสเตอร์แบบอาจารย์!!!! {0:['','',''......],1:['','']}
# Check = TorRestNodes1(inter_C1, Cluster_ALL2)
Dic_Cluster_RestNodes = TorRestNodes(inter_C1, Cluster_ALL1)  # ได้ครัสเตอร์ที่ต่อกับโหนดที่เหลือแว้ว
print'จำนวนครัสเตอร์ภายในกราฟกหลังต่อกิ่ง =', len(Dic_Cluster_RestNodes) - 1

# C = set(Cluster_ALL2[0])
# print'C', C
# D = set(Cluster_ALL2[1])
# print 'D', D

# E = A & C
# print 'E', E
# F = B & D
# print 'F', F

# หากิ่งระหว่างครัสเตอร์ {1:20,2:21,3:0}
Dic_Edges_inter_Cluster = Find_Edges_between_C(Dic_Cluster_RestNodes)  # กิ่งภายนอกของแต่ละครัสเตอร์
# print'กิ่งที่อยู่ระหว่างครัสเตอร์ 2 ครัสเตอร์ =', Dic_Edges_inter_Cluster

# ลองหาผลต่างระหว่างยังไม่ต่อกับต่อกิ่ง
pontang_CC = pontang(Cluster_ALL3, Cluster_ALL2)

# ค่าของตัวแปร inter, intra, N ,NC แบบ list
intra_list = Keep_intra(Cluster_ALL)  # list [intra, intra, intra]
N_list = Keep_N(Dic_Cluster_RestNodes)  # [N,N,N]
inter_list = Keep_inter(Dic_Edges_inter_Cluster)
NC_list = Keep_NC(Cluster_ALL)
# print 'ค่า inter of edges =', inter_list
# print 'ค่า intra of edges =', intra_list
# print 'ค่า โหนดในครัสเตอร์แต่ละก้อน =', NC_list
# print 'ค่า โหนดทั้งหมดในครัสเตอร์แต่ละก้อน =', N_list - NC_list

# คำนวน Measure Difference Density
Diff_Density = Cal_DiffDen(intra_list, inter_list, NC_list, N_list, Cluster_ALL2)
print 'ค่า Difference Density ในแต่ละก้อน =', Diff_Density