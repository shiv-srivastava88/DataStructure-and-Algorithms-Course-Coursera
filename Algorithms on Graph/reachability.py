#Uses python3
from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isReachable(self, s, d):
        visited = [0] * (self.V)

        queue = []
        queue.append(s)
        visited[s] = 1

        while queue:
            
            n = queue.pop(0)

            if n == d:
                return 1
            
            for i in self.graph[n]:

                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
        return 0

m, n = map(int, input().split())
g = Graph(m+1)

for i in range(n):
    u, v = map(int, input().split())
    g.addEdge(u, v)
    g.addEdge(v, u)


a, b = map(int, input().split())

print(g.isReachable(a, b))




