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
Sub3 = [c for c in nx.cycle_basis(G) if len(c) == 3]


# -------- SUB MAX Degree --------------- #

def D_Max_Degree_Sub(Start):
    # List[['','',''],['','','']]
    L1 = []
    L2 = {}
    K = nx.Graph()
    for h in Start:
        Start_L = h
        K.add_cycle(Start_L)
        # draw_networkx(K, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
        # plt.show()
    for i in Start:
        for u in K.degree(i):
            Degree_Node_i = u[1]
            L1.append(Degree_Node_i)
        Sum_L1 = sum(L1)
        L2[Sum_L1] = i
        L1 = []

    return L2  # Dict[int:List['','','',],['','','',]]


def L_Max_Degree_Sub(Start):
    # Dict{int:List['','','',],['','','',]}
    Result = []
    M_K = max(Start.keys())
    Result = Start[M_K]
    return Result


# --- Deffinition Change Type ---------------------------- #

def Change_SetTolist(Start):  # ทำ set(['','',''],['','','']) เป็น list[[],[]]
    T1 = []
    for i in Start:
        T = list(i)
        T1.append(T)
    return T1


def Change_Shlist_TO_Llist(Sh_list):  # [[],[],[]] -> [[...........]] ก้อนเป็นยาว ๆ
    Result = []
    for i in Sh_list:
        Result += (i)
    return Result


def Plus_ListToLost(Start, Plus):  # [['1','','']] + [['2','','']] = [['1','',''],['2','','']]
    T11 = copy.deepcopy(Start)
    T12 = copy.deepcopy(Plus)
    T1 = []
    T1.append(T11)
    for i in T12:
        if i is not []:
            T1.append(i)
    return T1


def Plus_ListToLost3(Start, Plus):  # Compare_DIFFDENS0, NS21
    T11 = copy.deepcopy(Start)
    T12 = copy.deepcopy(Plus)
    T1 = T11
    # T1.append(T11)
    for i in T12:
        if i is not []:
            T1.append(i)
    return T1

def Plus_ListToLost2(Start, Plus):  # [['1','','']] + [['2','','']] = [['1','',''],['2','','']]
    T11 = copy.deepcopy(Start)
    T12 = copy.deepcopy(Plus)
    T1 = T11
    if T12 == [[]]:
        T12 = []
    for i in T12:
        if i is not []:
            T1.append(i)
    return T1

def Change_ListToSet(Start):  # ทำ List[[],[]] เป็น [set[],set[],set[]]
    T1 = []
    for i in Start:
        T = set(i)
        T1.append(T)
    return T1


def Cut_Sub_3(Start, Compare):  # Start = Sub3ทั้งหมด Compare = ก้อนที่หามา
    # List[['','',''],['','','']]  # List[['','',''],['','','']]
    Result = []
    keep = []
    for h in Start:
        Start_L = h
        if Start_L not in Compare:
            Result.append(Start_L)

    return Result

# เอาไม่เหมือนทั้งหมด หา Sub cycle ของครัสเตอร์ก้อนใหม่
def Cut_Sub_4(Start, Compare, Node):  # (Sub3_L, Compare_DIFFDENS7, Node_Graph)
    # List[['','',''],['','','']]  # List[['','',''],['','','']]
    Result = []
    keep = []
    Compare_Long = Change_Shlist_TO_Llist(Compare)
    Compare_Long_S = set(Compare_Long)
    for h in Start:
        Start_L = h
        Start_S = set(h)
        a = Compare_Long_S & Start_S
        if len(a) == 0:
            Result.append(Start_L)
        else:
            keep.append(Start_L)
    return Result


def draw_Sub(Start):
    # Compare_DIFFDENS0
    Start_L = copy.deepcopy(Start)
    SS = Change_Shlist_TO_Llist(Start_L)
    G = nx.Graph()
    G.add_cycle(SS)
    draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
    plt.show()

# --- Deffinition Change Type ---------------------------- #

