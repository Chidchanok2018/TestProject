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
#Sub4 = [c for c in nx.cycle_basis(G) if len(c) == 4]  # หา Sub = 4 โหนดในกราฟ List
#print'Len of Sub4', len(Sub4), 'Cycles'  # พิมพ์จำนวน cycle4 ในกราฟ
Sub_cycle3_sort = sorted(Sub3)  #  เรียง Sub3 ใหม่จากน้อยไปมาก
#print'Sub_cycle3_MaDeg', Sub_cycle3_sort  # พิมพ์ Sub3
#Sub_cycle4_MaDeg = sorted(Sub4)  # เรียง Sub4 ใหม่จากน้อยไปมาก

# ------Definition Function-------------#
def Next_SubN2(Start, Compare):  # เอาเหมือนรอบๆ 2 โหนด
    # Start ใส่ list[set([],[])], Next ใส่ list[set([],[])]
    Scycle_same2 = []  # กำหนด type ให้
    Keep = []
    for h in Start:  # แต่ละตัวใน A_Subcycle (ตัวตั้งต้น)
        count = len(Start) - 1  # นับจำนวนแต่ละตัวใน A_Subcycle (ตั้งต้น)
        for i in range(count + 1):  # แต่ละตัวใน A_Subcycle จำนวนรอบเท่ากับ count
            Start_Scycle = set(h)  # ให้ Start_Scycle คือตัวแรกใน Start
            if i == count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = set(Compare[0])  # list
            if i < count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = set(Compare[i + 1])  # เปลี่ยน Next ให้เป็น list
            a = Start_Scycle & Next_Sub  # ให้ a คือตัวที่ แตกต่าง กันของ Start กับ Next
            # b = Start_Scycle - Next_Scycle #เอาที่ไม่เหมือน
            if len(a) == 2.0:  # ถ้า จำนวนของ a มากกว่าเท่ากับ 2
                Merge_Sub = Start_Scycle | Next_Sub  # ให้ Mearge_Sub เท่ากับ Start U Next
                Scycle_same2.append(Next_Sub)  # ให้ เพิ่ม Next ใน Scycle_same2
            else:
                Keep.append(Next_Sub)
        return Scycle_same2  # ส่งค่า Scycle_same2 [set([],[],...)]

def interintra(Start, Compare):  # หาค่า interintra แบบเหมือนกัน 2 โหนด
    # Start ใส่ list[set([],[])], Next ใส่ list[set([],[])]
    for o in Start:  # แต่ละตัวใน Start (ตัวตั้งต้น)
        Cluster = []  # กำหนด type ให้ Cluster [list]
        Keep = []
        count = len(Start) - 1  # นับจำนวนแต่ละตัวใน Start
        for o1 in range(count + 1):  # แต่ละตัวใน Start จำนวนรอบเท่ากับ count
            #print'-----------inter-intra----------------'
            #print'Round =', o1
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
                #print 'inter4', " %+2.2f" % Re_inter4
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
                #print 'Re_intra4', " %+2.2f" % Re_intra4
                Dif_Den_N2 = Re_intra4 - Re_inter4
                #print 'Difference Density =', " %+2.2f" % Dif_Den_N2

            if Dif_Den_N2 >= 0.80:  # กำหนดคุณภาพของ Dif
                Cluster = a
            else:
                Keep = a
        return Cluster

def Next_SubN2N1(Start, Compare): # หา Sub รอบที่ 2 ที่โหนดเหมือน 2
    # Start ใส่ list[.,.,.], Compare หมุนใส่ list[set([],[])]
    Merge = []  # กำหนด type ให้ตัว Return
    Keep = []
    for h in Compare:  # Compare เป็นตัวหมุน
        count = len(Compare) - 1  # จำนวน Start-1
        for i in range(count + 1):  # จำนวนรอบใน count
            #print '-------Next_Scycle---------------'
            #print 'Len Round =', i
            Start_Sub = set(Start)  # ให้ Start เป็น set
            #print'StartScycle', Start_Sub
            if len(Merge) >= 1:
                Start_Sub = Start_Sub | b  # รวมไม่เอาที่ซ้ำ (set)
            if i == count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = set(Compare[0])  # list
            if i < count:  # แก้ปัญหารอบ cycle หาย
                Next_Sub = set(Compare[i + 1])  # เปลี่ยน Next ให้เป็น list
            #print'NextScycle', Next_Sub
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
            #print'-----------inter-intra----------------'
            #print'Round =', o1
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
                #print 'inter4', " %+2.2f" % Re_inter4
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
                #print 'Re_intra4', " %+2.2f" % Re_intra4
                Dif_Den_N2 = Re_intra4 - Re_inter4
                #print 'Difference Density =', " %+2.2f" % Dif_Den_N2

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
                    inter_1X = ((N_C1*(N1-N_C1)))
                    inter_2X = (Number_of_Edges_Out1) / inter_1X
                    Re_inter5 = round(inter_2X, 2)
                #print 'Re_inter', Re_inter5
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
                #print 'Re_intra', " %+2.2f" % Re_intra5
                Dif_Den_N1 = Re_intra5 - Re_inter5
                #print 'Difference Density =', " %+2.2f" % Dif_Den_N1
            Dif_Den = Dif_Den_N2 + Dif_Den_N1
            if Dif_Den >= 0.80:  # กำหนดคุณภาพของ Dif
                Cluster = a
            else:
                Keep = a
        return Cluster

