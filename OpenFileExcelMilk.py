from networkx import nx
import matplotlib.pyplot as plt
import pandas as pd
G = nx.Graph()
def ReadFileExcel(FileName):
    df = pd.read_excel(FileName)
    return df

def DataFileToGraph(DataFile):
    MaCo1 = 'Name'
    MaCo2 = 'Link'
    i = 0
    G = nx.Graph()
    for v in DataFile[MaCo1].values:
        L = DataFile[MaCo2][i]
        G.add_edge(str(v),str(L))
        i = i + 1
    return G

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

#def Sub_Cycles_ToCluster (cluster,cutcluster,):
#    set3 = 

if __name__ == "__main__":
    DataFile = ReadFileExcel('C:\Users\Kmutt_Wan\PycharmProjects\Sample1.xls')
    G = DataFileToGraph(DataFile)
    #GraphMe = nx.draw(G, edge_color='b', with_labels=True, edge_label=True)
    cycles = [[node] + path for node in G for path in dfs(G, node, node)]
    Result_dfs = dfs(G,node,node)
    print('All cycles =',len(cycles))
    list3 = []
    for node in cycles:
        if len(node) - 1 == 3:
            list3.append(node)
    tuple3 = tuple(list3)  #
    set3 = {frozenset(x) for x in tuple3}
    print('Sub cycles 3 node =',len(set3),set3)
    Graph_cycles = nx.draw_networkx(set3)
    plt.show()

#def SubcycleGraph(Sub_Cycle):
#    for n in Sub_Cycle.node:
#        count = len(n) - 1
#        for i in range(count):
#            Sub_Cycle.add_edge(n[i], n[i + 1])
#           if i == n - 1:
#               Sub_Cycle.add_edge(n[i + 1], n[0])