def Next_Sub_2n(Start, Compare):  # M_Sub, Sub3_L
    # List['','','']  # List[['','',''],['','','']]
    Result = []
    keep = []
    Start_L = Start
    Start_S = set(Start)
    # Result.append(Start_L)
    for h in Compare:
        Next_L = h
        Next_S = set(h)
        a = Start_S & Next_S
        if len(a) == 2:
            Result.append(Next_L)
    return Result  # List[['','',''],['','','']]


def Node_Sub_Degree(Start, Compare, MDS):
    # L_M_Sub, NS200, Node_Degree
    Result = []
    keep = {}
    Start_L = copy.deepcopy(Start)
    Compare_L = copy.deepcopy(Compare)
    DG = copy.deepcopy(MDS)
    # DG.append(('12',8))
    for h in Compare_L:
        Start_S = set(Start_L)
        Next_S = set(h)
        a = Next_S - Start_S
        for i in DG:
            DG_L = i
            DG_S = set(i)
            b = DG_S & a
            if len(b) == 1:
                keep[DG_L[1]] = i

    Max_Edge = L_Max_Degree_Sub(keep)
    for u in Compare_L:
        Next_LL = u
        Next_SS = set(u)
        Max_Edge_S = set(Max_Edge)
        c = Next_SS & Max_Edge_S
        if len(c) == 1:
            Result.append(Next_LL)
    return Result


def Edges_InsideSub(Start, Compare):
    # Merge_NE0, Edges_Graph
    Result = []
    keep = []
    Start_L = copy.deepcopy(Start)
    Compare_L = copy.deepcopy(Compare)
    Start_Long = Change_Shlist_TO_Llist(Start_L)
    Start_S = set(Start_Long)
    for h in Compare_L:
        Next_T = h
        Next_S = set(h)
        a = Start_S & Next_S
        if len(a) == 2:
            Result.append(Next_T)

    return Result


def Difference_Density(Start2):
    # List[['','',''],['','','']]  # DD
    Result = float()
    keep = []
    # Start_L = Change_Shlist_TO_Llist(Start)
    G = nx.Graph()
    for h in Start2:
        count = len(h)
        for i in range(1):
            G.add_edge(h[i], h[i + 1])
            # draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            # plt.show()

    Number_of_Edges_Out = 0.00  # จำนวนกิ่งภายนอกครัสเตอร์
    Number_of_Edes_All = float(len(G.edges))  # จำนวนกิ่งภายในครัสเตอร์
    print 'จำนวนกิ่งในกราฟ Inside =', Number_of_Edes_All
    N = float(len(G.nodes))  # จำนวนโหนดทั้งหมด
    N_C = float(len(G.nodes))  # จำนวนโหนดภายในครัสเตอร์
    print 'จำนวนโหนดในกราฟ Inside =', N_C

    if (N_C * (N - N_C)) <= 0.00:  # ถ้าส่วนเป็น 0 ให้ inter-edges = 0
        interN4 = 0.00
        Re_inter4 = interN4
    elif Number_of_Edges_Out <= 0.00:  # ถ้าเศษเป็น 0 ให้ inter-edges = 0
        interN4 = 0.00
        Re_inter4 = interN4
    else:  # นอกนั้นคำนวนได้
        inter_1 = ((N_C * (N - N_C)))
        inter_2 = (Number_of_Edges_Out) / inter_1
        Re_inter4 = round(inter_2, 2)  # ให้เหลือทศนิยม 2 ตำแหน่ง
    # intra cluster Density
    if (N_C * (N - 1) / 2) <= 0.00:
        intra4 = 0.00
        Re_intra4 = intra4
    elif Number_of_Edes_All <= 0.00:
        intra4 = 0.00
        Re_intra4 = intra4
    else:
        intra_1 = (N_C * (N - 1.00) / 2.00)
        intra_2 = (Number_of_Edes_All) / (N_C * (N_C - 1) / 2)
        Re_intra4 = round(intra_2, 2)
    Dif_Den_N2 = Re_intra4 - Re_inter4
    Result = Dif_Den_N2
    # print Result

    return Result  # ค่า Difference Density

