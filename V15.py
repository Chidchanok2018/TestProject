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


# --- Deffinition Section--- #

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


def Next_Sub_Inside(Start, Compare, DD):  # NS20, Sub3_L, DD
    # List[['','',''],['','','']]  # List[['','',''],['','','']]
    Result = []
    keep = []
    Start_L = Start
    Start_Long = Change_Shlist_TO_Llist(Start)
    Start_S = set(Start_Long)
    for h in Compare:
        Next_L = h
        Next_S = set(h)
        # b = len(Start_S) - 1
        a = Start_S & Next_S
        if len(a) == 3:
            if Next_L not in Start_L:
                Result.append(Next_L)
            else:
                keep.append(Next_L)
    if Result == []:
        Result = [[]]
    return Result  # List[['','',''],['','','']]


def Difference_Density(Start, DD):
    # List[['','',''],['','','']]  # DD
    Result = float()
    keep = []
    Start_L = Change_Shlist_TO_Llist(Start)
    G = nx.Graph()
    G.add_cycle(Start_L)
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


def Compare_DIFF(Merge_Sub, Next_Sub, Edge_Insiide, DIFF_DENS, DD):
    # Merge_NE01, L_M_Sub, NS20, NS2Inside0, DIFF_DENS0
    Result = []
    keep = []
    Start = copy.deepcopy(Merge_Sub)
    Start_Long = Change_Shlist_TO_Llist(Start)
    SOLO_N = Next_Sub
    SOLO_E = Edge_Insiide
    G = nx.Graph()
    if DIFF_DENS >= DD:
        Result = Merge_Sub
        G.add_cycle(Start_Long)
        draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
        plt.show()

    else:
        print ' Difference Density < ', DD
        # กิ่ง
        count = len(SOLO_E)
        for i in range(count):
            if count > 0:
                Start.pop(-1)
        # SUB
        count1 = len(SOLO_N)
        for h in range(count1):
            if count1 > 0:
                Start.pop(-1)
            Result = Start
            Result1 = Change_Shlist_TO_Llist(Result)
            G.add_cycle(Result1)
            draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            plt.show()
    # print 'Compare_DIFFDENS = ', Result
    return Result  # List[['','',''],['','','']]


def Cut_Sub_3(Start, Compare):  # Start = Sub3ทั้งหมด Compare = ก้อนที่หามา
    # List[['','',''],['','','']]  # List[['','',''],['','','']]
    Result = []
    keep = []
    for h in Start:
        Start_L = h
        if Start_L not in Compare:
            Result.append(Start_L)

    return Result


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



def Merge_SubToCluster(Sub3_L, DD):
    Result = []
    Cluster = {}
    Start_SUB = copy.deepcopy(Sub3_L)
    Num_Sub = len(Start_SUB)
    h = 0
    while Num_Sub >= 0:
        h += 1
        if h > 1:
            Start_SUB = Cut_Sub_3(Start_SUB, Compare_DIFFDENS0)
            Start_SUB = Cut_Sub_3(Start_SUB, L_M_Sub)
        M_Sub = D_Max_Degree_Sub(Start_SUB)  # dict
        L_M_Sub = L_Max_Degree_Sub(M_Sub)  # List
        print 'Max_Degree_SUB =', L_M_Sub
        # ------------------ สำหรับเริ่มต้นการหา
        NS20 = Next_Sub_2n(L_M_Sub, Start_SUB)  # ค้นหา SUB ที่มี 2n,1e
        Merge_NE0 = Plus_ListToLost(L_M_Sub, NS20)  # นำ SUB ทั้ง 2 มารวมกัน
        NS2Inside0 = Next_Sub_Inside(Merge_NE0, Start_SUB, DD)
        Merge_NE01 = Plus_ListToLost2(Merge_NE0, NS2Inside0)
        DIFF_DENS0 = Difference_Density(Merge_NE01, DD)
        print 'DIFF_DENS0 =', DIFF_DENS0
        Compare_DIFFDENS0 = Compare_DIFF(Merge_NE01, NS20, NS2Inside0, DIFF_DENS0, DD)
        print 'Compare_DIFFDENS0 = ', Compare_DIFFDENS0
        Cut_SUB0 = Cut_Sub_3(Start_SUB, Compare_DIFFDENS0)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด
        Num_Sub = len(Cut_SUB0)
        # ----------------- เริ่มต้นการหารอบที่ 2
        e = 1
        while e >= DD:
            NS21 = Next_Sub_2n2(Compare_DIFFDENS0, Cut_SUB0)  # เลือก SUB มาต่อ
            Merge_NE1 = Plus_ListToLost2(Compare_DIFFDENS0, NS21)  # SUB เดิม + SUB มาต่อ
            NS2Inside1 = Next_Sub_Inside(Merge_NE1, Cut_SUB0, DD)  # หา กิ่ง ภายในของทั้งก้อน
            Merge_NE11 = Plus_ListToLost2(Merge_NE1, NS2Inside1)  # ก้อน SUB + กิ่ง ภายใน
            DIFF_DENS1 = Difference_Density(Merge_NE11, DD)  # คำนวน DD
            print 'DIFF_DENS1 =', DIFF_DENS1
            Compare_DIFFDENS1 = Compare_DIFF(Merge_NE11, NS21, NS2Inside1, DIFF_DENS1, DD)  # ผ่านเกณฑ์หรือไม่
            print 'Compare_DIFFDENS1 = ', Compare_DIFFDENS1
            Cut_SUB0 = Cut_Sub_3(Start_SUB, Compare_DIFFDENS0)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด
            print 'Cut_SUB0 =', len(Cut_SUB0)

            if DIFF_DENS1 >= DD:  # ------- กรณีค่า DIFF_DENS1 น้อยกว่าค่า DD
                e = DIFF_DENS1
                Compare_DIFFDENS0 = Compare_DIFFDENS1
            else:
                e = DIFF_DENS1
                Cluster[h] = Compare_DIFFDENS1
                Compare_DIFFDENS0 = Compare_DIFFDENS1
                # break  # ออกไปยัง While Num_Sub > 0
            if len(Cut_SUB0) >= 0:  # ------- กรณีจำนวน SUB หมด
                Num_Sub = len(Cut_SUB0)
            else:
                Cluster[h] = Compare_DIFFDENS1
                Cut_SUB0
                break  # ออกไปยัง While Num_Sub > 0
    return Cluster

