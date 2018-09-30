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
fh = open("C:\Users\Kmutt_Wan\PycharmProjects\Nodes50_500.txt", "rb")
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
def Cut_Sub_4(Start, Compare):  # (Sub3_L, Compare_DIFFDENS7
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
    # draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
    # plt.show()


def Plus_Result(Result):
    Result1 = []
    for k, v in Result.items():
        if k == 1:
            Result1 = v
        if k >= 2:
            for h in v:
                Result1.append(h)

    return Result1


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
            if Next_L not in Result:
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
    # print 'จำนวนกิ่งในกราฟ Inside =', Number_of_Edes_All
    N = float(len(G.nodes))  # จำนวนโหนดทั้งหมด
    N_C = float(len(G.nodes))  # จำนวนโหนดภายในครัสเตอร์
    # print 'จำนวนโหนดในกราฟ Inside =', N_C

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


# เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index
def Cut_Edges_Cluster(Start, Compare):
    # Compare_DIFFDENS1, Start_edge1
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


def Cut_Nodes_Cluster(Start, Compare):
    # Compare_DIFFDENS1, Start_edge1
    Result = []
    keep = []
    for h in Compare:
        Compare_S = set(h)
        Start_Long = Change_Shlist_TO_Llist(Start)
        Start_S = set(Start_Long)
        a = Start_S & Compare_S
        if len(a) == 1:
            a = list(a)
            if a not in Result:
                Result.append(a)
    return Result


def Cut_Edges_Sub_Cluster(Start, Compare):
    # Compare_DIFFDENS1, Start_edge1
    Result = []
    keep = []
    for h in Compare:
        Compare_S = set(h)
        Start_Long = Change_Shlist_TO_Llist(Start)
        Start_S = set(Start_Long)
        a = Start_S & Compare_S
        if len(a) == 0:
            Result.append(h)
    return Result


# สร้างกราฟใหม่จาก กิ่ง ที่ได้จาก Cut_Edges_Cluster
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


def Create_Graph_Edges(Start2):  # Dict
    Result = []
    G = nx.Graph()
    for h in Start2.values():
        count = len(h)
        for u in h:
            u = list(u)
            for i in range(1):
                G.add_edge(u[i], u[i + 1])
                # draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                # plt.show()
    Result = [c for c in nx.cycle_basis(G) if len(c) == 3]
    return Result


def Cut_Start_edges(Compare, Start):  # Start_edge1, Result <= 1
    # List[(),(),....] #Dict []
    Result = []
    keep = []
    Start_L = copy.deepcopy(Start)
    Compare_L = copy.deepcopy(Compare)
    h = 0
    for v in Start_L.values():
        h += 1
        if h == 1:
            for i in Compare_L:
                Next_S = set(i)
                Start_Long = Change_Shlist_TO_Llist(v)
                Start_S = set(Start_Long)
                a = Start_S & Next_S
                if len(a) <= 1:
                    keep.append(i)
        if h >= 2:  # เอากิ่งที่เหลือมาหาก้อนต่อไป
            for u in keep:
                Next_SS = set(u)
                Start_Long1 = Change_Shlist_TO_Llist(v)
                Start_SS = set(Start_Long1)
                if len(v) == 1:
                    for j in v:
                        Start_SS = set(j)
                b = Start_SS & Next_SS
                if len(b) <= 1:
                    if u not in Result:
                        Result.append(u)
    if len(Start) == 1:
        Result = keep
    return Result


def List_Not_In(Start):  # Compare_DIFFDENS0
    Result = []
    Start_C = copy.deepcopy(Start)
    for h in Start_C:
        if h not in Result:
            Result.append(h)
    return Result


def Cut_Start_Edges_Sub_Cluster(Compare, Start):  # Compare_DIFFDENS1, Result <= 0
    # List[(),(),....] #Dict []
    # Result = []
    Result1 = []
    keep = []
    Start_L = copy.deepcopy(Start)
    Compare_L = copy.deepcopy(Compare)
    h = 0
    for v in Start_L.values():
        h += 1
        if h == 1:
            for i in Compare_L:
                Next_S = set(i)
                Start_Long = Change_Shlist_TO_Llist(v)
                Start_S = set(Start_Long)
                a = Start_S & Next_S
                if len(a) <= 0:
                    keep.append(i)
        if h >= 2:  # เอากิ่งที่เหลือมาหาก้อนต่อไป
            Result1 = []
            for u in keep:
                Next_SS = set(u)
                Start_Long1 = Change_Shlist_TO_Llist(v)
                Start_SS = set(Start_Long1)
                if len(v) == 1:
                    for j in v:
                        Start_SS = set(j)
                b = Start_SS & Next_SS
                if len(b) <= 0:
                    if u not in Result1:
                        Result1.append(u)
            Result0 = copy.deepcopy(Result1)
            keep = Result0
    Result = Result1
    if len(Start_L) == 1:
        Result = keep
    return Result