def CutSub(Start, Compare):  # เอา Start ลบออกจาก Compare
    # Start ใส่ list[.,.,.], Next ใส่ list[set([],[])]
    for o in Compare:  # แต่ละตัวใน Compare (ตัวตั้งต้น)
        Scycle_same2 = []  # เป็น list ว่าง
        Keep = []  # ใส่ที่เหลือไว้เช็ค
        count = len(Compare) - 1  # นับจำนวนแต่ละตัวใน Compare
        for o1 in range(count):  # หมนุนรอบ Compare
            #print'-----------inter-intra----------------'
            #print'Round =', o1
            Start_Sub = set(Start)  # เอา Set
            Next_Sub = set(Compare[o1 + 1])  # เอา set
            # ลบออก เหมือนไม่เอา
            a = Start_Sub & Next_Sub  # มีอะไรต่างกัน
            if a == set([]):  # ถ้า a เป็น set([])
                Scycle_same2.append(Next_Sub)
            else:
                Keep.append(Next_Sub)
        return Scycle_same2

 def RoundAddSub(จำนวนSub_ข้างเคียง, จำนวนSub_ทั้งหมด, จำนวนโหนดทั้งหมดในกราฟ ):
    i = จำนวนSub_ข้างเคียง
    a = จำนวนSub_ทั้งหมด
    b = จำนวนโหนดทั้งหมดในกราฟ
    while i >=0:  # ตราบใดที่ i ยังมากกว่าเท่ากับ 0

        i += จำนวนSub_ข้างเคียง  # ให้ i += Sub_ข้างเคียง
    print i

def FindNodesBetweenCluster(ClusterS, ClusterC, ClusterC1, ClusterC2):
    G = nx.Graph()
    ClusterA = ClusterS + ClusterC + ClusterC1 + ClusterC2 # กราฟรวมมีกิ่งเชื่อม
    S_ClusterA = set(ClusterA)  # จำนวนโหนดที่อยู่ใน cluster1
    #G.add_cycle(ClusterS)  # กราฟแยก ClusterS
    #G.add_cycle(ClusterC)  # กราฟแยก ClusterC
    #G.add_cycle(ClusterC1)  # กราฟแยก ClusterC1
    G.add_cycle(ClusterA)  # กราฟรวมกันมีกิ่งเชื่อมกัน
    #a = G.edges(ClusterS)
    #b = G.edges(ClusterC)
    draw_networkx(G, edge_color='b')
    plt.savefig('Test')
    plt.figure(1)
    plt.show()
    return ClusterA