def Compare_DIFF(Start, Start_M, Start_E, DIFF_DENS0, DD):
    # L_M_Sub, Merge_NE0, Ed_Inside0, DIFF_DENS0, DD
    Result = []
    keep = []
    G = nx.Graph()
    Start0 = copy.deepcopy(Start)
    Start_M0 = copy.deepcopy(Start_M)
    Start_MLong = Change_Shlist_TO_Llist(Start_M0)
    Start_E0 = copy.deepcopy(Start_E)
    if DIFF_DENS0 >= DD:
        for h in Start_E0:
            count = len(h)
            for i in range(1):
                G.add_edge(h[i], h[i + 1])
                # draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                # plt.show()
        Sub_Inside = [c for c in nx.cycle_basis(G) if len(c) == 3]
        # เติม Sub จาก Start_M แบบไม่ซ้ำเดิม
        Sub_Inside1 = copy.deepcopy(Sub_Inside)
        for u in Start_M:
            u1 = set(u)
            Sub_Inside1.append(u)
            for p in Sub_Inside:
                p1 = set(p)
                a = u1 & p1
                if u not in Sub_Inside:
                    if u not in Sub_Inside1:
                        Sub_Inside1.append(u)
                if len(a) == 3:
                    Sub_Inside1.pop(-1)
                    break
                SS = Sub_Inside1
        Result = SS

    else:
        Result = Start0
        print'aa'

    draw_Sub(Result)
    return Result  # List[['','',''],['','','']]


def Next_Sub_2n2(Start, Compare):  # NS2Inside, Sub3_L
    # List[['','',''],['','','']]  # List[['','',''],['','','']]
    Result = []
    keep = []
    Start_L = Start
    Start_Long = Change_Shlist_TO_Llist(Start)
    Start_S = set(Start_Long)
    # Result = Start_L
    for h in Compare:
        Next_L = h
        Next_S = set(h)
        a = Start_S & Next_S
        if len(a) == 2:
            Result.append(Next_L)
    return Result  # List[['','','']


def Node_Sub_Degree2(Start, Compare, MDS):
    # Compare_DIFFDENS0, NS21, Node_Degree
    Result = []
    keep = {}
    Start_L = copy.deepcopy(Start)
    Start_Long = Change_Shlist_TO_Llist(Start_L)
    Compare_L = copy.deepcopy(Compare)
    DG = copy.deepcopy(MDS)
    # DG.append(('12',8))
    for h in Compare_L:
        Start_S = set(Start_Long)
        Next_S = set(h)
        a = Next_S - Start_S
        for i in DG:
            DG_L = i
            DG_S = set(i)
            b = DG_S & a
            if len(b) == 1:
                keep[DG_L[1]] = i

    Max_Edge = L_Max_Degree_Sub(keep)
    for u in Compare_L:
        Next_LL = u
        Next_SS = set(u)
        Max_Edge_S = set(Max_Edge)
        c = Next_SS & Max_Edge_S
        if len(c) == 1:
            Result.append(Next_LL)

    return Result

def Cut_Edges_Cluster(Start, Compare):
    # Compare_DIFFDENS1(SUB), Start_edge1(Edges)
    Result = []
    keep = []
    for h in Compare:
        Compare_S = set(h)
        Start_Long = Change_Shlist_TO_Llist(Start)
        Start_S = set(Start_Long)
        a = Start_S & Compare_S
        if len(a) <= 1:
            Result.append(h)
        else:
            keep.append(h)
    return Result

def Create_Graph_another(Start2):
    Result = []
    G = nx.Graph()
    for h in Start2:
        count = len(h)
        for i in range(1):
            G.add_edge(h[i], h[i + 1])
            # draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            # plt.show()
    Result = [c for c in nx.cycle_basis(G) if len(c) == 3]

    return Result