def Rest_Sub(Start, Compare):  # Compare_DIFFDENS1, Start_Sub
    # List [[],[],[]] # List [[],[],[]]
    Result = []
    keep = []
    Start_L = copy.deepcopy(Start)
    Compare_L = copy.deepcopy(Compare)
    for h in Start_L:
        Start_S = set(h)
        for i in Compare_L:
            Compare_S = set(i)
            a = Start_S & Compare_S
            if len(a) < 3:
                if i not in Result:
                    Result.append(i)
            if len(a) == 3:
                if i not in keep:
                    keep.append(i)

    return Result


def Result_CutNode(Start):  # Result_Copy
    # Dict {[]}
    Result = {}
    keep = []
    Start_D = copy.deepcopy(Start)
    j = 0
    for h in Start_D.values():
        j += 1
        if j == 1:
            Start_Long = Change_Shlist_TO_Llist(h)
            Start_S = set(Start_Long)
            Start_Long_1 = list(Start_S)  # list เฉพาะโหนดก้อน 1
            keep1 = copy.deepcopy(Start_Long_1)
            Result[j] = Start_Long_1
        if j >= 2:
            Start_Long1 = Change_Shlist_TO_Llist(h)
            Start_S1 = set(Start_Long1)
            Start_Long1_1 = list(Start_S1)  # list เฉพาะโหนดก้อน 2

            a = Start_S & Start_S1
            if len(a) >= 1:  # ถ้ามีเหมือนกันให้
                a = list(a)
                for i in a:
                    Start_Long1_1.remove(i)
                Result[j] = Start_Long1_1
                for u in Start_Long1_1:
                    keep1.append(u)
                Start_S = set(keep1)
            if len(a) == 0:
                Result[j] = Start_Long1_1
                for u in Start_Long1_1:
                    keep1.append(u)
                Start_S = set(keep1)

    return Result


def Tor_Rest_Sub(Start, Compare):  # Result, Start_Sub1
    # Dict {[]}  # List [[],[],....]
    Result = {}
    Start_D = copy.deepcopy(Start)
    Compare_L = copy.deepcopy(Compare)
    j = 0
    for h in Start_D.values():
        j += 1
        keep = []
        for i in Compare_L:
            Next_S = set(i)
            Start_S = set(h)
            a = Start_S & Next_S
            Result[j] = keep
            if len(a) == 2:
                if i not in keep:
                    keep.append(i)
                Result[j] = keep
                Compare_L.remove(i)
            if len(a) == 3:
                Compare_L.remove(i)
    k = 0
    for u in Start_D.values():
        k += 1
        keep = []
        if len(Compare_L) > 0:
            for v in Compare_L:
                Next_SS = set(v)
                Start_SS = set(u)
                b = Start_SS & Next_SS
                if len(b) == 1:
                    if v not in keep:
                        for q, w in Result.items():
                            if q == k:
                                keep = w
                        keep.append(v)
                    Result[k] = keep
                    Compare_L.remove(v)
                if len(b) == 3:
                    Compare_L.remove(v)
    return Result


def Check_Sub_before(Start, Compare):  # Result, Start_Sub1
    # Dict {[]} # List [[],[],.....]
    Start_D = copy.deepcopy(Start)
    Compare_L = copy.deepcopy(Compare)
    for h in Start_D.values():
        for i in h:
            Start_S = set(i)
            for u in Compare_L:
                Next_S = set(u)
                a = Start_S & Next_S
                if len(a) == 3:
                    Compare_L.remove(u)

    return Compare_L


def Add_Node_FTorSub(Start, Compare):  # Result_Cut_Node, Result_Sub_TorSub_Node
    # Dict {}  # Dict {}
    Result = {}
    Start_D = copy.deepcopy(Start)
    Compare_D = copy.deepcopy(Compare)
    k = 0
    for v in Compare_D.values():
        k += 1
        v_s = set(v)
        keep = v
        for q, u in Start_D.items():
            if q == k:
                u_s = set(u)
                keep += u
        a = v_s & u_s
        a = list(a)
        Result[k] = keep
        for h in a:
            keep.remove(h)
            Result[k] = keep

    return Result


def Check_Nodes_Rest(Start, Start_1, Compare):  # Result_Cut_Node, Result_Sub_TorSub, Node_Graph
    # Dict {}  # Dict  #
    PP = []
    # Result = []
    Start_D = copy.deepcopy(Start)
    Start_1_D = copy.deepcopy(Start_1)
    Compare_L = copy.deepcopy(Compare)
    Compare_S = set(Compare_L)
    k = 0
    for v in Start_D.values():
        k += 1
        keep = []
        keep += v
        for q, w in Start_1_D.items():
            if q == k:
                w_Long = Change_Shlist_TO_Llist(w)
                w_s = set(w_Long)
                w_L = list(w_s)
                keep += w_L
                PP.append(keep)
    P1 = Change_Shlist_TO_Llist(PP)
    P2 = set(P1)
    a = Compare_S - P2
    Result = list(a)

    return Result


def Check_Edge_Nodes_Rest(Start, Compare):  # Result_Rest_Node, Edges_Graph
    # List [[, , ,]]  # List [(),()]
    Result = {}
    keep = []
    keep1 = []
    Start_L = copy.deepcopy(Start)
    Compare_L = copy.deepcopy(Compare)
    Start_S = set(Start_L)
    for h in Compare_L:
        Next_S = set(h)
        a = Start_S & Next_S
        if len(a) >= 1:
            keep.append(h)
            if a not in keep1:
                a = tuple(a)
                if a not in keep1:
                    keep1.append(a)
    for u in keep1:
        u_s = set(u)
        keep2 = []
        for v in keep:
            v_s = set(v)
            b = u_s & v_s
            if len(b) == 1:
                keep2.append(v)
                Result[u] = keep2
                # keep.remove(v)

    return Result