print'------เริ่มทำการหาครัสเตอร์---Snow ball 2---------------'
print'จำนวนโหนดทั้งหมดในกราฟ ', Number_of_nodes, 'โหนด'
print'จำนวน Sub3 ทั้งหมด', len(Sub3), 'โหนด'
Node_Graph = [i for i in G.nodes]  # ก้อนยาวๆ
# print'Node_Graph =', Node_Graph
Edges_Graph = [i for i in G.edges]  # ก้อนสั้นๆ
# print'Edges_Graph =', Edges_Graph
DD = float(0.50)

# --------------------------------------------------------#
# หา cycles ข้างเคียงที่มีโหนดเหมือนกันจำนวน 2 โหนด Sub3=list[['23','8','30']]
# ทำให้เป็น List จะได้ง่าย
Sub3_L = Change_SetTolist(Sub3)
Sub3_L_sort = sorted(Sub3_L)

# ---------------------------------------------- #

M1 = Merge_SubToCluster(Sub3_L, DD)

# M_Sub = D_Max_Degree_Sub(Sub3_L)  # dict
# L_M_Sub = L_Max_Degree_Sub(M_Sub)  # List

# NS20 = Next_Sub_2n(L_M_Sub, Sub3_L)  # รับ 1 SUB
# Merge_NE0 = Plus_ListToLost(L_M_Sub, NS20)
# NS2Inside0 = Next_Sub_Inside(Merge_NE0, Sub3_L, DD)
# Merge_NE01 = Plus_ListToLost2(Merge_NE0, NS2Inside0)
# DIFF_DENS0 = Difference_Density(Merge_NE01, DD)
# Compare_DIFFDENS0 = Compare_DIFF(Merge_NE01, NS20, NS2Inside0, DIFF_DENS0, DD)
# Cut_SUB0 = Cut_Sub_3(Sub3_L, Compare_DIFFDENS0)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด

# NS21 = Next_Sub_2n2(Compare_DIFFDENS0, Cut_SUB0)  # เลือก SUB มาต่อ
# Merge_NE1 = Plus_ListToLost2(Compare_DIFFDENS0, NS21)
# NS2Inside1 = Next_Sub_Inside(Merge_NE1, Cut_SUB0, DD)
# Merge_NE11 = Plus_ListToLost2(Merge_NE1, NS2Inside1)
# DIFF_DENS1 = Difference_Density(Merge_NE11, DD)
# Compare_DIFFDENS1 = Compare_DIFF(Merge_NE11, NS21, NS2Inside1, DIFF_DENS1, DD)
# Cut_SUB1 = Cut_Sub_3(Sub3_L, Compare_DIFFDENS1)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด

# NS22 = Next_Sub_2n2(Compare_DIFFDENS1, Cut_SUB1)  # เลือก SUB มาต่อ
# Merge_NE2 = Plus_ListToLost2(Compare_DIFFDENS1, NS22)
# NS2Inside2 = Next_Sub_Inside(Merge_NE2, Cut_SUB1, DD)
# Merge_NE21 = Plus_ListToLost2(Merge_NE2, NS2Inside2)
# DIFF_DENS2 = Difference_Density(Merge_NE21, DD)
# Compare_DIFFDENS2 = Compare_DIFF(Merge_NE21, NS22, NS2Inside2, DIFF_DENS2, DD)
# Cut_SUB2 = Cut_Sub_3(Sub3_L, Compare_DIFFDENS2)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด

# NS23 = Next_Sub_2n2(Compare_DIFFDENS2, Cut_SUB2)  # เลือก SUB มาต่อ
# Merge_NE3 = Plus_ListToLost2(Compare_DIFFDENS2, NS23)
# NS2Inside3 = Next_Sub_Inside(Merge_NE3, Cut_SUB2, DD)
# Merge_NE31 = Plus_ListToLost2(Merge_NE3, NS2Inside3)
# DIFF_DENS3 = Difference_Density(Merge_NE31, DD)
# Compare_DIFFDENS3 = Compare_DIFF(Merge_NE31, NS23, NS2Inside3, DIFF_DENS3, DD)
# Cut_SUB3 = Cut_Sub_3(Sub3_L, Compare_DIFFDENS3)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด

# NS24 = Next_Sub_2n2(Compare_DIFFDENS3, Cut_SUB3)  # เลือก SUB มาต่อ
# Merge_NE4 = Plus_ListToLost2(Compare_DIFFDENS3, NS24)
# NS2Inside4 = Next_Sub_Inside(Merge_NE4, Cut_SUB3, DD)
# Merge_NE41 = Plus_ListToLost2(Merge_NE4, NS2Inside4)
# DIFF_DENS4 = Difference_Density(Merge_NE41, DD)
# Compare_DIFFDENS4 = Compare_DIFF(Merge_NE41, NS24, NS2Inside4, DIFF_DENS4, DD)
# Cut_SUB4 = Cut_Sub_3(Sub3_L, Compare_DIFFDENS4)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด

print 'a'
