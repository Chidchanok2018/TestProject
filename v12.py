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
# Sub4 = [c for c in nx.cycle_basis(G) if len(c) == 4]
# print'Len of Sub3', len(Sub3), 'Cycles'  # พิมพ์จำนวน cycle3 ในกราฟ
# Sub_cycle3_sort = sorted(Sub3)  # เรียง Sub3 ใหม่จากน้อยไปมาก list[['11','80','79']]


# -------------Definition of Program--------------#

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
    T1 = Start
    T11 = copy.deepcopy(T1)
    for i in Plus:
        T1.append(i)
    return T1

def Change_ListToSet(Start):  # ทำ List[[],[]] เป็น [set[],set[],set[]]
    T1 = []
    for i in Start:
        T = set(i)
        T1.append(T)
    return T1

def Next_SN2(Start, Compare, V):
    # List[['','',''],['','','']]  List[['','',''],['','','']]
    Result = []
    Keep = []
    for h in Start:
        count = len(Compare)
        Start_L = h
        Start_S = set(h)
        Result.append(Start_L)
        for i in range(count - 1):
            Next_L = Compare[i]
            Next_S = set(Next_L)
            a = Start_S & Next_S
            if len(a) >= V:
                Result.append(Next_L)
            else:
                Keep.append(Next_L)
        return Result  # List[['','',''],['','','']]


def DiffDen(Compare3, DD):
    # List[['','',''],['','','']]  List[['','',''],['','','']]
    Result = []
    Keep = []
    G = nx.Graph()
    Result_L = []
    for item3 in Compare3:
        count3 = len(Compare3)
        # count4 = len(Compare4)
        Result_L.append(item3)
        for i in range(count3 - 1):  # รอบ 3 โหนดรอบแรก
            Start = item3
            Next = Compare3[i]
            if i > 0:
                Start = a
            a = Start + Next
            G.add_cycle(a)
            draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            # plt.show()

            b = set(Start) & set(Next)
            Number_of_Edges_Out = 0.00  # จำนวนกิ่งภายนอกครัสเตอร์
            Number_of_Edes_All = float(len(G.edges))  # จำนวนกิ่งภายในครัสเตอร์
            if i >= 2:
                Number_of_Edes_All = float(len(G.edges)) - 1.00 # จำนวนกิ่งภายในครัสเตอร์
            N = float(len(G.nodes))  # จำนวนโหนดทั้งหมด
            N_C = float(len(G.nodes))  # จำนวนโหนดภายในครัสเตอร์
            if len(b) >= 2:  # มีโหนดเหมือนมากกว่า 2 โหนด
                # inter Cluster Density
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
                if Dif_Den_N2 >= DD:
                    Result = a
                    if Next not in Result_L:
                        Result_L.append(Next)
                else:
                    G.clear()
                    a.pop(-1)
                    a.pop(-1)
                    a.pop(-1)
                    G.add_cycle(a)
                    draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                    # plt.show()
                    Keep.append(Next)
            else:
                G.clear()
                a.pop(-1)
                a.pop(-1)
                a.pop(-1)
                G.add_cycle(a)
                draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                # plt.show()
                Keep.append(Next)

        # for ii in range(count4 - 1):
        #     Start = a
        #     Next = Compare4[ii]
        #     if i > 0:
        #         Start = a
            # a = Start + Next
            # G.add_cycle(a)
            # draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            # plt.show()
            #
            # b = set(Start) & set(Next)
            # Number_of_Edges_Out = 0.00  # จำนวนกิ่งภายนอกครัสเตอร์
            # Number_of_Edes_All = float(len(G.edges)) - 1.0 # จำนวนกิ่งภายในครัสเตอร์
            # N = float(len(G.nodes))  # จำนวนโหนดทั้งหมด
            # N_C = float(len(G.nodes))  # จำนวนโหนดภายในครัสเตอร์
            # if len(b) >= 2:  # มีโหนดเหมือนมากกว่า 2 โหนด
            #     inter Cluster Density
                # if (N_C * (N - N_C)) <= 0.00:  # ถ้าส่วนเป็น 0 ให้ inter-edges = 0
                #     interN4 = 0.00
                #     Re_inter4 = interN4
                # elif Number_of_Edges_Out <= 0.00:  # ถ้าเศษเป็น 0 ให้ inter-edges = 0
                #     interN4 = 0.00
                #     Re_inter4 = interN4
                # else:  # นอกนั้นคำนวนได้
                #     inter_1 = ((N_C * (N - N_C)))
                #     inter_2 = (Number_of_Edges_Out) / inter_1
                #     Re_inter4 = round(inter_2, 2)  # ให้เหลือทศนิยม 2 ตำแหน่ง
                # intra cluster Density
                # if (N_C * (N - 1) / 2) <= 0.00:
                #     intra4 = 0.00
                #     Re_intra4 = intra4
                # elif Number_of_Edes_All <= 0.00:
                #     intra4 = 0.00
                #     Re_intra4 = intra4
                # else:
                #     intra_1 = (N_C * (N - 1.00) / 2.00)
                #     intra_2 = (Number_of_Edes_All) / (N_C * (N_C - 1) / 2)
                #     Re_intra4 = round(intra_2, 2)
                # Dif_Den_N3 = Re_intra4 - Re_inter4
                # if Dif_Den_N3 >= 0.55:
                #     Result = a
                # else:
                #     G.clear()
                #     for U in range(len(Next)):
                #         a.pop(-1)
                #     G.add_cycle(a)
                #     draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                #     plt.show()
                #     Keep.append(Next)
            # else:
            #     G.clear()
            #     for U in range(len(Next)):
            #         a.pop(-1)
            #     G.add_cycle(a)
            #     draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            #     plt.show()
            #     Keep.append(Next) #
        return Result_L  # D1 = List[['','',''],['','','']]

