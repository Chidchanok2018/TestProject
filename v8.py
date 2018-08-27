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


# -------------Definition of Program--------------#

# ใช้งาน 1 สำหรับการหาโหนดข้างเคียงที่มีโหนดเหมือนกัน 2 โหนด
def Next_SubN2(Start, Compare):  # เอาเหมือนรอบๆ 2 โหนด
    # Start ใส่ list[['65','79','24']], Next ใส่ list[['11','80','79']]
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

# ใช้งาน 2 สำหรับการคำนวน interintra โดยสามารถกำหนดค่า DD ได้
def interintra(Start, Compare, Dif_Den):  # Interintra 2 Sub เหมือนกันมากกว่า 2 โหนด
    # Start ใส่ list[set(['11','65','79']), Next ใส่ list[['11','80','79']]
    for o in Start:  # แต่ละตัวใน Start (ตัวตั้งต้น)
        Cluster = []
        Keep = []
        Result = []
        count = len(Start)
        Start_Sub = list(o)  # เปลี่ยน Start ให้เป็น list
        # Result.append(Start_Sub)
        for o1 in range(count-1):  # ไม่ลบ 1 เผื่อมีที่ Keep
            # print'-----------inter-intra----------------'
            # print'Round =', o1
            G = nx.Graph()
            if len(Cluster) >= 3:  # ถ้า Start_sub มากกว่าเท่ากับ 3 โหนด
                Start_Sub = a  # a คือที่รวมผลลัพท์เป็นก้อนยาวๆแล้ว[...........]
            if o1 == 0:
                Next_Sub = list(Compare[o1])
            if o1 > 0:
                Next_Sub = list(Compare[o1])  # เปลี่ยน Next ให้เป็น list
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

            if Dif_Den_N2 >= Dif_Den:  # กำหนดคุณภาพของ Dif เท่าเดิมแหละ
                Cluster = a
                Result.append(Next_Sub)
            else:
                Keep.append(Next_Sub)  # มี Sub อะไรที่เหลือบ้าง
        return Result

# ใช้ 3 ทำให้ [[],[],[]] -> [[...........]]
def Change_Shlist_TO_Llist(Sh_list):
    Result = []
    for i in Sh_list:
        Result += (i)
    return Result

# ใช้ 4 หา Cycles ข้างเคียงอีกครั้ง ใช้ก้อนยาวเปรียบเทียบก้อนสั้น ๆ
def Next_SubN21(Llist,Sub, Shlist):  # เอาอันที่เหมือนกันออกไป
    Result = []
    Keep = []
    Sub # list ของซับ 3 ทั้งหมด
    Shlist  # list เตรียมเอามาต่อเพิ่ม
    Start = Llist  # list ที่รวมเป็นก้อนยาวเอาไปเปรียบเทียบ คงที่
    count = len(Sub)
    for h in range(count - 1):
        Start = set(Llist)  # เปรียบเทียบต้องเป็น set
        if h == 0:
            Next = set(Sub[h])  # Sub ทั้งหมดก้อนที่ h
        if h > 0:
            Next = set(Sub[h])
        a = Start & Next
        if len(a) == 3:
            Keep.append(Next)
        else:
            if len(a) == 0:
                Result.append(Sub[h])
            else:
                Result.append(Sub[h])
    b = len(Result)
    return Result

