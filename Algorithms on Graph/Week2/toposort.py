from collections import defaultdict
class Graph:
    
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def topologicalSortUtil(self, v, visited, stack):
        
        visited[v] = True
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
                
        stack.insert(0, v)
        
    def topologicalSort(self):
        
        visited = [False]*(self.V+1)
        stack = []
        
        for i in range(1, self.V+1):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
                
        return stack
        
        

m, n = map(int, input().split())
g = Graph(m)
for i in range(n):
    u, v = map(int, input().split())
    g.addEdge(u, v)
print(*(g.topologicalSort()))
