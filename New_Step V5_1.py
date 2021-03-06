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
print'Len of Sub3', len(Sub3), 'Cycles'  # พิมพ์จำนวน cycle3 ในกราฟ
Sub_cycle3_sort = sorted(Sub3)  # เรียง Sub3 ใหม่จากน้อยไปมาก list[['11','80','79']]


# print'Sub_cycle3_MaDeg', Sub_cycle3_sort  # พิมพ์ Sub3

# ------Definition Function-------------#
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


def interintra(Start, Compare):  # Interintra Start & Compare
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

            if Dif_Den_N2 >= 0.80:  # กำหนดคุณภาพของ Dif
                Cluster = a
            else:
                Keep = a
        return Cluster


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


def interintra2(Start, Compare):  # หาค่า interintra แบบเหมือนกัน 2 โหนด
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


def CutSub(Start, Compare):  # เอา Start ที่ต่างกับ Compare
    # Start ใส่ list[.,.,.], Next ใส่ list[set([],[])]
    for o in Compare:  # แต่ละตัวใน Compare (ตัวตั้งต้น)
        Scycle_same2 = []  # เป็น list ว่าง
        Keep = []  # ใส่ที่เหลือไว้เช็ค
        count = len(Compare) - 1  # นับจำนวนแต่ละตัวใน Compare
        for o1 in range(count):  # หมนุนรอบ Compare
            # print'-----------inter-intra----------------'
            # print'Round =', o1
            Start_Sub = set(Start)  # เอา Set
            Next_Sub = set(Compare[o1 + 1])  # เอา set
            # ลบออก เหมือนไม่เอา
            a = Start_Sub & Next_Sub  # มีอะไรต่างกัน
            if a == set([]):  # เอาที่ต่างกัน
                Scycle_same2.append(Next_Sub)
            else:
                Keep.append(Next_Sub)
        return Scycle_same2


def MergeSubToCluster1(Sub, Sub_sort):  # ตั้งต้นการหาครัสเตอร์1 โหนด 2
    Cluster = []
    Keep = []
    count = len(Sub) - 1
    for h in range(1):
        # หา Sub ที่มีโหนดรอบๆ 2 โหนด
        N2_R0 = Next_SubN2(Sub, Sub_sort)
        if len(N2_R0) == 0:
            Cluster.append(N2_R0)
        if len(N2_R0) > 0:
            N2_Sort = sorted(N2_R0)  # Sorted Sub 2
            # คำนวน interintra จาก Sub ที่หามา
            N2_inter_R0 = interintra(N2_R0, N2_Sort)  # Cal inter Sub 2
            if N2_inter_R0 is None:
                print'None'
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
                    #print 'โหนดที่ใช้ไป', len(N2N1_R1)
                    if len(N2N1_R1) < 1:  # ไม่มีซับเหลือแล้ว
                        Cluster = Cluster + N2_inter_R0
                    if len(N2N1_R1) == 1:  # ไม่มีซับเหลือแล้ว
                        Cluster = Cluster + N2_inter_R0
                    # คำนวน interintra กับ Sub ที่หามา
                    if len(N2_R0) >= 1:  # มี Sub ให้เอาไปคำนวนต่อ
                        N2_inter_R1 = interintra2(N2_inter_R0, N2N1_R1)  # คำนวน interintra
                        # print 'N2_inter_R1', N2_inter_R1
                        if N2_inter_R1 is None:  # Sub ไม่ผ่าน interintra
                            print 'None'
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


def FindNodesBetweenCluster(ClusterS, ClusterS1, ClusterS2, ClusterS3, ClusterS4, ClusterS5):
    G = nx.Graph()
    ClusterA = ClusterS
    G.add_cycle(ClusterA)  # กราฟรวมกันมีกิ่งเชื่อมกัน
    G.add_cycle(ClusterS1)
    G.add_cycle(ClusterS2)
    G.add_cycle(ClusterS3)
    G.add_cycle(ClusterS4)
    G.add_cycle(ClusterS5)

    draw_networkx(G, edge_color='b')
    plt.savefig('Snowball2_Test1')
    plt.figure(1)
    plt.show()
    return ClusterA


print'------เริ่มทำการหาครัสเตอร์---Snow ball 2---------------'
print'จำนวนโหนดทั้งหมดในกราฟ ', Number_of_nodes, 'โหนด'
print'จำนวน Sub3 ทั้งหมด', len(Sub3), 'โหนด'
N2_inter_R0 = MergeSubToCluster1(Sub3, Sub_cycle3_sort)  # รวมขั้นตอนเป็น 1 Cluster ยาวๆ
#print 'N2_inter_R0 =', N2_inter_R0

# ---------Round 2---------
Rest_S3N2_R0 = CutSub(N2_inter_R0, Sub3)  # ตัด cluster 1 ออกจาก sub3
print'Sub ที่เหลือจากการใช้ครั้ง 2 =', len(Rest_S3N2_R0), 'Cycles'
Rest_S3N2_R0_Sorted = sorted(Rest_S3N2_R0)
N2_inter_R1 = MergeSubToCluster1(Rest_S3N2_R0, Rest_S3N2_R0_Sorted)  # รวมขั้นตอนเป็น 1 Cluster ยาวๆ
#print'N2_inter_R1 =', N2_inter_R1