# ใช้งาน 5 คำนวน Difference Density รอบที่ 2
def interintra21(Start, Compare, DD):  # list[[],[],[]]
    Start  # ก้อนสั้นของการรวมครัสเตอร์ก่อนหน้านี้ list[[],[],[]]
    Start1 = copy.deepcopy(Start)  # ไม่ยุ่งกับ input
    Compare  # ก้อนสั้นของซับไซเคิลข้างเคียงที่หามาได้ list[[],[],[]]
    Keep = []  # เก็ยซับที่ไม่ผ่านการคำนวน
    Result = copy.deepcopy(Start)  # เตรียมไว้เป็นผลลัพท์ตอนเอาออกไป list[[],[],[]]
    Result1 = Start1  # ใส่ค่าเก่าลงไปในก้อนก่อน ค่าเปลี่ยนแปลงได้

    count = len(Compare)  #
    for h in range(count - 1):
        G = nx.Graph()
        Start_L = Change_Shlist_TO_Llist(Start1)  # ทำให้ก้อนสั้นเป็นก้อนยาว
        # if len(Cluster) >= 3:  # ถ้า Start_sub มากกว่าเท่ากับ 3 โหนด
        #     Start_Sub = a  # a คือที่รวมผลลัพท์เป็นก้อนยาวๆแล้ว[...........]
        if h == 0:
            Next = Compare[h]  # List ก้อนสั้น
        if h > 0:
            Next = Compare[h]  # List ก้อนสั้น

        b = set(Start_L) & set(Next)
        G.add_cycle(Start_L)  # ต้อง Add แบบนี้เท่านั้นรูปจึงไม่เพี้ยน เพิ่มก้อนยาว
        G.add_cycle(Next)  # ต้อง Add แบบนี้เท่านั้นรูปจึงไม่เพี้ยน เพิ่มก้อนสั้น
        draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
        # plt.figure(1)
        plt.show()
        # มีโหนดเหมือนกัน มากกว่าเท่ากับ 2 โหนด
        if len(b) >= 2:
            Dif_Den_N2 = 0.00  # ให้หมดนี่เท่ากับ 0.00
            Dif_Den_N1 = 0.00
            Re_inter4 = 0.00
            Re_inter5 = 0.00
            Re_intra5 = 0.00
            Re_intra4 = 0.00

            # ตัวแปรที่รอการคำนวน
            Number_of_Edges_Out = 0.00  # จำนวนกิ่งภายนอกครัสเตอร์
            Number_of_Edes_All = float(len(G.edges))  # จำนวนกิ่งภายในครัสเตอร์
            N = float(len(G.nodes()))  # จำนวนโหนดทั้งหมด
            N_C = float(len(G.nodes()))    # จำนวนโหนดภายในครัสเตอร์
            # inter Cluster Density
            if (N_C * (N - N_C)) <= 0.00:  # ถ้าส่วนเป็น 0 ให้ inter-edges = 0
                interN4 = 0.00
                Re_inter4 = interN4
            elif Number_of_Edges_Out <= 0.00:  # ถ้าเศษเป็น 0 ให้ inter-edges = 0
                interN4 = 0.00
                Re_inter4 = interN4
            else:   # นอกนั้นคำนวนได้
                inter_1 = ((N_C * (N - N_C)))
                inter_2 = (Number_of_Edges_Out) / inter_1
                Re_inter4 = round(inter_2, 2)   # ให้เหลือทศนิยม 2 ตำแหน่ง
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

            # มีโหนดเหมือนกันน้อยกว่า 2 โหนด
            if len(b) < 2:
                Dif_Den_N2 = 0.00  # ให้อีกฝั่งเป็น 0
                Dif_Den_N1 = 0.00
                Re_inter4 = 0.00
                Re_inter5 = 0.00
                Re_intra5 = 0.00
                Re_intra4 = 0.00
                Dif_Den = 0.00

                # ตัวแปรรอการคำนวน
                Number_of_Edges_Out1 = 2.00
                Number_of_Edes_All1 = float(len(G.edges))
                N1 = float(len(G.nodes))
                N_C1 = float(len(G.nodes))
                # inter cluster density
                if (N_C1 * (N1 - N_C1)) == 0.00:
                    inter5 = 0.00
                    Re_inter5 = inter5
                elif Number_of_Edges_Out1 <= 0.00:
                    inter5 = 0.00
                    Re_inter5 = inter5
                else:
                    inter_1X = ((N_C1 * (N1 - N_C1)))
                    inter_2X = (Number_of_Edges_Out1) / inter_1X
                    Re_inter5 = round(inter_2X, 2)
                # intra cluster density
                if (N_C1 * (N1 - 1) / 2) <= 0.00:
                    intra5 = 0.00
                    Re_intra5 = intra5
                elif Number_of_Edes_All1 <= 0.00:
                    intra5 = 0.00
                    Re_intra5 = intra5
                else:
                    intra_1X = (N_C1 * (N1 - 1) / 2)
                    intra_2X = (Number_of_Edes_All1) / (N_C1 * (N_C1 - 1) / 2)
                    Re_intra5 = round(intra_2X, 2)
                print 'Re_intra', " %+2.2f" % Re_intra5
                Dif_Den_N1 = Re_intra5 - Re_inter5
            Dif_Den = Dif_Den_N2 + Dif_Den_N1  # ได้ทั้ง 2 ตัว

            if Dif_Den >= DD:  # กำหนดคุณภาพของ Dif
                Start_L.append(Next_L)  # เอาไปเพิ่มในรอบต่อไป กราฟเพี้ยนอีก
                Result.append(Next)  # เพิ่มในผลที่จะออกไปจะได้เป็นก้อน
            else:
                Keep.append(Next)
    return Result


