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

# ใช้ 2 เอาไว้เปลี่ยนจาก [[],[],[]] -> [[...........]] ก้อนเป็นยาว ๆ
def Change_Shlist_TO_Llist(Sh_list):
    Result = []
    for i in Sh_list:
        Result += (i)
    return Result

# ใช้งาน 2 ใช้ซับข้างเคียงในการคำนวน Difference Density
def Difference_Density(Start, Compare, DD):  # (Next_SNodes2, Next_SNodes2_Sort, DD)
    Result = []  # ใช้ append เพิ่ม
    # เริ่มต้นให้ตัวแปรเป็น list, เปรียบเทียบตัวแปรเป็น set, เพิ่มตัว Start เป็น list
    Keep = []
    G = nx.Graph()
    Start_L = []
    for item3 in Start:
        count = len(Compare) - 1
        Start_L = list(item3)
        G.add_cycle(Start_L)
        for i in range(count):
            Next_L = list(Compare[i+1])
            Result.append(Next_L)
            Result.append(Start_L)
            G.add_cycle(Next_L)
            draw_networkx(G, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
            plt.show()


    return Result  # ผลลัพทธ์ออกมา [['','',''],['','','']]





print'------เริ่มทำการหาครัสเตอร์---Snow ball 2---------------'
print'จำนวนโหนดทั้งหมดในกราฟ ', Number_of_nodes, 'โหนด'
print'จำนวน Sub3 ทั้งหมด', len(Sub3), 'โหนด'
Node_Graph = [i for i in G.nodes]  # ก้อนยาวๆ
# print'Node_Graph =', Node_Graph
Edges_Graph = [i for i in G.edges]  # ก้อนสั้นๆ
# print'Edges_Graph =', Edges_Graph
DD = float(0.70)

# --------------------------------------------------------#
# หา cycles ข้างเคียงที่มีโหนดเหมือนกันจำนวน 2 โหนด Sub3=list[['23','8','30']]
Next_SNodes2 = Next_SubN2(Sub3, Sub_cycle3_sort)  # list [set(['1','8','30']),...]#
print 'จำนวนไซเคิลข้างเคียงในรอบแรก =', len(Next_SNodes2)
print 'จำนวนไซเคิลที่เหลืออยํู =', len(Sub3) - len(Next_SNodes2)
Next_SNodes2_Sort = sorted(Next_SNodes2)
Cal_Difference1 = Difference_Density(Next_SNodes2, Next_SNodes2_Sort, DD)
print 'จำนวนไซเคิลที่ผ่านการคำนวน intra-inter =', len(Cal_Difference1)
print 'จำนวนไซเคิลที่เหลืออยู่ =', len(Sub3) - len(Cal_Difference1)


# Result = []  # ไว้ใส่ผลลัพท์
    # Start1 = copy.deepcopy(Start)  # ตั้งต้นตัวเดียว
    # count = len(Compare)
    # Keep = []
    # Start_L = []
    # for i in Start1:  # set
    #     Start_L = list(i)
    #     Result.append(Start_L)
    #     for h in range(count - 1):  # เอารอบของ Compare
    #
    #         if len(Result) > 1:
    #             Start_L = Change_Shlist_TO_Llist(Result)
    #         if h == 0:
    #             Next_L = list(Compare[h])  # set ก้อนสั้น
    #         if h > 0:
    #             Next_L = list(Compare[h])  # set ก้อนสั้น
    #         # c = [set(['5','9','16']),set(['10','9','16'])]
    #         # Start_S.update(c) # set(['1','5','16','9','8','30'])
    #         # K.add_cycle(c)
    #         # draw_networkx(K, edge_color='b')
    #         # plt.show()
    #
    #         a = i & set(Next_L)  # ต่างกันเท่าไร
    #         K = nx.Graph()
    #         K.add_cycle(Start_L)  # เพิ่มไซเคิล List Start_S
    #         K.add_cycle(Next_L)  #
    #         draw_networkx(K, edge_color='b')  # ภาพกราฟค่อยๆเพิ่มขึ้น
    #         plt.show()
    #         # มีโหนดเหมือนกัน มากกว่าเท่ากับ 2 โหนด
    #         if len(a) >= 2:
    #             Dif_Den_N2 = 0.00  # ให้หมดนี่เท่ากับ 0.00
    #             Dif_Den_N1 = 0.00
    #             Re_inter4 = 0.00
    #             Re_inter5 = 0.00
    #             Re_intra5 = 0.00
    #             Re_intra4 = 0.00
    #
    #             # ตัวแปรที่รอการคำนวน
    #             Number_of_Edges_Out = 0.00  # จำนวนกิ่งภายนอกครัสเตอร์
    #             Number_of_Edes_All = float(len(K.edges))  # จำนวนกิ่งภายในครัสเตอร์
    #             N = float(len(K.nodes))  # จำนวนโหนดทั้งหมด
    #             N_C = float(len(K.nodes))  # จำนวนโหนดภายในครัสเตอร์
    #             # inter Cluster Density
    #             if (N_C * (N - N_C)) <= 0.00:  # ถ้าส่วนเป็น 0 ให้ inter-edges = 0
    #                 interN4 = 0.00
    #                 Re_inter4 = interN4
    #             elif Number_of_Edges_Out <= 0.00:  # ถ้าเศษเป็น 0 ให้ inter-edges = 0
    #                 interN4 = 0.00
    #                 Re_inter4 = interN4
    #             else:  # นอกนั้นคำนวนได้
    #                 inter_1 = ((N_C * (N - N_C)))
    #                 inter_2 = (Number_of_Edges_Out) / inter_1
    #                 Re_inter4 = round(inter_2, 2)  # ให้เหลือทศนิยม 2 ตำแหน่ง
    #             # intra cluster Density
    #             if (N_C * (N - 1) / 2) <= 0.00:
    #                 intra4 = 0.00
    #                 Re_intra4 = intra4
    #             elif Number_of_Edes_All <= 0.00:
    #                 intra4 = 0.00
    #                 Re_intra4 = intra4
    #             else:
    #                 intra_1 = (N_C * (N - 1.00) / 2.00)
    #                 intra_2 = (Number_of_Edes_All) / (N_C * (N_C - 1) / 2)
    #                 Re_intra4 = round(intra_2, 2)
    #             Dif_Den_N2 = Re_intra4 - Re_inter4
    #
    #         if Dif_Den_N2 >= DD:  # กำหนดคุณภาพของ Dif เท่าเดิมแหละ
    #             if Next_L not in Result:
    #                 Start_L.append(Next_L)
    #                 Result += Next_L
    #         else:
    #             Keep.append(Next_L)  # มี Sub อะไรที่เหลือบ้าง
