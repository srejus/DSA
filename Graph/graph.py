class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        
    def add_edge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
    
    def remove_vertex(self,vertex):
        if vertex in self.graph:
            for adj in self.graph[vertex]:
                self.graph[adj].remove(vertex)
            
            del self.graph[vertex]
        
    def remove_edge(self,v1,v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)
        
    def dfs(self,start,visited=None):
        if not visited:
            visited = set()
        
        visited.add(start)
        print(start,end=' ')
        for next_vertex in self.graph[start]:
            if next_vertex not in visited:
                self.dfs(next_vertex,visited)
            
    def bfs(self,start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            vertex = queue.pop(0)
            print(vertex,end=' ')
            for next_vertex in self.graph[vertex]:
                if next_vertex not in visited:
                    visited.add(next_vertex)
                    queue.append(next_vertex)


g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print("DFS:")
g.dfs(0)
print("\nBFS:")
g.bfs(0)