def Plus_Result(Result):
    Result1 = []
    for k, v in Result.items():
        if k == 1:
            Result1 = v
        if k >= 2:
            for h in v:
                Result1.append(h)

    return Result1

def Make_Cluster(Start_Sub, Start_edge, DD, Start_degree):
    # Sub3_L, Edges_Graph, DD, Node_Degree
    Result = {}
    keep = []
    C = 1
    Start_Sub1 = copy.deepcopy(Start_Sub)
    Start_edge1 = copy.deepcopy(Start_edge)

    A = len(Start_Sub)
    B = DD
    while A >= 0:
        if C >= 2:  #  หา cycle ดีกรีรวมสูงสุดที่โหนดไม่ซ้ำเดิม
            Start_Sub1 = Create_Graph_another(Cut_Edges)  # กราฟที่เหลือ
            if len(Start_Sub2) == 0:
                Start_Sub2 = Start_Sub1
            M_Sub = D_Max_Degree_Sub(Start_Sub2)  # dict
            B = DD
        # หา Sub cycle ที่มีดีกรีรวมสูงสุด
        if C <= 1:
            M_Sub = D_Max_Degree_Sub(Start_Sub1)  # dict
        L_M_Sub = L_Max_Degree_Sub(M_Sub)  # List[]
        print 'SUB เริ่มต้น =', L_M_Sub
        # ถ้าไม่มี Sub cycle เหลืออยู่แล้ว
        if len(L_M_Sub) == 0:
            break
        # หา Sub cycle ที่มีโหนดเหมือนกัน 2 โหนดและโหนดที่เหลือมมีดีกรีโหนดมากที่สุด
        NS20 = Next_Sub_2n(L_M_Sub, Start_Sub1)  # ค้นหา SUB ที่มีโหนดเหมือนกัน 2 โหนด
        # ไม่มี Sub cycle ที่นำมาต่อแล้ว
        if len(NS20) == 0:
            Result[C] = L_M_Sub
            break
        Node_SMD0 = Node_Sub_Degree(L_M_Sub, NS20, Start_degree)  # List[[]]
        print 'Sub ที่เพิ่มขึ้น =', Node_SMD0
        Merge_NE0 = Plus_ListToLost(L_M_Sub, Node_SMD0)  # List[]+[[]]

        # หา กิ่ง ภายในที่มีอยู่ใน Sub ที่รวมกันในข้างต้น
        Ed_Inside0 = Edges_InsideSub(Merge_NE0, Start_edge1)
        # นำทั้งหมดที่ได้มาคำนวนหาค่า Difference Density
        DIFF_DENS0 = Difference_Density(Ed_Inside0)
        print 'DIFF_DENS0 =', DIFF_DENS0
        # นำค่าที่คำนวนได้มาแสดงผล
        Compare_DIFFDENS0 = Compare_DIFF(L_M_Sub, Merge_NE0, Ed_Inside0, DIFF_DENS0, DD)
        print 'Compare_DIFFDENS0 =', Compare_DIFFDENS0
        # ถ้าค่า DIFF_DENS0 น้อยกว่า DD
        if DIFF_DENS0 <= DD:
            Result[C] = Compare_DIFFDENS0
            break
        if C <= 1:
            Cut_SUB0 = Cut_Sub_3(Start_Sub1, Compare_DIFFDENS0)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด
            print 'Cut_SUB0 =', len(Cut_SUB0)
        if C >= 2:
            Cut_SUB0 = Start_Sub1
        # ถ้าไม่มี Sub cycle เหลืออยู่แล้ว
        if len(Cut_SUB0) == 0:
            Result[C] = Compare_DIFFDENS0
            break

        while B >= DD:  # Step 2
            # หา Sub cycle รอบๆ อีกครั้ง
            NS21 = Next_Sub_2n2(Compare_DIFFDENS0, Cut_SUB0)  # เลือก SUB มาต่อ
            # ถ้าไม่มี Sub cycle ข้างเคียงเหลืออยู่แล้ว
            if len(NS21) == 0:
                Result[C] = Compare_DIFFDENS0
                break
            Node_SMD1 = Node_Sub_Degree2(Compare_DIFFDENS0, NS21, Start_degree)  # List[[]]
            print 'Sub ที่เพิ่มขึ้น =', Node_SMD1
            Merge_NE1 = Plus_ListToLost2(Compare_DIFFDENS0, Node_SMD1)  # List[]+[[]]
            # หา กิ่ง ภายใน Sub ทั้งหมด
            Ed_Inside1 = Edges_InsideSub(Merge_NE1, Start_edge1)
            # คำนวนค่า Difference Density
            DIFF_DENS1 = Difference_Density(Ed_Inside1)
            print 'DIFF_DENS0 =', DIFF_DENS1
            B = DIFF_DENS1
            # เปรียบเทียบค่า DD
            Compare_DIFFDENS1 = Compare_DIFF(Compare_DIFFDENS0, Merge_NE1, Ed_Inside1, DIFF_DENS1, DD)
            print 'Compare_DIFFDENS1 =', Compare_DIFFDENS1

            if DIFF_DENS1 >= DD:
                Cut_SUB0 = Start_Sub1  # วน Step 2
                Compare_DIFFDENS0 = Compare_DIFFDENS1

            # ถ้าค่า DIFF_DENS1 น้อยหว่า DD
            else:

                if C < 2:
                    Result[C] = Compare_DIFFDENS1
                    # หา Sub สำหรับการเริ่มต้นครัสเตอร์ set == 0
                    Start_Sub2 = Cut_Sub_4(Start_Sub1, Compare_DIFFDENS1, Node_Graph)
                    # ตัด กิ่งทิ้งด้วย
                    Cut_Edges = Cut_Edges_Cluster(Compare_DIFFDENS1, Start_edge1)
                if C >= 2:  # Edges
                    Result[C] = Compare_DIFFDENS1
                    # Y คือเอาก้อนที่ 1 + 2 เข้าด้วยกัน
                    Y = Plus_Result(Result)
                    # หาจุดเริ่มต้นของก้อนครัสเตอร์ใหม่ ไม่เหมือนทั้งหมด
                    Start_Sub2 = Cut_Sub_4(Start_Sub1, Y)
                    # เอากิ่งมาสร้างกราฟใหม่ ตัดกิ่งที่เหมือนกัน 1 โหนดออก
                    Cut_Edges = Cut_Edges_Cluster(Y, Start_edge1)
                C += 1
                break

    return Result

