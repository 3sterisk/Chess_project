from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end =' ')
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)
    
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

g  = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(5, 2)
g.addEdge(2, 9)
g.addEdge(4, 3)
g.addEdge(2, 4)
g.addEdge(3, 5)
g.DFS(2)