# ---------Round 3---------
# -----ต้องบวกอันที่ 2 เข้ามาด้วยให้เป็นก้อน
N2_inter_R1S = N2_inter_R0 + N2_inter_R1
Rest_S3N2_R1 = CutSub(N2_inter_R1S, Sub3)  # ตัด cluster 1 ออกจาก sub3
print'Sub ที่เหลือจากการใช้ครั้ง 3 =', len(Rest_S3N2_R1), 'Cycles'
Rest_S3N2_R1_Sorted = sorted(Rest_S3N2_R1)
N2_inter_R2 = MergeSubToCluster1(Rest_S3N2_R1, Rest_S3N2_R1_Sorted)  # รวมขั้นตอนเป็น 1 Cluster ยาวๆ
#print'N2_inter_R2 =', N2_inter_R2

# ---------Round 4---------
# -----ต้องบวกอันก้อนหน้าทั้งหมดมาด้วย
N2_inter_R2S = N2_inter_R0 + N2_inter_R1 + N2_inter_R2
Rest_S3N2_R2 = CutSub(N2_inter_R2S, Sub3)  # ตัด cluster 1 ออกจาก sub3
print'Sub ที่เหลือจากการใช้ครั้ง 4 =', len(Rest_S3N2_R2), 'Cycles'
Rest_S3N2_R2_Sorted = sorted(Rest_S3N2_R2)
N2_inter_R3 = MergeSubToCluster1(Rest_S3N2_R2, Rest_S3N2_R2_Sorted)  # รวมขั้นตอนเป็น 1 Cluster ยาวๆ
#print'N2_inter_R3 =', N2_inter_R3

# ---------Round 4---------
# -----ต้องบวกอันก้อนหน้าทั้งหมดมาด้วย
N2_inter_R3S = N2_inter_R0 + N2_inter_R1 + N2_inter_R2 + N2_inter_R3
# แล้วตัดออกจากก้อน Sub ทั้งหมด
Rest_S3N2_R3 = CutSub(N2_inter_R3S, Sub3)  # ตัด cluster 1 ออกจาก sub3
# เหลือเท่าไร
print'Sub ที่เหลือจากการใช้ครั้ง 5 =', len(Rest_S3N2_R3), 'Cycles'
# จัดเรียงใหม่ตัวแปรจะได้ไม่ซ้ำ
Rest_S3N2_R3_Sorted = sorted(Rest_S3N2_R3)
# เข้ากระบวนการทำให้เป็นครัสเตอร์
N2_inter_R4 = MergeSubToCluster1(Rest_S3N2_R3, Rest_S3N2_R3_Sorted)  # รวมขั้นตอนเป็น 1 Cluster ยาวๆ
# ออกมาเป็นก้อนครัสเตอร์
# print'N2_inter_R4 =', N2_inter_R4

# ---------Round 5---------
# -----ต้องบวกอันก้อนหน้าทั้งหมดมาด้วย
N2_inter_R4S = N2_inter_R0 + N2_inter_R1 + N2_inter_R2 + N2_inter_R3 + N2_inter_R4
# print'Count', len(set(N2_inter_R4S))
# แล้วตัดออกจากก้อน Sub ทั้งหมด
Rest_S3N2_R4 = CutSub(N2_inter_R4S, Sub3)  # ตัด cluster 1 ออกจาก sub3
# เหลือเท่าไร
print'Sub ที่เหลือจากการใช้ครั้ง 6 =', len(Rest_S3N2_R4), 'Cycles'
# จัดเรียงใหม่ตัวแปรจะได้ไม่ซ้ำ
Rest_S3N2_R4_Sorted = sorted(Rest_S3N2_R4)
# เข้ากระบวนการทำให้เป็นครัสเตอร์
N2_inter_R5 = MergeSubToCluster1(Rest_S3N2_R4, Rest_S3N2_R4_Sorted)  # รวมขั้นตอนเป็น 1 Cluster ยาวๆ
#print'N2_inter_R5 =', N2_inter_R5

# ---------Round 6---------
# -----ต้องบวกอันก้อนหน้าทั้งหมดมาด้วย
N2_inter_R5S = N2_inter_R0 + N2_inter_R1 + N2_inter_R2 + N2_inter_R3 + N2_inter_R4 + N2_inter_R5
# print'Count', len(set(N2_inter_R5S))
# แล้วตัดออกจากก้อน Sub ทั้งหมด
Rest_S3N2_R5 = CutSub(N2_inter_R5S, Sub3)  # ตัด cluster 1 ออกจาก sub3
# เหลือเท่าไร
print'Sub ที่เหลือจากการใช้ครั้ง 7 =', len(Rest_S3N2_R5), 'Cycles'
# จัดเรียงใหม่ตัวแปรจะได้ไม่ซ้ำ
Rest_S3N2_R5_Sorted = sorted(Rest_S3N2_R5)
# เข้ากระบวนการทำให้เป็นครัสเตอร์
N2_inter_R6 = MergeSubToCluster1(Rest_S3N2_R5, Rest_S3N2_R5_Sorted)  # รวมขั้นตอนเป็น 1 Cluster ยาวๆ
print'N2_inter_R6 =', N2_inter_R6  # พบ [[]]

# --------Graph-------
# Node_BetweenC = FindNodesBetweenCluster(N2_inter_R0, N2_inter_R1, N2_inter_R2, N2_inter_R3, N2_inter_R4, N2_inter_R5)
G = nx.Graph()
plt.show()
