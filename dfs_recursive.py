def Adj(graph,i):   #graph , index returns all adjacent vertexes as a list
    adjLst = []
    for k in range (len(graph[i])):
        if (graph[i][k] == 1):
            adjLst.append(k)
    return adjLst


def DFS(graph):

    c = []  #color
    p = []  #predecessor
    d = [] #discover time array
    f = [] #finished time array
    t = 0   #timestamp

    def DFS(G):
        for u in range(len(G)):
            c.append("WHITE")
            p.append(None)
            d.append(-1)
            f.append(-1)

        global t
        t = 0

        for u in range(len(G)):
            if c[u] == "WHITE":
                DFS_visit(u)

    def DFS_visit(u):
        global t

        c[u] = "GRAY"   #vertex u has been discovered
        d[u] = t = t+1

        for v in Adj(graph,u):
            if c[v] == "WHITE":
                p[v] = u
                DFS_visit(v)

        c[u] = "BLACK"
        f[u] = t = t+1

    DFS(graph)

    print(d)
    print(f)


mat = [[0,1,0,1,0,0],
       [0,0,0,0,1,0],
       [0,0,0,0,1,1],
       [0,1,0,0,0,0],
       [0,0,0,1,0,0],
       [0,0,0,0,0,0]]

DFS(mat)