print'------เริ่มทำการหาครัสเตอร์---------------------'
print'จำนวนโหนดทั้งหมดในกราฟ ', Number_of_nodes, 'โหนด'
print'จำนวน Sub3 ทั้งหมด', len(Sub3), 'Cycles'
# -------------- รอบที่ 1 -----------------------
S3N2_R0 = Next_SubN2(Sub3, Sub_cycle3_sort) # หาโหนดใกล้เคียงเหมือนกัน 2 โหนด list[set([],[])]
print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 1 =', len(S3N2_R0), 'Cycles'
S3N2_Sorted = sorted(S3N2_R0)  # จัดเรียงโหนดใกล้เคียงรอบแรก list[set([],[])]
# interintra ต้องการ (list[set([],[])], list[set([],[])])
S3N2_inter_R0 = interintra(S3N2_R0, S3N2_Sorted)  # หาโหนดที่มี DifDen มากกว่าเท่ากับ 0.70 list[.,.,.]
# -------------- รอบที่ 2 -----------------------
# Next_SubN2N1 ต้องการ (list[.,.,.], list[set([],[])])
S3N2_R1 = Next_SubN2N1(S3N2_inter_R0, Sub3)  # หาโหนดใกล้เคียงเหมือนกัน 2 โหนด list[set([],[])]
print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 2 =', len(S3N2_R1), 'Cycles'
# interintra2 ต้องการ (list[.,.,.], list[set([],[])])
S3N2_inter_R1 = interintra2(S3N2_inter_R0, S3N2_R1)  # หาโหนดที่มี DifDen มากกว่าเท่ากับ 0.70 list[.,.,.]
# -------------- รอบที่ 3 -----------------------
# Next_SubN2N1 ต้องการ (list[.,.,.], list[set([],[])])
S3N2_R2 = Next_SubN2N1(S3N2_inter_R1, Sub3)  # หาโหนดใกล้เคียงเหมือนกัน 2 โหนด(2) list[set([],[])]
print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 3 =', len(S3N2_R2), 'Cycles'
# interintra2 ต้องการ (list[.,.,.], list[set([],[])])
S3N2_inter_R2 = interintra2(S3N2_inter_R1, S3N2_R2)  # หาโหนดที่มี DifDen มากกว่าเท่ากับ 0.70 list[.,.,.]
# -------------- รอบที่ 4 -----------------------
# Next_SubN2N1 ต้องการ (list[.,.,.], list[set([],[])])
S3N2_R3 = Next_SubN2N1(S3N2_inter_R2, Sub3)  # หาโหนดใกล้เคียงเหมือนกัน 2 โหนด(3) list[set([],[])]
print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 4 =', len(S3N2_R3), 'Cycles'
# interintra2 ต้องการ (list[.,.,.], list[set([],[])])
S3N2_inter_R3 = interintra2(S3N2_inter_R2, S3N2_R3)  # หาโหนดที่มี DifDen มากกว่าเท่ากับ 0.70 list[.,.,.]