print'------เริ่มทำการหาครัสเตอร์---Snow ball 2---------------'
print'จำนวนโหนดทั้งหมดในกราฟ ', Number_of_nodes, 'โหนด'
print'จำนวน Sub3 ทั้งหมด', len(Sub3), 'โหนด'
Node_Graph = [i for i in G.nodes]  # ก้อนยาวๆ
# print'Node_Graph =', Node_Graph
Edges_Graph = [i for i in G.edges]  # ก้อนสั้นๆ
# print'Edges_Graph =', Edges_Graph
DD = float(0.60)

# --------------------------------------------------------#
# หา cycles ข้างเคียงที่มีโหนดเหมือนกันจำนวน 2 โหนด Sub3=list[['23','8','30']]
# ทำให้เป็น List จะได้ง่าย
Sub3_L = Change_SetTolist(Sub3)
Sub3_L_sort = sorted(Sub3_L)

C1 = Make_Cluster(Sub3_L, Edges_Graph, DD, Node_Degree)

# M_Sub = D_Max_Degree_Sub(Sub3_L)  # dict
# L_M_Sub = L_Max_Degree_Sub(M_Sub)  # List[]

# NS20 = Next_Sub_2n(L_M_Sub, Sub3_L)  # ค้นหา SUB ที่มีโหนดเหมือนกัน 2 โหนด
# NS200 = Cut_Sub_3(NS20, L_M_Sub)  # ตัด SUB MaxD ออกจาก NS20
# Node_SMD0 = Node_Sub_Degree(L_M_Sub, NS20, Node_Degree)  # List[[]]
# print 'Sub ที่เพิ่มขึ้น =', Node_SMD0
# Merge_NE0 = Plus_ListToLost(L_M_Sub, Node_SMD0)  # List[]+[[]]
# Ed_Inside0 = Edges_InsideSub(Merge_NE0, Edges_Graph)
# DIFF_DENS0 = Difference_Density(Ed_Inside0)
# print 'DIFF_DENS0 =', DIFF_DENS0
# Compare_DIFFDENS0 = Compare_DIFF(L_M_Sub, Merge_NE0, Ed_Inside0, DIFF_DENS0, DD)
# print 'Compare_DIFFDENS0 =', Compare_DIFFDENS0
# Cut_SUB0 = Cut_Sub_3(Sub3_L, Compare_DIFFDENS0)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด
# print 'Cut_SUB0 =', len(Cut_SUB0)

