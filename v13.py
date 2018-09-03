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
        for i in range(count):
            Next_L = Compare[i]
            Next_S = set(Next_L)
            a = Start_S & Next_S
            if len(a) >= V:
                Result.append(Next_L)
            else:
                Keep.append(Next_L)
        return Result  # List[['','',''],['','','']]


def DiffDen(Compare3, DD):
    # List[['','',''],['','','']]
    Result = []
    Keep = []
    G = nx.Graph()
    Result_L = []
    for item3 in Compare3:
        count3 = len(Compare3)
        # count4 = len(Compare4)
        Result_L.append(item3)
        for i in range(count3):  # รอบ 3 โหนดรอบแรก
            Start = item3
            Next = Compare3[i]
            if i > 0:
                Start = a
            a = Start + Next
            G.add_cycle(a)
            draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            plt.show()

            b = set(Start) & set(Next)
            Number_of_Edges_Out = 0.00  # จำนวนกิ่งภายนอกครัสเตอร์
            Number_of_Edes_All = float(len(G.edges))  # จำนวนกิ่งภายในครัสเตอร์
            # if i >= 2:
            #     Number_of_Edes_All = float(len(G.edges)) - 1.00 # จำนวนกิ่งภายในครัสเตอร์
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
                    plt.show()
                    Keep.append(Next)
            else:
                G.clear()
                a.pop(-1)
                a.pop(-1)
                a.pop(-1)
                G.add_cycle(a)
                draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                plt.show()
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

def Cut_Sub(Start, Compare):  # หา Sub ที่เหลือจากทั้งหมด ไม่เอาซ้ำหมด
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
            if len(a) == 2:  # ไม่เอาที่ซ้ำกันหมด
                if Next not in Result:
                    Result.append(Next)
            else:
                Keep.append(Next)

        return Result  # CutSub = [['','',''],['','','']]

def Cut_Sub_2(Start, Compare):  # หา Sub ที่เหลือจากทั้งหมด
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
            if len(a) == 3:  # เอาที่ซ้ำกันหมด
                Keep.append(Next)
            else:
                if Next not in Result:
                    Result.append(Next)

        return Keep  # CutSub = [['','',''],['','','']]

def Cut_Sub_3(Start, Compare):  # ไม่เอาที่ซ้ำกันใน Compare
    Result = []
    keep = []
    for h in Start:
        Start_L = h
        if Start_L not in Compare:
            Result.append(Start_L)

    return Result

def DiffDen2(Compare3, DD):
    # List[['','',''],['','','']]
    Result = []
    Keep = []
    G = nx.Graph()
    Result_L = []
    for item3 in Compare3:
        count3 = len(Compare3)
        # count4 = len(Compare4)
        Result_L.append(item3)
        for i in range(count3):  # รอบ 3 โหนดรอบแรก
            Start = item3
            Next = Compare3[i]
            if i > 0:
                Start = a
            a = Start + Next
            G.add_cycle(a)
            draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            plt.show()

            b = set(Start) & set(Next)
            Number_of_Edges_Out = 0.00  # จำนวนกิ่งภายนอกครัสเตอร์
            Number_of_Edes_All = float(len(G.edges))  # จำนวนกิ่งภายในครัสเตอร์
            # if i >= 2:
            #     Number_of_Edes_All = float(len(G.edges)) - 1.00 # จำนวนกิ่งภายในครัสเตอร์
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
                    plt.show()
                    Keep.append(Next)
            else:
                G.clear()
                a.pop(-1)
                a.pop(-1)
                a.pop(-1)
                G.add_cycle(a)
                draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                plt.show()
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


