from collections import defaultdict
class Graph:
    
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCyclicUtil(self, v, visited, trace):
        
        visited[v] = True
        trace[v] = True
        
        for i in self.graph[v]:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, trace) == 1:
                    return 1
            elif trace[i] == True:
                return 1
        trace[v] = False
        return 0
                
                
    def isCyclic(self):
        
        visited = [False]*(self.V + 1)
        trace = [False]*(self.V + 1)
        
        for i in range(1, self.V+1):
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, trace) == 1:
                    return 1
        return 0


        
m, n = map(int, input().split())
g = Graph(m)
for i in range(n):
    u, v = map(int, input().split())
    g.addEdge(u, v)

print(g.isCyclic())