def Cut_Sub(Start, Compare):  # หา Sub ที่เหลือจากทั้งหมด
    # List[['','',''],['','','']]  List[['','',''],['','','']]
    Result = []  # กำหนด type ให้ตัว Return
    Keep = []
    Start_L = Change_Shlist_TO_Llist(Start)
    Start_S = set(Start_L)
    for h in Start_S:
        count = len(Compare)
        for i in range(count):
            Next = Compare[i]
            Next_S = set(Next)
            a = Start_S & Next_S  # สมาชิกที่ซ้ำกัน
            if len(a) == 3:  # ไม่เอาที่ซ้ำกันหมด
                Keep.append(Next)
            else:
                if Next not in Result:
                    Result.append(Next)

        return Result  # CutSub = [['','',''],['','','']]


def draw_Cluster(Start, Compare):
    # List[['','',''],['','','']] List[['','',''],['','','']]
    Result = []
    k = nx.Graph()
    for h in Start:
        Start_L = h
        count = len(Start)
        for i in range(count - 1):
            Next_L = Start[i+1]
            a = Start_L + Next_L
            k.add_cycle(a)
            draw_networkx(k, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            # plt.show()
        for J in Compare:
            Start_LL = a + J
            count1 = len(Compare)
            for O in range(count1 - 1):
                Next_LL = Compare[O + 1]
                aa = Start_LL + Next_LL
                k.add_cycle(aa)
                draw_networkx(k, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                # plt.show()

            return

def Check_inter_Edges(Start, Compare):  # Cluster, All Edges
    # Dict{0:['','',''],1:['','','']}  List[('','',''),('','','')]
    Result = {}
    Result1 = {}
    Keep = []
    kep = []
    u = 0
    Start1 = copy.deepcopy(Start)
    for k, v in Start.items():
        Result1[k] = Change_Shlist_TO_Llist(v)
    # for h in Compare:
    #     Start_L = list(h)
    #     Start_S = set(h)
    #     count = len(Start)
    #     for i in range(count):
    #         G = nx.Graph()
    #         Next_L = Result1[i]
    #         Next_S = set(Next_L)
    #         a = Start_S & Next_S
    #         if len(a) == 1:
    #             if u == 0:
    #                 Result[i] = Start_L
    #             if u >= 1:
    #                 Result[i] = Start_L
    #         else:
    #             Keep.append(Start_L)
    #     u += 1
    i = 0
    for r in Result1.values():
        count = len(Compare)
        for e in range(count):
            Start_L = r
            Start_S = set(r)
            Next_L = list(Compare[e])
            Next_S = set(Next_L)
            a = Start_S & Next_S
            if len(a) == 1:
                kep.append(Next_L)
                Result[i] = kep
            else:
                Keep.append(Next_L)
        kep = []
        i += 1
    return Result


def Make_Cluster(Cycles, R):
    Result = {}
    keep = []
    Cycles_Def = copy.deepcopy(Cycles)
    w = 1
    h = 0
    i = len(Cycles_Def)
    while w > 0:
        Cycles_sort = sorted(Cycles_Def)
        N0 = Next_SN2(Cycles_Def, Cycles_sort, 2)  # หา SUB ข้างเคียงที่เหลืออยู่
        w = len(N0)  # หาก Sub ข้างเคียงไม่เหลือ
        D0 = DiffDen(N0, 0.65)  # เอา N0 มาคำนวนหา DD
        if len(D0) == 0:
            Result[h] = N0
            break
        w = len(D0)  # หากคำนวน DD แล้วไม่มีรอดสัก SUB
        # ตัดออกจาก SUB ทั้งหมด
        if h == 0:
            C0 = Cut_Sub(D0, Cycles)  # ตัดก้อนเล็กออกจากกอง SUB ทั้งหมด
        if h >= 1:
            D1 = copy.deepcopy(D0)
            D1 += keep
            C0 = Cut_Sub(D1, Cycles)
        if len(C0) == 0:
            Result[h] = D0
            break
        w = len(C0)  # หากไม่มี SUB เหลืออยู่
        C0_sort = sorted(C0)
        # เริ่มเอา SUB มาต่อรอบๆก้อนเล็ก
        N0_1 = Next_SN2(C0, C0_sort, 2)  # หา SUB ที่เหลือมาหาที่เหมือนกับก้อนเล็ก
        if N0_1 is None:
            Result[h] = D0
        if len(N0_1) == 0:
            Result[h] = D0
        w = len(N0_1)
        D0_1 = copy.deepcopy(D0)
        P0 = Plus_ListToLost(D0_1, N0_1)  # เอาก้อนเล็ก + N0_1
        w = len(Cycles_Def) - len(P0)
        # วาดรูป
        # draw_Cluster(D0_1, N0_1)  # วาดเฉพาะก้อน P0
        # จัดใส่ผลลัพท์
        Result[h] = P0  # {ก้อนครัสเตอร์ : กิ่งรอบ ๆ}
        h += 1
        # if h == R:
        #     break
        # ตัดก้อนครัสเตอร์ออกจาก Sub ทั้งหมด
        keep += P0  # เก็บจำนวน SUB ในครัสเตอร์
        if h == 1:
            C0_1 = Cut_Sub(P0, Cycles)  # Sub ที่เหลืออยู่
        if h >= 2:
            C0_1 = Cut_Sub(keep, Cycles)  # Sub ที่เหลืออยู่
        Cycles_Def = C0_1
        if len(C0_1) == 1:
            Result[h] = C0_1
            w = 0  # จบการทำงานไปเลย
        w = len(C0_1)  # หากไม่มีซับเหลืออยู่แล้ว

    return Result

def Cluster_Cut_ALLSub(Start, Compare):
    Result = []
    keep = []
    kep = []
    # รวมครัสเตอร์ก่อน
    count = len(Start)
    for i in range(count):  # วนทุกครัสเตอร์
        Start_L = Start[i]
        Start_Long = Change_Shlist_TO_Llist(Start_L)
        keep += Start_Long
    keep_S = set(keep)
    count1 = len(Compare)
    for h in range(count1):
        Next_L = Compare[h]
        Next_S = set(Next_L)
        a = keep_S & Next_S
        if len(a) == 3:
            kep.append(Next_L)
        else:
            Result.append(Next_L)

    return Result


def Cluster_Tor_RSub(Start1, Compare, V):
    Result = {}
    Result1 = {}
    keep = []
    # a = []
    # count = len(Start)
    # k = nx.Graph()
    # for h in Start.values():  # ทำกราฟจากครัสเตอร์ก้อนแรก
    #     Start_L = h
    #     for u in Start_L:
    #         Start_LL = u
    #         count = len(Start_L)
    #         for i in range(count):
    #             Next_LL = Start_L[i+1]
    #             if i >= 1:
    #                 Start_LL = keep
    #             a = Start_LL + Next_LL
    #             k.add_cycle(a)
    #             draw_networkx(k, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
    #             # plt.show()
    #             keep = a
    Start = copy.deepcopy(Start1)
    for e, r in Start1.items():
        Result1[e] = r
    for k, v in Start.items():
        Result[k] = Change_Shlist_TO_Llist(v)
    for h in Compare:
        Start_L = h
        Start_S = set(h)
        count = len(Start)
        for i in range(count):
            G = nx.Graph()
            Next_1 = Result1[i]
            Next_L = Result[i]
            Next_S = set(Next_L)
            a = Start_S & Next_S
            if len(a) == V:
                b = Start_L + Next_L
                G.add_cycle(b)
                draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                # plt.show()
                Number_of_Edges_Out = 0.00  # จำนวนกิ่งภายนอกครัสเตอร์
                Number_of_Edes_All = float(len(G.edges))  # จำนวนกิ่งภายในครัสเตอร์
                if i >= 2:
                    Number_of_Edes_All = float(len(G.edges)) - 1.00  # จำนวนกิ่งภายในครัสเตอร์
                N = float(len(G.nodes))  # จำนวนโหนดทั้งหมด
                N_C = float(len(G.nodes))  # จำนวนโหนดภายในครัสเตอร์

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
                if Dif_Den_N2 >= 0.00:
                    Result[i] = b
                    Next_1.append(Start_L)

    return Result1

def Nodes_intra(Start):
    Result = {}
    Result_1 = {}
    keep = []
    Start1 = copy.deepcopy(Start)
    for e, r in Start1.items():
        Result[e] = r
    for h, i in Result.items():
        Start_L = i
        Start_Long = Change_Shlist_TO_Llist(Start_L)
        k = nx.Graph()
        k.add_cycle(Start_Long)
        draw_networkx(k, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
        # plt.show()
        N = float(len(k.nodes))  # จำนวนโหนดทั้งหมด
        Result_1[h] = N
    return Result_1

print'------เริ่มทำการหาครัสเตอร์---Snow ball 2---------------'
print'จำนวนโหนดทั้งหมดในกราฟ ', Number_of_nodes, 'โหนด'
print'จำนวน Sub3 ทั้งหมด', len(Sub3), 'โหนด'
Node_Graph = [i for i in G.nodes]  # ก้อนยาวๆ
# print'Node_Graph =', Node_Graph
Edges_Graph = [i for i in G.edges]  # ก้อนสั้นๆ
# print'Edges_Graph =', Edges_Graph
DD = float(0.65)

# --------------------------------------------------------#
# หา cycles ข้างเคียงที่มีโหนดเหมือนกันจำนวน 2 โหนด Sub3=list[['23','8','30']]
# ทำให้เป็น List จะได้ง่าย
Sub3_L = Change_SetTolist(Sub3)
Sub3_L_sort = sorted(Sub3_L)

# N1 = Next_SN2(Sub3_L, Sub3_L_sort, 2)
# D1 = DiffDen(N1, DD)
# C1 = Cut_Sub(D1, Sub3_L)  # ตัดครัสเตอร์แรกออกจากกอง SUB ทั้งหมด
# C1_sort = sorted(C1)
# N1_1 = Next_SN2(C1, C1_sort, 1)  # หารอบ ๆ ครัสเตอร์
# draw_Cluster(D1, N1_1)
# D1_1 = copy.deepcopy(D1)
# P1 = Plus_ListToLost(D1_1, N1_1)  # ได้ก้อนครัสเตอร์ 1
# ED1 = Check_inter_Edges(P1, Edges_Graph)  # กิ่งที่ต่อกับครัสเตอร์ 1
# C1_1 = Cut_Sub(P1, Sub3_L)  # Sub ที่เหลืออยู่
D_Cluster = Make_Cluster(Sub3_L, 5)  # ได้ครัสเตอร์ออกมาตามที่กำหนด
D_Nodes_intra = Nodes_intra(D_Cluster)
print 'Nodes intra =', D_Nodes_intra