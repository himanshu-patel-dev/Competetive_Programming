"""
Using bellman-ford we can get shortest path in (V*E)
Using Dijkstra we can get shortest path in O(E + VlogV)
But here using BSF we get path in time O(V+E) 
"""
from collections import defaultdict, deque
class Graph:
	def __init__(self):
		self.g = defaultdict(list)
		self.v = 0

	# considering undirectional graph
	def addEdge(self,u,v):
		self.g[u].append(v)
		self.g[v].append(u)

	def BFS(self,src,dest,precedor,distance):
		visited = [False]*self.v
		q = deque()

		visited[src] = True
		q.append(src)

		while q:
			node = q.popleft()

			for v in self.g[node]:
				if not visited[v]:
					visited[v] = True
					q.append(v)
					# set node as precedor of v
					precedor[v] = node
					# set distance of v from source
					distance[v] = distance[node] + 1
					# as soon dest is encountered return True
					if v == dest:
						return True
		return False

	def shortest_path(self,src,dest):
		precedor = [-1]*self.v
		distance = [0]*self.v
		# run BFS to find dest
		found = self.BFS(src,dest,precedor,distance)
		if not found:
			print("Destination is either not present or unreachable from source")
			return

		path = []
		current = dest
		while current!= -1:
			path.append(current)
			current = precedor[current]
		path = path[::-1]

		print("Path : ",path)
		print("Path Length: ",distance[dest])

if __name__ == "__main__":
	
	# instance of graph with num of verices declared
	g = Graph()
	g.v = 8

	g.addEdge(0,1)
	g.addEdge(0,3)
	g.addEdge(1,2)
	g.addEdge(7,3)
	g.addEdge(7,4)
	g.addEdge(4,3)
	g.addEdge(7,3)
	g.addEdge(4,6)
	g.addEdge(0,5)

	g.shortest_path(0,7)
	