def Make_Cluster(Cycles, R):
    Result = {}
    keep = []
    Cycles_Def = copy.deepcopy(Cycles)
    w = 1
    h = 0
    i = len(Cycles_Def)
    while w > 0:
        Cycles_sort = sorted(Cycles_Def)
        N0 = Next_SN2(Cycles_Def, Cycles_sort, 2)  # หา SUB ข้างเคียงที่เหลืออยู่ ซ้ำกันมากกว่า2
        w = len(N0)  # หาก Sub ข้างเคียงไม่เหลือ
        D0 = DiffDen(N0, R)  # เอา N0 มาคำนวนหา DD
        if D0 is None:
            Result[h] = D0
            break
        if len(D0) == 0:
            Result[h] = N0
            break
        w = len(D0)  # หากคำนวน DD แล้วไม่มีรอดสัก SUB

        if h == 0:
            C00 = Cut_Sub_2(D0, Cycles)  # มีโหนดที่ซ้ำกัน3 หากิ่งเพิ่ม
            D00 = DiffDen(C00, R)  # คำนวน Sub ที่ตกค้าง
            # หา SUB ข้างเคียงเพิ่ม เผื่อเจอมากขึ้น
            N1 = Cut_Sub(D00, Cycles)  # เอาที่เหมือนกัน 2 โหนด

            D01 = copy.deepcopy(D00)
            P0 = Plus_ListToLost(D01, N1)  # รวมกับก้อนที่หามาก่อนหน้านี้
            D01 = DiffDen2(P0, R)  # คำนวน Sub ที่ตกค้าง
            C01 = Cut_Sub_2(D01, Cycles)  # มีโหนดที่ซ้ำกัน3 หากิ่งเพิ่มอีก
            C02 = Cut_Sub_3(C01, D01)  # ไม่เอาที่ซ้ำกันใน D02

            D02 = copy.deepcopy(D01)
            P1 = Plus_ListToLost(D02, C02)  # รวมกับก้อนที่หามาก่อนหน้านี้
            D03 = DiffDen2(P1, R)  # คำนวน Sub ที่ตกค้าง
            

            C0 = Cut_Sub_3(Cycles, D03)  # ไม่เอาที่ซ้ำกันใน C03
            keep += D03  #  เก็บ
            Result[h] = D03  # {ก้อนครัสเตอร์ : Sub ครัสเตอร์}
            # หากไม่มีแล้ว
            # while len(D00) != len(C01):
            #     D00 = DiffDen(C01, 0.50)
            #     C01 = Cut_Sub_2(D00, Cycles)  # มีโหนดที่ซ้ำกัน3 หากิ่งเพิ่ม
            # C0 = Cut_Sub_3(Cycles, C01)  # ไม่เอาที่ซ้ำกันใน C01
            # keep += C01  #
            # Result[h] = C01  # {ก้อนครัสเตอร์ : Sub ครัสเตอร์}

        if h >= 1:
            C00 = Cut_Sub_2(D0, Cycles,)  # มีโหนดที่ซ้ำกัน3 หากิ่งเพิ่ม แต่จะมีในก้อน1มาด้วย
            C01 = Cut_Sub_3(C00, keep)  # ไม่เอาที่ซ้ำกันใน keep ก้อนแรก ก้อนจริง
            D00 = DiffDen2(C01, 0.50)  # คำนวน Sub ที่ตกค้าง

            # C02 = Cut_Sub_2(D00, Cycles)  # มีโหนดที่ซ้ำกัน3 หากิ่งเพิ่ม
            # C03 = Cut_Sub_3(C02, keep)  # ไม่เอาที่ซ้ำกันใน keep
            # while len(C01) != len(C03):
            #     D00 = DiffDen(C03, 0.50)
            #     C02 = Cut_Sub_2(D00, Cycles)  # มีโหนดที่ซ้ำกัน3 หากิ่งเพิ่ม
            #     C03 = Cut_Sub_3(C02, keep)  # ไม่เอาที่ซ้ำกันใน keep
            # keep += C03  #
            # Result[h] = C03  # {ก้อนครัสเตอร์ : Sub ครัสเตอร์}
            C0 = Cut_Sub_3(Cycles, keep)  # ไม่เอาที่ซ้ำกันใน C03

        if len(C0) == 0:
            Result[h] = D00
            break
        Cycles_Def = C0
        h += 1
        w = len(C0)  # เช็ค Sub ที่เหลือ

    return Result


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
D_Cluster = Make_Cluster(Sub3_L, 0.5)  # ได้ครัสเตอร์ออกมาตามที่กำหนด