print'------เริ่มทำการหาครัสเตอร์---Snow ball 2---------------'
print'จำนวนโหนดทั้งหมดในกราฟ ', Number_of_nodes, 'โหนด'
print'จำนวน Sub3 ทั้งหมด', len(Sub3), 'โหนด'
Node_Graph = [i for i in G.nodes]  # ก้อนยาวๆ
# print'Node_Graph =', Node_Graph
Edges_Graph = [i for i in G.edges]  # ก้อนสั้นๆ
# print'Edges_Graph =', Edges_Graph

# --------------------------------------------------------#
# หา cycles ข้างเคียงที่มีโหนดเหมือนกันจำนวน 2 โหนด Sub3=list[['23','8','30']]
N_C2 = Next_SubN2(Sub3, Sub_cycle3_sort)  # list [set(['1','8','30']),...]#
print 'จำนวนไซเคิลข้างเคียงในรอบแรก =', len(N_C2)
print 'จำนวนไซเคิลที่เหลืออยํู =', len(Sub3) - len(N_C2)
N_C2_S = sorted(N_C2)
# ***ถ้า N_C2 == list[set()] ให้ จบการทำงาน
# นำมาคำนวนหาค่า Difference Density C2
N3_C2_I = interintra(N_C2, N_C2_S, 0.60)  # tuple [[Subชุดแรกที่ผ่านการต่อไซเคิล]]
N3_C2_I = list(N3_C2_I) # ทำให้เป็น list [[],[],[]]
print 'จำนวนไซเคิลที่ผ่านการคำนวน intra-inter =', len(N3_C2_I)
print 'จำนวนไซเคิลที่เหลืออยู่ =', len(Sub3) - len(N3_C2_I)
#   *** ถ้า N_C2_I == tuple([]) ให้จบการทำงาน

# # ทำก้อนๆให้เป็นก้อนยาวๆ [[],[],[]] -> [[.......]] เป็นก้อนยาว ๆ ซ้ำ ๆ นำไปคำนวนได้
N_C2_I_Llist = Change_Shlist_TO_Llist(N3_C2_I)  # list[[......]]
# K = nx.Graph()
# K.add_cycle(N_C2_I_Llist)
# draw_networkx(K, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
# plt.figure(1)
# plt.show()

# เอาก้อนที่ได้มาไปหักลบกับ Sub3 #
# # หาไซเคิลรอบ ๆ อีกครั้ง เอาก้อนๆ list มาด้วยเพื่อต่อ C21
# # ต้องใช้คนละ def กับรอบแรกเพราะตัวตั้งต้นเปลี่ยนไป
N_C21 = Next_SubN21(N_C2_I_Llist, Sub3, N3_C2_I)  # list[[.....]] -> list[[],[],[]]
print 'จำนวนไซเคิลข้างเคียงรอบที่ 2 =', len(N_C21)
print 'จำนวนไซเคิลที่เหลืออยู่ =', len(Sub3) - len(N_C21)
# *** ถ้า N_C21 == list[[]] ให้ข้ามไปที่การต่อกิ่ง
# นำไซเคิลที่หาได้มาคำนวน Difference Density C21
# # ต้องใช้คนละ def กับรอบแรกเพราะตัวตั้งต้นเปลี่ยนไป และต้องเอาก้อนยาวๆ มาด้วย N_C2_I_Llist
N_C21_Sort = sorted(N_C21)
# # # ก้อนสั้นของซับข้างเคียงที่หามาได้, ก้อนยาวที่จะเอามาเปรียบเทียบ, ก้อนสั้นที่จะเอามาต่อเป็นกราฟ, ค่า DD
N_C21_I = interintra21(N3_C2_I, N_C21, 0.30)
print 'จำนวนไซเคิลที่ผ่านการคำนวน intra-inter =', len(N_C21_I)