def Dict_Unicode_Toint(Start):  # Dict {1:[[,,],[,,]..]}
    Start_D = copy.deepcopy(Start)
    Result1 = {}
    for u, v in Start_D.items():
        keep1 = []
        for h in v:
            keep = []
            for i in h:
                i = int(i)
                keep.append(i)
            keep1.append(keep)
        Result1[u] = keep1
    return Result1


def Dict_Unicode_Toint1(Start):  # Dict {1:[[.....],2:[.....]..]}
    Start_D = copy.deepcopy(Start)
    Result1 = {}
    for u, v in Start_D.items():
        keep1 = []
        for h in v:
            h = int(h)
            keep1.append(h)
        Result1[u] = keep1

    return Result1


def Result_CutEdge(Start, Compare):  # Result_Copy, Edges_Graph
    # Dict {1:[[,,],[,,]..]}  # List [[,,],[,,]....]
    Result = {}

    Start_D = copy.deepcopy(Start)
    Compare_D = copy.deepcopy(Compare)
    for h, i in Start_D.items():
        keep = []
        for u in i:
            u_s = set(u)
            for v in Compare_D:
                v_s = set(v)
                a = u_s & v_s
                if len(a) == 2:
                    keep.append(v)
        Result[h] = keep
    return Result


# --------- Measure --------- #
def Coverage_Cluster(Start, Compare):  # Result_Cut_Edges, Edges_Graph
    # Dict {1:[(,),(,)],2:[(,),(,)]}  # List [(,),(,)]
    Result = float()
    keep = []
    Start_D = copy.deepcopy(Start)
    Compare_D = copy.deepcopy(Compare)
    for h, i in Start_D.items():
        i_l = float(len(i))
        keep.append(i_l)
    sum1 = sum(keep)
    all_edges = float(len(Compare_D))
    Result = sum1 / all_edges
    Result = round(Result, 2)
    return Result


def Conductance_Cluster(Start, Compare, Compare1):  # Result_Copy, Result_Cut_Edges, Result_Sub_TorSub_Edge
    # Dict {1:[(,),(,)],2:[(,),(,)]}  # Dict {1:[(,),(,)],2:[(,),(,)]}
    Result = float()
    Result1 = {}
    Start_D = copy.deepcopy(Start)  # Sub Cluster
    Compare_D = copy.deepcopy(Compare)  # Edges inside
    Compare_D1 = copy.deepcopy(Compare1)  # TOR SUB
    keep_K = []
    for h, i in Start_D.items():  # Cluster
        i_Long = Change_Shlist_TO_Llist(i)
        i_s = set(i_Long)
        inter = []
        keep1 = []
        for u, v in Compare_D.items():  # Edges inside
            if h == u:  # ครัสเตอร์ตรงกับกิ่ง
                for t in v:  # แต่ละกิ่งในครัสเตอร์นั้น ๆ เพิ่มใน keep1
                    keep1.append(t)  # ตั้งต้น
                    intra1 = float(len(v))  # กิ่งภายในของก้อนนั้น
            if len(keep1) >= 1:  # ถ้า keep1 มีค่า
                if h != u:
                    for e in v:  # vกิ่ง ที่ไม่เท่ากับครัสเตอร์นั้น
                        e_s = set(e)
                        a = i_s & e_s
                        if len(a) == 1:
                            if e not in inter:
                                inter.append(e)
        for y, g in Compare_D1.items():
            for gg in g:
                gg_s = set(gg)
                b = i_s & gg_s
                if len(b) == 1:
                    if gg not in inter:
                        inter.append(gg)
            inter1 = float(len(inter))  # กิ่งภายนอกทั้งหมดของก้อนนี้
            C1 = inter1 / intra1
            keep_K.append(C1)
            break
    sum1 = sum(keep_K)
    V_C = len(Start_D)
    Result = 1.00 - ((1.00 / V_C) * sum1)
    Result = round(Result, 2)
    return Result


