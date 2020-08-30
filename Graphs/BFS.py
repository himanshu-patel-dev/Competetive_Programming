# Directed edge
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    # undirected graph
    def add_edge(self,src,dst):
        self.graph[src].append(dst)
        self.graph[dst].append(src)

    def BFS(self,start):
        # Mark all vertices as not visited
        visited = [False]* len(self.graph)

        queue = deque()
        # putting start vertex in queue and making it visited
        queue.append(start) 
        visited[start] = True

        # until q not empty
        while queue:
            s = queue.popleft()
            print(s,end=' ')

            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(2,0)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,3)    

    g.BFS(0)