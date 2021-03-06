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
Sub_cycle3_sort = sorted(Sub3)  # เรียง Sub3 ใหม่จากน้อยไปมาก list[['11','80','79']]


# -------------Definition of Program--------------#

# ใช้งาน 1 สำหรับการหาโหนดข้างเคียงที่มีโหนดเหมือนกัน 2 โหนด
def Next_SubN2(Start, Compare):  # เอาเหมือนรอบๆ 2 โหนด

    Scycle_same2 = []
    Keep = []
    for h in Start:  # เอา Start แค่ตัวเดียว
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

# ใช้ 2 เอาไว้เปลี่ยนจาก [[],[],[]] -> [[...........]] ก้อนเป็นยาว ๆ
def Change_Shlist_TO_Llist(Sh_list):
    Result = []
    for i in Sh_list:
        Result += (i)
    return Result


# ใช้ 12, T1 มี 2 cycles
def Change_SetTolist(Start):  # ทำ set(['','',''],['','','']) เป็น list[[],[]]
    T1 = []
    for i in Start:
        T = list(i)
        T1.append(T)
    return T1

def Plus_ListToLost(Start, Plus):
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

def DiffDen(Next_SNodes2, Compare3, DD):
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
            plt.show()

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


# ใช้งาน 3
def Cut_Sub(Start, Compare):  # หา Sub ที่เหลือจากทั้งหมด

    Result = []  # กำหนด type ให้ตัว Return
    Keep = []
    Start_L = Change_Shlist_TO_Llist(Start)
    Start_S = set(Start_L)
    for h in Start_S:
        count = len(Compare)
        for i in range(count - 1):
            Next = Compare[i]
            Next_S = set(Next)
            a = Start_S & Next_S  # สมาชิกที่ซ้ำกัน
            if len(a) == 3:  # ไม่เอาที่ซ้ำกันหมด
                Keep.append(Next)
            else:
                if Next not in Result:
                    Result.append(Next)

        return Result  # CutSub = [['','',''],['','','']]


def Next_SN2(Start, Compare):
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
            if len(a) >= 1:
                Result.append(Next_L)
            else:
                Keep.append(Next_L)
        return Result  # List[['','',''],['','','']]


def draw_Cluster(Start, Compare):
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
            plt.show()
        for J in Compare:
            Start_LL = a + J
            count1 = len(Compare)
            for O in range(count1 - 1):
                Next_LL = Compare[O + 1]
                aa = Start_LL + Next_LL
                k.add_cycle(aa)
                draw_networkx(k, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
                plt.show()

            return

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
Next_SNodes2 = Next_SubN2(Sub3, Sub_cycle3_sort)  # list [set(['1','8','30']),...]#
print 'จำนวนไซเคิลข้างเคียงในรอบแรก =', len(Next_SNodes2)
print 'จำนวนไซเคิลที่เหลืออยํู =', len(Sub3) - len(Next_SNodes2)
L = Change_SetTolist(Next_SNodes2)
L1 = sorted(L)
D1 = DiffDen(L, L1, DD)

C2 = Cut_Sub(D1, Sub3)  # ตัดครัสเตอร์แรกออกจากกอง SUB ทั้งหมด
C2_sort = sorted(C2)
N2 = Next_SN2(C2, C2_sort)  # หาครัสเตอร์ใหม่
Draw2 = draw_Cluster(D1, N2)
P2 = Plus_ListToLost(D1, N2)  # ได้ก้อนครัสเตอร์ 1

C3 = Cut_Sub(P2, Sub3)  # ตัดครัสเตอร์แรกออกจากกอง SUB ทั้งหมด
C3_sort = sorted(C3)

D3 = DiffDen(C3, C3_sort, DD)
print 'a'




