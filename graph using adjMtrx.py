class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class Stack:
   def __init__(self):
      self.stack = []
   def push(self,data):
      self.stack.append(data)
   def pop(self):
      return self.stack.pop()
   def isEmpty(self):
      return len(self.stack)==0

class Graph:    #using Adjacency Matrix             paras vertices E-edges(from,to,weight)
    def __init__(self,V,E): #v-vertices E-edges
        self.graph = []
        self.data = V
        for i in V:
            k = []
            for i in V:
                k.append(0)
            self.graph.append(k)

        for i in E:
            self.graph[i[0]-1][i[1]-1] = i[2]

    def printGraph(self):
        for i in self.graph:
            print(i)

    def printData(self):
        print self.data

    def isEdg(self,x,y): #checks weather there's an edge from x to y
        return self.graph[x-1][y-1] > 0

    def Adj(self,i):   #graph , index returns all adjacent vertexes as a list
        adjLst = []
        for k in range (len(self.graph[i])):
            if (self.graph[i][k] == 1):
                adjLst.append(k)
        return adjLst

    def inDegree(self): #para - graph
        inDeg = []
        for i in range(len(self.graph)):
            count = 0
            for k in self.graph:
                if k[i] == 1:
                    count += 1
            inDeg.append(count)
        return inDeg

    def outDegree(self): #graph
        outDeg = []
        for i in range(len(self.graph)):
            outDeg.append(len(self.Adj(i)))
        return outDeg

    def BFS(self,s):
        c = []      #colour
        d = []      #distance
        p = []      #parent predecessor
        s = s - 1
        for u in range (len(self.graph)):
            c.append("WHITE")   #colour all white   Not discovered
            d.append(-1)        #distance infinite
            p.append(None)      #no parent

        c[s] = "GRAY"   #Discovered
        d[s] = 0
        p[s] = None

        Q = Queue()
        Q.enqueue(s)

        bfs = [] #stores bfs

        while not Q.isEmpty():
            u = Q.dequeue()
            for v in self.Adj(u):
                if (c[v] == "WHITE"):
                    c[v] = "GRAY"
                    d[v] = d[u] + 1
                    p[v] = u
                    Q.enqueue(v)
            c[u] = "BLACK"  #done with it
            bfs.append(u+1)

        print(d)
        return bfs

    def isPath(self,x,y):   #checks weather there's a path from x to y
        return (y) in self.BFS(x)

    def isSink(self,s):
        for i in range(len(self.graph)):
            if self.graph[s-1][i] > 0:
                return False
        for i in range(len(self.graph)):
            if (self.graph[i][s-1]==0) and (i != (s-1)):
                return False
        return True

    def BIPARTITE(self,s):
        G = self.graph
        s -= 1

        c = []  #colour
        d = []  #distance
        p = []  #partition

        for i in range(len(G)):
            c.append("WHITE")   #Not discovered
            d.append(-1)        #-1 denotes infinity
            p.append(0)

        c[s] = "GRAY"   #discoverd
        p[s] = 1
        d[s] = 0

        Q = Queue()
        Q.enqueue(s)

        while not Q.isEmpty():
            u = Q.dequeue()

            for v in self.Adj(u):
                if p[u] == p[v]:
                    return False
                else:
                    if c[v] == "WHITE":
                        c[v] = "GRAY"
                        d[v] = d[u]+1
                        p[v] = 3 - p[u]
                        Q.enqueue(v)
            c[u] = "BLACK"
        return True

    def DFS_rec(self):

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

            for v in self.Adj(u):
                if c[v] == "WHITE":
                    p[v] = u
                    DFS_visit(v)

            c[u] = "BLACK"
            f[u] = t = t+1

        DFS(self.graph)




        print(self.data)
        print(d)
        print(f)


v = [0,1,2,3,4,5,6]
e = [[1,2,1],[1,4,1],
     [2,5,1],
     [3,5,1],
     [3,6,1],
     [4,2,1],
     [5,4,1]
     ]
mat  = [[0,1,0,0,0,1,0],
        [0,0,1,0,0,1,0],
        [0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1],
        [0,0,0,1,1,0,0],]
g = Graph(v,e)
g.graph = mat
print(g.BFS(4))