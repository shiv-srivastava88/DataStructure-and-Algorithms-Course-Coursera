from collections import defaultdict 
import sys
sys.setrecursionlimit(200000)

class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = defaultdict(list) 
   

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    
    def DFSUtil(self,v,visited): 
        
        visited[v]= True
        
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited) 
  
  
    def fillOrder(self,v,visited, stack): 
       
        visited[v]= True
 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack = stack.append(v) 
      
  
    def getTranspose(self): 
        g = Graph(self.V) 
  
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g 
  

    def printSCCs(self): 
          
        stack = [] 
        count = 0

        visited =[False]*(self.V+1) 

        for i in range(1, self.V+1): 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 

        gr = self.getTranspose() 
        
        visited =[False]*(self.V+1) 
  
        while stack: 
            i = stack.pop() 
            if visited[i]==False: 
                gr.DFSUtil(i, visited) 
                count += 1
                
        return count

m, n = map(int, input().split())
g = Graph(m)
for i in range(n):
    u, v = map(int, input().split())
    g.addEdge(u, v)
print(g.printSCCs())