def Modularity_Cluster(Start, Compare, Compare1, Compare2):
    # Result_Copy, Result_Cut_Edges, Result_Sub_TorSub_Edge, Edges_Graph
    Result = float()
    Result1 = {}
    Start_D = copy.deepcopy(Start)  # Sub Cluster
    Compare_D = copy.deepcopy(Compare)  # Edges inside
    Compare_D1 = copy.deepcopy(Compare1)  # TOR SUB
    Compare_D2 = copy.deepcopy(Compare2)
    all_edge = float(len(Compare_D2))
    keep_K = []
    for h, i in Start_D.items():  # Cluster
        i_Long = Change_Shlist_TO_Llist(i)
        i_s = set(i_Long)
        inter = []
        keep1 = []
        for u, v in Compare_D.items():  # Edges inside
            if h == u:  # ครัสเตอร์ตรงกับกิ่ง
                for t in v:  # แต่ละกิ่งในครัสเตอร์นั้น ๆ เพิ่มใน keep1
                    keep1.append(t)  # ตั้งต้น
                    intra1 = float(len(v))  # กิ่งภายในของก้อนนั้น
            if len(keep1) >= 1:  # ถ้า keep1 มีค่า
                if h != u:
                    for e in v:  # vกิ่ง ที่ไม่เท่ากับครัสเตอร์นั้น
                        e_s = set(e)
                        a = i_s & e_s
                        if len(a) == 1:
                            if e not in inter:
                                inter.append(e)
        for y, g in Compare_D1.items():
            for gg in g:
                gg_s = set(gg)
                b = i_s & gg_s
                if len(b) == 1:
                    if gg not in inter:
                        inter.append(gg)
            inter1 = float(len(inter))  # กิ่งภายนอกทั้งหมดของก้อนนี้
            A1 = intra1 / all_edge
            A2 = (intra1 + inter1) / all_edge
            A3 = A1 - A2
            keep_K.append(A3)
            break
    Result = sum(keep_K)
    Result = round(Result, 2)
    return Result


# ----------- Draw Graph ----------- #

def Create_Graph_Cluster_Original(Node, Edge, Node_G):  # Result_Cut_Node, Result_Cut_Edges, G.node, G.edges
    # Dict {1:[[,,],[,,]..]}  # Dict {1:[[,,],[,,]..]}
    Node_D = copy.deepcopy(Node)
    Edge_D = copy.deepcopy(Edge)
    # ทำ Original Graph
    l = len(Node_G)
    # Node_GL_int = List_Unicode_Toint(Node_GL)
    # Edges_GL_int = List_Unicode_Toint(Edges_GL)
    # ----- Define position
    # N1 = 0
    # N2 = l
    # i = range(N1, N2)
    # random.shuffle(i)
    # i2 = copy.deepcopy(i)
    # random.shuffle(i2)
    colorList = ['c', 'red', 'magenta', 'green', 'GreenYellow', 'Salmon', \
                'orange', 'brown', 'purple', 'yellow', 'black']
    # pos = {}
    # K = nx.Graph()  # ไม่ให้ทำกับกราฟเก่า
    # for u, v in Node_D.items():
    #     if u == 1:
    #         m = 0
    #         for r in v:  # r = node , c = position
    #             pos[r] = c[m]
    #             m += 1
    #         K.add_nodes_from(pos.keys())  # บอกว่าจะเริ่มเพิ่มโหนดตามนี้ โหนดเป็น int
    #         for n, p in pos.iteritems():
    #                 K.node[n]['pos'] = p
    # draw_networkx(K, pos, edge_color='skyblue', node_color='red')
    # plt.show()
    print 'q'
    # เปลี่ยน unicode => int ทั้ง Cluster
    Edges_int = Dict_Unicode_Toint(Edge_D)
    Nodes_int = Dict_Unicode_Toint1(Node_D)

    # pos = {}
    m = 0
    ww = 1
    Q = 1
    pos = {}
    for o, v in Nodes_int.items():  # position
        c = [(17, 12), (19, 9), (34, 41), (35, 2), (15, 20), (4, 8), (12, 24), (1, 32), (13, 4), (33, 30), (10, 46),
             (41, 0), (30, 3), (8, 49), (39, 43), (43, 23), (24, 33), (7, 5), (11, 10), (2, 15), (3, 20), (22, 15),
             (47, 37), (37, 6), (16, 25), (23, 11), (36, 45), (26, 19), (13, 36), (42, 38), (27, 42), (28, 14),
             (38, 31), (5, 35), (49, 40), (10, 39), (32, 22), (12, 48), (21, 27), (18, 29), (25, 44), (40, 47),
             (6, 10), (44, 7), (29, 34), (46, 13), (45, 18), (48, 28), (31, 1), (20, 21)]
        for u in v:
            # N1 = 0
            # N2 = l
            # i = range(N1, N2)
            # random.shuffle(i)
            # i2 = copy.deepcopy(i)
            # random.shuffle(i2)
            # c = zip(i,i2)
            # c = [(17, 12), (19, 9), (34, 41), (35, 2), (15, 20), (4, 8), (12, 24), (1, 32), (13, 4), (33, 30), (10, 46),
            #      (41, 0),(30, 3), (8, 49), (39, 43), (43, 23), (24, 33), (7, 5), (11, 10), (2, 15), (3, 20), (22, 15),
            #      (47, 37),(37, 6),(16, 25), (23, 11), (36, 45), (26, 19), (13, 36), (42, 38), (27, 42), (28, 14),
            #      (38, 31), (5, 35),(49, 40),(10, 39), (32, 22), (12, 48), (21, 27), (18, 29), (25, 44), (40, 47),
            #      (6, 10), (44, 7), (29, 34),(46, 13),(45, 18), (48, 28), (31, 1), (20, 21)]
            pos[u] = c[m]
            m += 1

        K = nx.Graph()  # ไม่ให้ทำกับกราฟเก่า
        K.add_nodes_from(pos.keys())  # บอกว่าจะเริ่มเพิ่มโหนดตามนี้ โหนดเป็น int
        for n, p in pos.iteritems():
            K.node[n]['pos'] = p

        for r, t in Edges_int.items():
            if r == ww:
                for w in t:
                    w = list(w)
                    K.add_edge(int(w[0]), int(w[1]))

                draw_networkx(K, pos, edge_color='skyblue', node_color=colorList[Q % len(colorList)])
                plt.show()
                Q += 1
        ww += 1



