from collections import defaultdict
class Graph:
	def __init__(self,v):
		self.v = v
		self.graph = defaultdict(list)
 
	def addEdge(self,u,v): 
		# add an edge to undirected graph
		self.graph[u].append(v) 
		self.graph[v].append(u) 
		

	def DFS(self,source,visited,parent):
		# a usual DFS function
		visited[source] = True

		for node in self.graph[source]:
			# if neighbour is already visited then its a cycle
			if node == parent:
				continue
			elif visited[node]:
				return True
			else:
			# if neighbour is not visited visit them first
				self.DFS(node,visited,node)
		# if leaf is reached then no cycle reaturn false from this node
		return False

	def isCycle(self):
		visited = [False]*self.v
		cycle = False

		for node in range(self.v):
			if not visited[node]:
				if self.DFS(node,visited,-1):
					cycle = True
					break
		if cycle:
			print("Cycle Present")
		else:
			print("No Cycle")

if __name__ == "__main__":
	g = Graph(5) 
	g.addEdge(1, 0) 
	g.addEdge(0, 2) 
	g.addEdge(2, 1) 
	g.addEdge(0, 3) 
	g.addEdge(3, 4) 

	g.isCycle()

	print('')

	g = Graph(5) 
	g.addEdge(0, 1) 
	g.addEdge(0, 2) 
	g.addEdge(0, 3) 
	g.addEdge(0, 4) 

	g.isCycle()