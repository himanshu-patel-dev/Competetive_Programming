from collections import defaultdict
class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    # considering undirectional graph
    def addEdge(self,u,v):
        self.g[u].append(v)
        self.g[v].append(u)

    # DFS when node to start with is given of graph is not forest
    def DFS_simple(self,node,visited):
        visited[node] = True            # dfs is called only on unvisited node so make them visited
        print(node, end=' ')
        for n in self.g[node]:
            if visited[n] == False:
                self.DFS_simple(n,visited)

    # work even on forest as we check every vertex
    def DFS_forest(self):
        v = len(self.g)     # getting no of vertices
        visited = [False]*v
        for node in range(v):
            if visited[node] == False:
                self.DFS_simple(node,visited)


graph = Graph()
graph.addEdge(0, 1) 
graph.addEdge(0, 2) 
graph.addEdge(1, 2) 
graph.addEdge(2, 0) 
graph.addEdge(2, 3) 
graph.addEdge(3, 3) 

print("DFS Forest: ")
graph.DFS_forest()
print('\n')

print("DFS Simple")
visited = [False]*len(graph.g)
graph.DFS_simple(0,visited)
print('\n')
