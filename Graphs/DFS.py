from collections import defaultdict
class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    # considering undirectional graph
    def addEdge(self,u,v):
        self.g[u].append(v)
        self.g[v].append(u)

    # DFS when vertex 'node' to start with is given of graph is not forest
    def DFS_simple(self,node,visited):
        """ T = O(V + E) """
        # dfs is called only on unvisited node so make them visited
        visited[node] = True            
        print(node, end=' ')
        for n in self.g[node]:
            if not visited[n]:
                self.DFS_simple(n,visited)

    # work even on forest as we check every vertex
    def DFS_forest(self):
        """ T = O(V + E) """
        v = len(self.g)     # getting no of vertices
        visited = [False]*v
        for node in range(v):
            if not visited[node]:
                self.DFS_simple(node,visited)

if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0,1)
    graph.addEdge(0,2)
    graph.addEdge(2,1)
    graph.addEdge(3,1)
    graph.addEdge(2,7)

    graph.addEdge(5,4)
    graph.addEdge(4,6)
    
    # to display the adjacency list
    # for v in range(8): 
    #     print(graph.g[v])
    

    print("DFS Forest: ")
    graph.DFS_forest()
    print('\n')

    print("DFS Simple")
    visited = [False]*len(graph.g)
    graph.DFS_simple(0,visited)
    print('\n')
