# Directed edge
from collections import defaultdict

class Graph:
	def __init__(self,v):
		self.v = v
		self.graph = defaultdict(list)

	def addEdge(self,src,dst):
		self.graph[src].append(dst)
		self.graph[dst].append(src)

	def DFS(self,source,visited):
		# a usual DFS function
		visited[source] = True

		for node in self.graph[source]:
			if not visited[node]:
				self.DFS(node,visited)

	def isConnected(self):
		# find any vertex with at least one edge 
		# stop as soon we get one
		for v in range(self.v):
			if len(self.graph[v]) > 0:
				break

		# if its the last vertex means no previous vertex have a 
		# link neither do v-1 vertex have link to any other vertex
		# then return True to show it a euler graph
		if v == self.v-1:
			return True

		# make a DFS traversal so that all nodes in a cluster get visited
		visited = [False]*self.v
		self.DFS(v,visited)

		# checking if there is any node node not in the cluster and have 
		# non zero degree
		for v in range(self.v):
			if not visited[v] and len(self.graph[v]) > 0:
				return False
		return True


	def Euler(self):
		# if graph is not a connected graph (except isolated vertices)
		# then it can not be euler graph
		if not self.isConnected():
			return 0

		odd_degree_vertex = 0
		for node in range(self.v):
			if len(self.graph[node])%2:
				odd_degree_vertex += 1

		if odd_degree_vertex == 0:			# number of odd vertex is zero it a euler cycle
			return 2
		elif odd_degree_vertex == 2:		# number of odd vertex is 2 then its a euler path
			return 1
		else:								# not a euler graph
			return 0


	def test(self): 
		result = self.Euler() 
		if result == 0: 
			print("graph is not Eulerian")
		elif result ==1 : 
			print("graph has a Euler path")
		else: 
			print("graph has a Euler cycle")

if __name__ == "__main__":
	g1 = Graph(5); 
	g1.addEdge(1, 0) 
	g1.addEdge(0, 2) 
	g1.addEdge(2, 1) 
	g1.addEdge(0, 3) 
	g1.addEdge(3, 4) 
	g1.test() 
	
	g2 = Graph(5) 
	g2.addEdge(1, 0) 
	g2.addEdge(0, 2) 
	g2.addEdge(2, 1) 
	g2.addEdge(0, 3) 
	g2.addEdge(3, 4) 
	g2.addEdge(4, 0) 
	g2.test(); 
	
	g3 = Graph(5) 
	g3.addEdge(1, 0) 
	g3.addEdge(0, 2) 
	g3.addEdge(2, 1) 
	g3.addEdge(0, 3) 
	g3.addEdge(3, 4) 
	g3.addEdge(1, 3) 
	g3.test() 
	
	# a graph with 3 vertices 
	# connected in the form of cycle 
	g4 = Graph(3) 
	g4.addEdge(0, 1) 
	g4.addEdge(1, 2) 
	g4.addEdge(2, 0) 
	g4.test() 
	
	# a graph with all veritces 
	# with zero degree 
	g5 = Graph(3) 
	g5.test() 
	