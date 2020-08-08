from collections import defaultdict

class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def DFSUtil(self, temp, v, visited):

        visited[v] = True
        temp.append(v)

        for i in self.adj[v]:
            if visited[i] == False:

                temp =  self.DFSUtil(temp, i, visited)
        return temp
    
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


m, n = map(int, input().split())
g = Graph(m+1)
for i in range(n):
    u, v = map(int, input().split())
    g.addEdge(u, v)

print(len(g.connectedComponents()) - 1)

