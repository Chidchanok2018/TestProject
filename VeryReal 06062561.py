from networkx import nx
import matplotlib.pyplot as plt

fh = open("C:\Users\Kmutt_Wan\PycharmProjects\YeastEx.txt","r")
#print file.read(fh)

G = nx.read_adjlist(fh)
#nx.draw_networkx(G,edge_color='r',with_labels=True,edge_label=True)
#plt.savefig("AA.png")
plt.show()


Mdegree = sorted([d for n, d in G.degree()], reverse=True)
          #Leanglumdub([won G.degree moveto d],krubdan)
MDegree = max(Mdegree)#value maksud
#print ('Max Degree = ',MDegree)

DGee = G.degree()
#print (DGee)
MaxDegree = max(DGee)
print (MaxDegree)

Degrees = [val for (node,val)in G.degree()]#take degree from set(node,degree)
#print (Degrees)