if len(S3N2_R2) or len(S3N2_R3) == 0:  # เมื่อไม่เจอ sub รอบๆแล้ว ให้มาขึ้น Cluster ใหม่
    Cluster1 = S3N2_inter_R2  # list[.,.,.] นับไม่ได้ ไว้สร้างกราฟ
    print'โหนดทั้งหมดที่ใช้ในการหาครั้งแรก =', Cluster1
    print'จำนวนโหนดที่มีในครั้งแรก =', len(S3N2_R0) + len(S3N2_R1) + len(S3N2_R2) + len(S3N2_R3)
    P = len(S3N2_R0) + len(S3N2_R1) + len(S3N2_R2) + len(S3N2_R3)
    Q = Number_of_nodes - P
    print'จำนวนโหนดที่เหลืออยู่ในกราฟ=', Q, 'โหนด'

    print'----เริ่มการหา Sub ข้างเคียงรอบที่ 2---------------'
    # -------------- รอบที่ 1 -----------------------
    Rest_S3N2_R0 = CutSub(S3N2_inter_R2, Sub3)  # หา Sub ที่เหลือจาก Cluster1
    print'Sub ที่เหลือจากการใช้ครั้ง 2 =', len(Rest_S3N2_R0), 'Cycles'
    Rest_S3N2_Sorted = sorted(Rest_S3N2_R0)  # จัดเรียงซับที่เหลือจาก Cluster1
    Rest_S3N2_inter_R0 = interintra(Rest_S3N2_R0, Rest_S3N2_Sorted)  # เอาซับที่เหลือหา interintra
    # -------------- รอบที่ 2 -----------------------
    Rest_S3N2_R1 = Next_SubN2N1(Rest_S3N2_inter_R0, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 2
    print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 1 =', len(Rest_S3N2_R1)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 2
    Rest_S3N2_inter_R1 = interintra2(Rest_S3N2_inter_R0, Rest_S3N2_R1)  # คำนวน รnterintra รอบที่ 2
    # -------------- รอบที่ 3 -----------------------
    Rest_S3N2_R2 = Next_SubN2N1(Rest_S3N2_inter_R1, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 3
    print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 2=', len(Rest_S3N2_R2)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 3
    Rest_S3N2_inter_R2 = interintra2(Rest_S3N2_inter_R1, Rest_S3N2_R2)  # คำนวน รnterintra รอบที่ 3
    # -------------- รอบที่ 4 -----------------------
    Rest_S3N2_R3 = Next_SubN2N1(Rest_S3N2_inter_R2, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 4
    print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 3=', len(Rest_S3N2_R3)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 4
    Rest_S3N2_inter_R3 = interintra2(Rest_S3N2_inter_R2, Rest_S3N2_R3)  # คำนวน รnterintra รอบที่ 4
    # -------------- รอบที่ 5 -----------------------
    Rest_S3N2_R4 = Next_SubN2N1(Rest_S3N2_inter_R3, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 5
    print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 4=', len(Rest_S3N2_R4)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 5
    Rest_S3N2_inter_R4 = interintra2(Rest_S3N2_inter_R3, Rest_S3N2_R4)  # คำนวน รnterintra รอบที่ 5
    # -------------- รอบที่ 6 -----------------------
    Rest_S3N2_R5 = Next_SubN2N1(Rest_S3N2_inter_R4, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 6
    print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 5=', len(Rest_S3N2_R5)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 6
    Rest_S3N2_inter_R5 = interintra2(Rest_S3N2_inter_R4, Rest_S3N2_R5)  # คำนวน รnterintra รอบที่ 6

    if len(Rest_S3N2_R1) or len(Rest_S3N2_R2) or len(Rest_S3N2_R3) or len(Rest_S3N2_R4) or len(Rest_S3N2_R5) == 0:  # เมื่อไม่เจอ sub รอบๆแล้ว ให้มาขึ้น Cluster ใหม่
        Cluster2 = Rest_S3N2_inter_R3  # list[.,.,.] นับไม่ได้ ไว้สร้างกราฟ
        print'โหนดทั้งหมดที่ใช้ในการหาครั้ง 2 =', Cluster2
        P1 = len(Rest_S3N2_R0) + len(Rest_S3N2_R1) + len(Rest_S3N2_R2) + len(Rest_S3N2_R3) + len(Rest_S3N2_R4) + len(
            Rest_S3N2_R5)
        print'จำนวนโหนดที่มีในครั้ง 2 =', P1
        Q1 = Number_of_nodes - P1
        print'จำนวนโหนดที่เหลืออยู่ในกราฟ=', Q1, 'โหนด'

        print'----เริ่มการหา Sub ข้างเคียงรอบที่ 3---------------'
        # -------------- รอบที่ 1 -----------------------
        Rest_S3N2_inter_R3 = Cluster1 + Cluster2
        Rest1_S3N2_R0 = CutSub(Rest_S3N2_inter_R3, Sub3)  # หา Sub ที่เหลือจาก Cluster1
        print'Sub ที่เหลือจากการใช้ครั้ง 3 =', len(Rest1_S3N2_R0), 'Cycles'
        Rest1_S3N2_Sorted = sorted(Rest1_S3N2_R0)  # จัดเรียงซับที่เหลือจาก Cluster1
        Rest1_S3N2_inter_R0 = interintra(Rest1_S3N2_R0, Rest1_S3N2_Sorted)  # เอาซับที่เหลือหา interintra
        # -------------- รอบที่ 2 -----------------------
        Rest1_S3N2_R1 = Next_SubN2N1(Rest1_S3N2_inter_R0, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 2
        print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 1=', len(Rest1_S3N2_R1)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 2
        Rest1_S3N2_inter_R1 = interintra2(Rest1_S3N2_inter_R0, Rest1_S3N2_R1)  # คำนวน รnterintra รอบที่ 2
        # -------------- รอบที่ 3 -----------------------
        Rest1_S3N2_R2 = Next_SubN2N1(Rest1_S3N2_inter_R1, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 3
        print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 2=', len(Rest1_S3N2_R2)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 3
        Rest1_S3N21_inter_R2 = interintra2(Rest1_S3N2_inter_R1, Rest1_S3N2_R2)  # คำนวน รnterintra รอบที่ 3

        if len(Rest1_S3N2_R1) or len(Rest1_S3N2_R2) == 0:  # เมื่อไม่เจอ sub รอบๆแล้ว ให้มาขึ้น Cluster ใหม่
            Cluster3 = Rest1_S3N2_inter_R1  # list[.,.,.] นับไม่ได้ ไว้สร้างกราฟ
            print'โหนดทั้งหมดที่ใช้ในการหาครั้ง 3 =', Cluster3
            P2 = len(Rest1_S3N2_R0) + len(Rest1_S3N2_R1) + len(Rest1_S3N2_R2)
            print'จำนวนโหนดที่มีในครั้ง 2 =', P2
            Q2 = Number_of_nodes - P2
            print'จำนวนโหนดที่เหลืออยู่ในกราฟ', Q2, 'โหนด'

            print'----เริ่มการหา Sub ข้างเคียงรอบที่ 4---------------'
            Rest1_S3N2_inter_R1 = Cluster1 + Cluster2 + Cluster3
            Rest2_S3N2_R0 = CutSub(Rest1_S3N2_inter_R1, Sub3)  # หา Sub ที่เหลือจาก Cluster1
            print'Sub ที่เหลือจากการใช้ครั้ง 4=', len(Rest2_S3N2_R0), 'Cycles'
            Rest2_S3N2_Sorted = sorted(Rest2_S3N2_R0)  # จัดเรียงซับที่เหลือจาก Cluster1
            Rest2_S3N2_inter_R0 = interintra(Rest2_S3N2_R0, Rest2_S3N2_Sorted)  # เอาซับที่เหลือหา interintra
            # -------------- รอบที่ 2 -----------------------
            Rest2_S3N2_R1 = Next_SubN2N1(Rest2_S3N2_inter_R0, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 2
            print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 1=', len(Rest2_S3N2_R1)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 2
            Rest2_S3N2_inter_R1 = interintra2(Rest2_S3N2_inter_R0, Rest2_S3N2_R1)  # คำนวน รnterintra รอบที่ 2
            # -------------- รอบที่ 3 -----------------------
            Rest2_S3N2_R2 = Next_SubN2N1(Rest2_S3N2_inter_R1, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 3
            print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 2=', len(Rest2_S3N2_R2)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 3
            Rest2_S3N21_inter_R2 = interintra2(Rest2_S3N2_inter_R1, Rest2_S3N2_R2)  # คำนวน รnterintra รอบที่ 3

            if len(Rest2_S3N2_R1) or len(Rest2_S3N2_R2) == 0:  # เมื่อไม่เจอ sub รอบๆแล้ว ให้มาขึ้น Cluster ใหม่
                Cluster4 = Rest2_S3N2_inter_R0  # list[.,.,.] นับไม่ได้ ไว้สร้างกราฟ
                print'โหนดทั้งหมดที่ใช้ในการหาครั้ง 4 =', Cluster4
                P3 = len(Rest2_S3N2_R0) + len(Rest2_S3N2_R1) + len(Rest2_S3N2_R2)
                print'จำนวนโหนดที่มีในครั้ง 2 ', P3
                Q3 = Number_of_nodes - P2
                print'จำนวนโหนดที่เหลืออยู่ในกราฟ', Q3, 'โหนด'

                print'----เริ่มการหา Sub ข้างเคียงรอบที่ 5---------------'
                Rest2_S3N2_inter_R1 = Cluster1 + Cluster2 + Cluster3 + Cluster4
                Rest3_S3N2_R0 = CutSub(Rest2_S3N2_inter_R1, Sub3)  # หา Sub ที่เหลือจาก Cluster1
                print'Sub ที่เหลือจากการใช้ครั้ง 5 =', len(Rest3_S3N2_R0), 'Cycles'
                Rest3_S3N2_Sorted = sorted(Rest3_S3N2_R0)  # จัดเรียงซับที่เหลือจาก Cluster1
                Rest3_S3N2_inter_R0 = interintra(Rest3_S3N2_R0, Rest3_S3N2_Sorted)  # เอาซับที่เหลือหา interintra
                # -------------- รอบที่ 2 -----------------------
                Rest3_S3N2_R1 = Next_SubN2N1(Rest3_S3N2_inter_R0, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 2
                print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 1 =', len(Rest2_S3N2_R1)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 2
                Rest3_S3N2_inter_R1 = interintra2(Rest3_S3N2_inter_R0, Rest3_S3N2_R1)  # คำนวน รnterintra รอบที่ 2
                # -------------- รอบที่ 3 -----------------------
                #Rest3_S3N2_R2 = Next_SubN2N1(Rest3_S3N2_inter_R1, Sub3)  # หา Sub ข้างเคียงใหม่อีกครั้ง รอบที่ 3
                #print'Sub จากการหาโหนดเหมือนกัน 2 รอบที่ 2=', len(Rest3_S3N2_R2)  # พิมพ์จำนวน sub ข้างเคียงรอบที่ 3
                #------Error


#--------------Measure of Cluster--------------
# print'---Coverage Matric---'
Cluster1_M = Cluster1
# print'Cluster1_M =', Cluster1_M
Cluster2_M = Cluster2
# print'Cluster2_M =', Cluster2_M
Cluster3_M = Cluster3
Cluster4_M = Cluster4
Node_BetweenC = FindNodesBetweenCluster(Cluster1_M, Cluster2_M, Cluster3_M, Cluster4_M)
# --------------Draw Graph-----------------
G = nx.Graph()
#G.add_cycle(Cluster1)
#nx.draw(G, with_labels=True)
# draw_networkx(G)  #When open will happen multiple graph#
plt.show()