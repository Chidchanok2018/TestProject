import networkx as nx
import matplotlib.pyplot as plt
import sys
import math
import operator
import random as ran
import numpy as np
import pandas as pd
#importจากไฟล์ as คือชื่อย่อ

#ข้อมูลอินพุทของแก
list3 =[]
list3.append(['A', 'B', 'C']) #.append ใช้ในการเพิ่มข้อมูลเข้าลิส เพิ่มเติม เสริจ์ python list
list3.append(['A', 'B', 'D']) #expend (อะไรนี่แหละ) คล้ายๆ append แต่กรณีตัวอักษรหลายๆตัว มันจะ sprit เอาทีละตัว เหมือนพวก char เลยอะ
list3.append(['A', 'B', 'E']) #ลองลบตรงนี้ดูสิ แล้วไป ลบ if ล่าง
list3.append(['A', 'C', 'D']) #ลองลบตรงนี้ดูสิ แล้วไป ลบ if ล่าง
##จบ ข้อมูลอินพุทของแก

#ไม่ควรแก้ตรงนี้

G=nx.Graph() # กำหนดให้ G คือกราฟ

for item3 in list3: #เอา item3 จาก list3 มาใช้ทีละตัว
    count = len(item3)-1 #len = เช็คขนาด ที่ต้อง -1 เพราะ ถ้าไม่ -1 จะทำให้ ตรง item3[i+1] มันหาค่าไม่ได้ เพราะเกินจาก index ของ list >> ไม่มีค่า item3 ที่ index i +1 สมมติ ลิสมีค่า 2 ตัว จะมี index = 0,1 เท่านั้น แต่ถ้าไม่ -1 ออก จะทำให้มีการเรียกที่ index = 2 ทำให้ error
    for i in range(count):#range คือ อันดับ ถ้า count = 3 อันดับ คือ 0 1 2 หรือ 1 2 3 นี่แหละ ลองหารายละเอียดดูนะ กูลืมค้าบ
        G.add_edge(item3[i], item3[i+1]) # add_ege คือการเพิ่ม edge ให้ โหนด 2 โหนด (สามารถใส่น้ำหนักได้ด้วยนะ แต่คือเราไม่ใช้กับงานเรานาจา)
        #if นี้แพคคู่กับ for i เอาไปด้วย ไม่งั้น ไม่กลม (ลองลบละเล่นกะดาต้าน้อยๆก็ได้ จะได้เห็นชัด)
        if i == count-1: #กรณีเป็นตัวสุดท้ายของลิส มันจะไม่รู้จักโหนดตัวแรก (ไม่มี edge ถึงกัน เลยต้องเพิ่ม ไม่งั้นจะไม่เป็น cricle)
            G.add_edge(item3[i+1], item3[0])# add_ege คือการเพิ่ม edge ให้ โหนด 2 โหนด (สามารถใส่น้ำหนักได้ด้วยนะ แต่คือเราไม่ใช้กับงานเรานาจา)

#จบ ไม่ควรแก้

#แสดงผล
nx.draw(G, edge_color='b', with_labels=True, edge_labels=True) # แสดงผล edge_color แปลว่า สีของเอดจ์ ลองเปลี่ยน พวก True เป็น False ทีละครั้งสิ ลองเล่นดู
plt.savefig("AAA") #save fig ชื่ออะไรดีจ๊ะ
plt.show() #show แปลว่า โชว์
#จบแสดงผล