# NS21 = Next_Sub_2n2(Compare_DIFFDENS0, Cut_SUB0)  # เลือก SUB มาต่อ
# Node_SMD1 = Node_Sub_Degree2(Compare_DIFFDENS0, NS21, Node_Degree)  # List[[]]
# print 'Sub ที่เพิ่มขึ้น =', Node_SMD1
# Merge_NE1 = Plus_ListToLost2(Compare_DIFFDENS0, Node_SMD1)  # List[]+[[]]
# Ed_Inside1 = Edges_InsideSub(Merge_NE1, Edges_Graph)
# DIFF_DENS1 = Difference_Density(Ed_Inside1)
# print 'DIFF_DENS1 =', DIFF_DENS1
# Compare_DIFFDENS1 = Compare_DIFF(Compare_DIFFDENS0, Merge_NE1, Ed_Inside1, DIFF_DENS1, DD)
# print 'Compare_DIFFDENS0 =', Compare_DIFFDENS1


# NS22 = Next_Sub_2n2(Compare_DIFFDENS1, Sub3_L)  # เลือก SUB มาต่อ
# Node_SMD2 = Node_Sub_Degree2(Compare_DIFFDENS1, NS22, Node_Degree)  # List[[]]
# print 'Sub ที่เพิ่มขึ้น =', Node_SMD2
# Merge_NE2 = Plus_ListToLost2(Compare_DIFFDENS1, Node_SMD2)  # List[]+[[]]
# Ed_Inside2 = Edges_InsideSub(Merge_NE2, Edges_Graph)
# DIFF_DENS2 = Difference_Density(Ed_Inside2)
# print 'DIFF_DENS2 =', DIFF_DENS2
# Compare_DIFFDENS2 = Compare_DIFF(Compare_DIFFDENS1, Merge_NE2, Ed_Inside2, DIFF_DENS2, DD)
# print 'Compare_DIFFDENS2 =', Compare_DIFFDENS2

# NS23 = Next_Sub_2n2(Compare_DIFFDENS2, Sub3_L)  # เลือก SUB มาต่อ
# Node_SMD3 = Node_Sub_Degree2(Compare_DIFFDENS2, NS23, Node_Degree)  # List[[]]
# print 'Sub ที่เพิ่มขึ้น =', Node_SMD3
# Merge_NE3 = Plus_ListToLost2(Compare_DIFFDENS2, Node_SMD3)  # List[]+[[]]
# Ed_Inside3 = Edges_InsideSub(Merge_NE3, Edges_Graph)
# DIFF_DENS3 = Difference_Density(Ed_Inside3)
# print 'DIFF_DENS3 =', DIFF_DENS3
# Compare_DIFFDENS3 = Compare_DIFF(Compare_DIFFDENS2, Merge_NE3, Ed_Inside3, DIFF_DENS3, DD)
# print 'Compare_DIFFDENS3 =', Compare_DIFFDENS3