def Create_Graph_Cluster_Cluster(Cut_node, Cut_edge):  # Result_Cut_Node, Result_Cut_Edges
    # Dict {1:[[,,],[,,]..]}
    Cut_Node_C = copy.deepcopy(Cut_node)
    Cut_Edge_C = copy.deepcopy(Cut_edge)

    colorList = ['c', 'red', 'magenta', 'green', 'GreenYellow', 'Salmon', \
                 'orange', 'brown', 'purple', 'yellow', 'black']

    Edges_int = Dict_Unicode_Toint(Cut_Edge_C)
    Nodes_int = Dict_Unicode_Toint1(Cut_Node_C)


def List_Unicode_Toint(Node_GL):
    # List[.......]
    Result = []
    for h in Node_GL:
        keep = []
        for u in h:
            u = int(u)
            keep.append(u)
        keep = tuple(keep)
        Result.append(keep)
    return Result


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
        if C >= 2:  # หา cycle ดีกรีรวมสูงสุดที่โหนดไม่ซ้ำเดิม
            B = DD
            if len(Cut_Edges_Start) == 0:
                Cut_Edges_Start = Cut_Edges
            # ทำ Sub graph จาก Cut_Edges_Start
            Start_Sub2 = Create_Graph_another(Cut_Edges_Start)
            if len(Start_Sub2) == 0:  # หากไม่มีซับเหลือจากโหนดที่เหลือที่ไม่เหมือนกับครัสเตอร์ก่อนหน้า
                # print 'กิ่งที่เหลือไม่เจอ Sub 3'
                Start_Sub2
                break
            M_Sub = D_Max_Degree_Sub(Start_Sub2)  # dict

            Start_Sub0 = Create_Graph_another(Cut_Edges)  # กราฟที่เหลือ
            Start_Sub1 = Plus_ListToLost2(Start_Sub2, Start_Sub0)  # List[[]]+[[]]
            # ต้องเช็คว่ามี Sub ซ้ำกันในครัสเตอร์ไหม
            Start_Sub1 = Check_Sub_before(Result, Start_Sub1)

        # หา Sub cycle ที่มีดีกรีรวมสูงสุด
        if C <= 1:
            M_Sub = D_Max_Degree_Sub(Start_Sub1)  # dict
        if len(M_Sub) >= 1:
            L_M_Sub = L_Max_Degree_Sub(M_Sub)  # List[]
            # print 'SUB เริ่มต้น =', L_M_Sub
        # เจอ M_Sub == 0
        if len(M_Sub) == 0:
            M_Sub = D_Max_Degree_Sub(Start_Sub1)  # dict
            # print 'M_Sub = 0'
            if len(M_Sub) == 0:
                M_Sub = Rest_Sub(Compare_DIFFDENS1, Start_Sub)

        # หา Sub cycle ที่มีโหนดเหมือนกัน 2 โหนดและโหนดที่เหลือมมีดีกรีโหนดมากที่สุด
        NS20 = Next_Sub_2n(L_M_Sub, Start_Sub1)  # ค้นหา SUB ที่มีโหนดเหมือนกัน 2 โหนด
        # ไม่มี Sub cycle ที่นำมาต่อแล้ว
        if len(NS20) == 0:
            Result[C] = [L_M_Sub]
            # print 'ไม่มีซับข้างเคียงแล้ว 1'
            Node_2 = Change_Shlist_TO_Llist(L_M_Sub)
            # print 'จำนวนโหนดในครัสเตอร์ 1 =', len(set(Node_2))
            # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
            # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
            Cut_Edges = Cut_Start_edges(Start_edge1, Result)
            # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
            Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]
            C += 1
            break  # หลุด Loop While A >= 0
        Node_SMD0 = Node_Sub_Degree(L_M_Sub, NS20, Start_degree)  # List[[]]
        # print 'Sub ที่เพิ่มขึ้น =', Node_SMD0
        Merge_NE0 = Plus_ListToLost(L_M_Sub, Node_SMD0)  # List[]+[[]]

        # หา กิ่ง ภายในที่มีอยู่ใน Sub ที่รวมกันในข้างต้น
        Ed_Inside0 = Edges_InsideSub(Merge_NE0, Start_edge1)
        # นำทั้งหมดที่ได้มาคำนวนหาค่า Difference Density
        DIFF_DENS0 = Difference_Density(Ed_Inside0)
        B = DIFF_DENS0
        # print 'DIFF_DENS0 =', DIFF_DENS0
        # นำค่าที่คำนวนได้มาแสดงผล
        Compare_DIFFDENS0 = Compare_DIFF(L_M_Sub, Merge_NE0, Ed_Inside0, DIFF_DENS0, DD)
        # ซ้อนเพื่อหาการซ้ำ
        Compare_DIFFDENS0 = List_Not_In(Compare_DIFFDENS0)
        # print 'Compare_DIFFDENS0 =', Compare_DIFFDENS0
        # ถ้าค่า DIFF_DENS0 น้อยกว่า DD
        if DIFF_DENS0 <= DD:
            Result[C] = Compare_DIFFDENS0
            # print 'ค่า DD ไม่ถึง 1'
            Node_2 = Change_Shlist_TO_Llist(Compare_DIFFDENS0)
            # print 'จำนวนโหนดในครัสเตอร์ 1 =', len(set(Node_2))
            # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
            # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
            Cut_Edges = Cut_Start_edges(Start_edge1, Result)
            # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
            Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]
            C += 1
            break
        if C <= 1:
            # List not in
            Cut_SUB0 = Cut_Sub_3(Start_Sub1, Compare_DIFFDENS0)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด
            # print 'Cut_SUB0 =', len(Cut_SUB0)
        if C >= 2:
            Cut_SUB0 = Start_Sub1
        # ถ้าไม่มี Sub cycle เหลืออยู่แล้ว
        if len(Cut_SUB0) == 0:
            Result[C] = Compare_DIFFDENS0
            # print 'ไม่มี Sub ต่อไปอีกแล้ว 1'
            Node_2 = Change_Shlist_TO_Llist(Compare_DIFFDENS0)
            # print 'จำนวนโหนดในครัสเตอร์ 1 =', len(set(Node_2))
            # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
            # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
            Cut_Edges = Cut_Start_edges(Start_edge1, Result)
            # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
            Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]
            C += 1
            break

        while B >= DD:  # Step 2
            # หา Sub cycle รอบๆ อีกครั้ง
            NS21 = Next_Sub_2n2(Compare_DIFFDENS0, Cut_SUB0)  # เลือก SUB มาต่อ
            # ถ้าไม่มี Sub cycle ข้างเคียงเหลืออยู่แล้ว
            if len(NS21) == 0:
                Result[C] = Compare_DIFFDENS0
                # print 'ไม่มีซับต่อไปอีกแล้ว 2'
                Node_2 = Change_Shlist_TO_Llist(Compare_DIFFDENS0)
                # print 'จำนวนโหนดในครัสเตอร์ 2 =', len(set(Node_2))
                # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
                # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                Cut_Edges = Cut_Start_edges(Start_edge1, Result)
                # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]
                C += 1
                break
            Node_SMD1 = Node_Sub_Degree2(Compare_DIFFDENS0, NS21, Start_degree)  # List[[]]
            # print 'Sub ที่เพิ่มขึ้น =', Node_SMD1
            Merge_NE1 = Plus_ListToLost2(Compare_DIFFDENS0, Node_SMD1)  # List[]+[[]]
            # หา กิ่ง ภายใน Sub ทั้งหมด
            Ed_Inside1 = Edges_InsideSub(Merge_NE1, Start_edge1)
            # คำนวนค่า Difference Density
            DIFF_DENS1 = Difference_Density(Ed_Inside1)
            # print 'DIFF_DENS0 =', DIFF_DENS1
            B = DIFF_DENS1
            # เปรียบเทียบค่า DD
            Compare_DIFFDENS1 = Compare_DIFF(Compare_DIFFDENS0, Merge_NE1, Ed_Inside1, DIFF_DENS1, DD)
            Compare_DIFFDENS1 = List_Not_In(Compare_DIFFDENS1)
            # print 'Compare_DIFFDENS1 =', Compare_DIFFDENS1

            if DIFF_DENS1 >= DD:
                Cut_SUB0 = Start_Sub1  # วน Step 2
                Compare_DIFFDENS0 = Compare_DIFFDENS1

            else:
                if C == 1:
                    Result[C] = Compare_DIFFDENS1
                    # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                    Cut_Edges = Cut_Edges_Cluster(Compare_DIFFDENS1, Start_edge1)  # List[(),()]
                    # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                    Cut_Edges_Start = Cut_Edges_Sub_Cluster(Compare_DIFFDENS1, Start_edge1)  # List[(),()]
                    # เอา โหนด ในครัสเตอร์ออกมา เพื่อที่จะเอากิ่งมาสร้างเป็นกราฟ == 1
                    Cut_Nodes = Cut_Nodes_Cluster(Compare_DIFFDENS1, Start_edge1)  # List[[],[]]
                    # print 'โหนดในครัสเตอร์ =', len(Cut_Nodes)

                if C >= 2:
                    # ให้ Compare_DIFFDENS1 = Result[1]+Result[2]+,...
                    Result[C] = Compare_DIFFDENS1
                    # นับจำนวนโหนด
                    Node_2 = Change_Shlist_TO_Llist(Compare_DIFFDENS1)
                    # print 'จำนวนโหนดในครัสเตอร์ 2 =', set(Node_2)
                    # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
                    # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                    Cut_Edges = Cut_Start_edges(Start_edge1, Result)
                    # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                    Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]

                C += 1
    H = len(Start_Sub)
    while H >= 0:
        if C >= 2:  # หา cycle ดีกรีรวมสูงสุดที่โหนดไม่ซ้ำเดิม
            B = DD
            if len(Cut_Edges_Start) == 0:
                Cut_Edges_Start = Cut_Edges

            Start_Sub2 = Create_Graph_another(Cut_Edges_Start)
            M_Sub = D_Max_Degree_Sub(Start_Sub2)  # dict
            # Start_Sub2, M_Sub == 0

            Start_Sub0 = Create_Graph_another(Cut_Edges)  # กราฟที่เหลือ
            Start_Sub1 = Plus_ListToLost2(Start_Sub2, Start_Sub0)  # List[[]]+[[]]
            Start_Sub1 = Check_Sub_before(Result, Start_Sub1)

            if len(M_Sub) >= 1:
                L_M_Sub = L_Max_Degree_Sub(M_Sub)  # List[]
                # print 'SUB เริ่มต้น =', L_M_Sub

            if len(M_Sub) == 0:
                # ต้องกำจัดโหนดที่แม่งซ้ำในแต่ละครัสเตอร์ออกก่อน
                Result_Copy = copy.deepcopy(Result)
                Result_Cut_Node = Result_CutNode(Result_Copy)
                Result_Cut_Edges = Result_CutEdge(Result_Copy, Edges_Graph)
                # ได้เฉพาะโหนดล้วนมาแระ
                # ก่อนต่อต่อเช็คที่เป็นแค่กิ่งระหว่างโหนดออกไปก่อน
                # Result_Cut_Sub_Edge = Result_CutSubEdge(Result_Cut_Node, Result_Copy)
                # ต้องเอาที่เหลือมาต่อ แต่ต้องแยกไว้
                Result_Sub_TorSub = Tor_Rest_Sub(Result_Cut_Node, Start_Sub1)
                Result_Sub_TorSub_Node = Result_CutNode(Result_Sub_TorSub)
                Result_Sub_TorSub_Edge = Result_CutEdge(Result_Sub_TorSub, Edges_Graph)
                # หาโหนดที่เหลืออยู่ โหนดที่ไม่ถูกนำมาจัด
                Result_Rest_Node = Check_Nodes_Rest(Result_Cut_Node, Result_Sub_TorSub, Node_Graph)
                print 'โหนดที่ไม่ถูกจัดอยู่ในครัสเตอร์ =', Result_Rest_Node
                # จาก Result_Rest_Node นำมาหากิ่งของโหนดที่เหลือ วาดรูปเช็คซับอีกรอบ
                Result_Rest_Node_Edge = Check_Edge_Nodes_Rest(Result_Rest_Node, Edges_Graph)
                Sub3_1 = Create_Graph_Edges(Result_Rest_Node_Edge)
                # Result_Cut_Node_2 = Add_Node_FTorSub(Result_Cut_Node, Result_Sub_TorSub_Node)

                # จุดจบที่นี่ ที่ต้องใช้คือ
                # Coverage
                Coverage_D = Coverage_Cluster(Result_Cut_Edges, Edges_Graph)
                print 'ค่า Coverage Matric = ', Coverage_D
                # Conductance
                Conductance_D = Conductance_Cluster(Result_Copy, Result_Cut_Edges, Result_Sub_TorSub_Edge)
                print 'ค่า Conductance Matric = ', Conductance_D
                # Modularity
                Modularity_D = Modularity_Cluster(Result_Copy, Result_Cut_Edges, Result_Sub_TorSub_Edge, Edges_Graph)
                print 'ค่า Mpdularity Matric = ', Modularity_D
                # สร้ากราฟ 1 Original 2 Cluster ใช้ K = nx.Graph() เปลี่ยนโหนดเป็น int นะ
                Create_Graph_Cluster_Original(Result_Cut_Node, Result_Cut_Edges, G.node)
                Create_Graph_Cluster_Cluster(Result_Cut_Node, Result_Cut_Edges)
                break
            # หา Sub cycle ที่มีโหนดเหมือนกัน 2 โหนดและโหนดที่เหลือมมีดีกรีโหนดมากที่สุด
            NS20 = Next_Sub_2n(L_M_Sub, Start_Sub1)  # ค้นหา SUB ที่มีโหนดเหมือนกัน 2 โหนด
            # ไม่มี Sub cycle ที่นำมาต่อแล้ว
            if len(NS20) == 0:
                Result[C] = [L_M_Sub]
                print 'ไม่มีซับข้างเคียงแล้ว 1'
                Node_2 = Change_Shlist_TO_Llist(L_M_Sub)
                print 'จำนวนโหนดในครัสเตอร์ 1 =', len(set(Node_2))
                # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
                # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                Cut_Edges = Cut_Start_edges(Start_edge1, Result)
                # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]
                C += 1
                break  # หลุด Loop While A >= 0
            Node_SMD0 = Node_Sub_Degree(L_M_Sub, NS20, Start_degree)  # List[[]]
            print 'Sub ที่เพิ่มขึ้น =', Node_SMD0
            Merge_NE0 = Plus_ListToLost(L_M_Sub, Node_SMD0)  # List[]+[[]]

            # หา กิ่ง ภายในที่มีอยู่ใน Sub ที่รวมกันในข้างต้น
            Ed_Inside0 = Edges_InsideSub(Merge_NE0, Start_edge1)
            # นำทั้งหมดที่ได้มาคำนวนหาค่า Difference Density
            DIFF_DENS0 = Difference_Density(Ed_Inside0)
            B = DIFF_DENS0
            print 'DIFF_DENS0 =', DIFF_DENS0
            # นำค่าที่คำนวนได้มาแสดงผล
            Compare_DIFFDENS0 = Compare_DIFF(L_M_Sub, Merge_NE0, Ed_Inside0, DIFF_DENS0, DD)
            # ซ้อนเพื่อหาการซ้ำ
            Compare_DIFFDENS0 = List_Not_In(Compare_DIFFDENS0)
            print 'Compare_DIFFDENS0 =', Compare_DIFFDENS0
            # ถ้าค่า DIFF_DENS0 น้อยกว่า DD
            if DIFF_DENS0 <= DD:
                Result[C] = Compare_DIFFDENS0
                print 'ค่า DD ไม่ถึง 1'
                Node_2 = Change_Shlist_TO_Llist(Compare_DIFFDENS0)
                print 'จำนวนโหนดในครัสเตอร์ 1 =', len(set(Node_2))
                # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
                # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                Cut_Edges = Cut_Start_edges(Start_edge1, Result)
                # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]
                C += 1
                break

            if C <= 1:
                # List not in
                Cut_SUB0 = Cut_Sub_3(Start_Sub1, Compare_DIFFDENS0)  # ตัด SUB ที่ได้ออกจาก SUB ทั้งหมด
                print 'Cut_SUB0 =', len(Cut_SUB0)
            if C >= 2:
                Cut_SUB0 = Start_Sub1
            # ถ้าไม่มี Sub cycle เหลืออยู่แล้ว
            if len(Cut_SUB0) == 0:
                Result[C] = Compare_DIFFDENS0
                print 'ไม่มี Sub ต่อไปอีกแล้ว 1'
                Node_2 = Change_Shlist_TO_Llist(Compare_DIFFDENS0)
                print 'จำนวนโหนดในครัสเตอร์ 1 =', len(set(Node_2))
                # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
                # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                Cut_Edges = Cut_Start_edges(Start_edge1, Result)
                # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]
                C += 1
                break

            while B >= DD:  # Step 2
                # หา Sub cycle รอบๆ อีกครั้ง
                NS21 = Next_Sub_2n2(Compare_DIFFDENS0, Cut_SUB0)  # เลือก SUB มาต่อ
                # ถ้าไม่มี Sub cycle ข้างเคียงเหลืออยู่แล้ว
                if len(NS21) == 0:
                    Result[C] = Compare_DIFFDENS0
                    print 'ไม่มีซับต่อไปอีกแล้ว 2'
                    Node_2 = Change_Shlist_TO_Llist(Compare_DIFFDENS0)
                    print 'จำนวนโหนดในครัสเตอร์ 2 =', len(set(Node_2))
                    # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
                    # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                    Cut_Edges = Cut_Start_edges(Start_edge1, Result)
                    # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                    Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]
                    C += 1
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
                Compare_DIFFDENS1 = List_Not_In(Compare_DIFFDENS1)
                print 'Compare_DIFFDENS1 =', Compare_DIFFDENS1

                if DIFF_DENS1 >= DD:
                    Cut_SUB0 = Start_Sub1  # วน Step 2
                    Compare_DIFFDENS0 = Compare_DIFFDENS1

                else:
                    if C == 1:
                        Result[C] = Compare_DIFFDENS1
                        # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                        Cut_Edges = Cut_Edges_Cluster(Compare_DIFFDENS1, Start_edge1)  # List[(),()]
                        # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                        Cut_Edges_Start = Cut_Edges_Sub_Cluster(Compare_DIFFDENS1, Start_edge1)  # List[(),()]
                        # เอา โหนด ในครัสเตอร์ออกมา เพื่อที่จะเอากิ่งมาสร้างเป็นกราฟ == 1
                        Cut_Nodes = Cut_Nodes_Cluster(Compare_DIFFDENS1, Start_edge1)  # List[[],[]]
                        print 'โหนดในครัสเตอร์ =', len(Cut_Nodes)

                    if C >= 2:
                        # ให้ Compare_DIFFDENS1 = Result[1]+Result[2]+,...
                        Result[C] = Compare_DIFFDENS1
                        # นับจำนวนโหนด
                        Node_2 = Change_Shlist_TO_Llist(Compare_DIFFDENS1)
                        print 'จำนวนโหนดในครัสเตอร์ 2 =', set(Node_2)
                        # ตัดกิ่งก้อน 1 , 2 ออกจากกิ่งทั้งหมด
                        # เอา SUB มา Compare กับกิ่ง เอากิ่งที่เหมือนกับ SUB 1 index <=1
                        Cut_Edges = Cut_Start_edges(Start_edge1, Result)
                        # เอา SUB มา Compare กับกิ่ง เอากิ่งที่ไม่มีโหนดในครัสเตอร์ก้อนแรก == 0
                        Cut_Edges_Start = Cut_Start_Edges_Sub_Cluster(Start_edge1, Result)  # List[(),()]

                    C += 1

    return Result


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

C1 = Make_Cluster(Sub3_L, Edges_Graph, DD, Node_Degree)