# NS24 = Next_Sub_2n2(Compare_DIFFDENS3, Sub3_L)  # เลือก SUB มาต่อ
# Node_SMD4 = Node_Sub_Degree2(Compare_DIFFDENS3, NS24, Node_Degree)  # List[[]]
# print 'Sub ที่เพิ่มขึ้น =', Node_SMD4
# Merge_NE4 = Plus_ListToLost2(Compare_DIFFDENS3, Node_SMD4)  # List[]+[[]]
# Ed_Inside4 = Edges_InsideSub(Merge_NE4, Edges_Graph)
# DIFF_DENS4 = Difference_Density(Ed_Inside4)
# print 'DIFF_DENS4 =', DIFF_DENS4
# Compare_DIFFDENS4 = Compare_DIFF(Compare_DIFFDENS3, Merge_NE4, Ed_Inside4, DIFF_DENS4, DD)
# print 'Compare_DIFFDENS4 =', Compare_DIFFDENS4

# NS25 = Next_Sub_2n2(Compare_DIFFDENS4, Sub3_L)  # เลือก SUB มาต่อ
# Node_SMD5 = Node_Sub_Degree2(Compare_DIFFDENS4, NS25, Node_Degree)  # List[[]]
# print 'Sub ที่เพิ่มขึ้น =', Node_SMD5
# Merge_NE5 = Plus_ListToLost2(Compare_DIFFDENS4, Node_SMD5)  # List[]+[[]]
# Ed_Inside5 = Edges_InsideSub(Merge_NE5, Edges_Graph)
# DIFF_DENS5 = Difference_Density(Ed_Inside5)
# print 'DIFF_DENS5 =', DIFF_DENS5
# Compare_DIFFDENS5 = Compare_DIFF(Compare_DIFFDENS4, Merge_NE5, Ed_Inside5, DIFF_DENS5, DD)
# print 'Compare_DIFFDENS5 =', Compare_DIFFDENS5

# NS26 = Next_Sub_2n2(Compare_DIFFDENS5, Sub3_L)  # เลือก SUB มาต่อ
# Node_SMD6 = Node_Sub_Degree2(Compare_DIFFDENS5, NS26, Node_Degree)  # List[[]]
# print 'Sub ที่เพิ่มขึ้น =', Node_SMD6
# Merge_NE6 = Plus_ListToLost2(Compare_DIFFDENS5, Node_SMD6)  # List[]+[[]]
# Ed_Inside6 = Edges_InsideSub(Merge_NE6, Edges_Graph)
# DIFF_DENS6 = Difference_Density(Ed_Inside6)
# print 'DIFF_DENS6 =', DIFF_DENS6
# Compare_DIFFDENS6 = Compare_DIFF(Compare_DIFFDENS5, Merge_NE6, Ed_Inside6, DIFF_DENS6, DD)
# print 'Compare_DIFFDENS6 =', Compare_DIFFDENS6

# NS27 = Next_Sub_2n2(Compare_DIFFDENS6, Sub3_L)  # เลือก SUB มาต่อ
# Node_SMD7 = Node_Sub_Degree2(Compare_DIFFDENS6, NS27, Node_Degree)  # List[[]]
# print 'Sub ที่เพิ่มขึ้น =', Node_SMD7
# Merge_NE7 = Plus_ListToLost2(Compare_DIFFDENS6, Node_SMD7)  # List[]+[[]]
# Ed_Inside7 = Edges_InsideSub(Merge_NE7, Edges_Graph)
# DIFF_DENS7 = Difference_Density(Ed_Inside7)
# print 'DIFF_DENS7 =', DIFF_DENS7
# Compare_DIFFDENS7 = Compare_DIFF(Compare_DIFFDENS6, Merge_NE7, Ed_Inside7, DIFF_DENS7, DD)
# print 'Compare_DIFFDENS7 =', Compare_DIFFDENS7
# Cut_SUB1 = Cut_Sub_4(Sub3_L, Compare_DIFFDENS7)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด

print 'a'