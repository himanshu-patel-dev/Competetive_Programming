# Directed edge
from collections import defaultdict

class Graph:
	def __init__(self,v):
		self.v = v
		self.graph = defaultdict(list)
		# variable to record time
		self.Time = 0
	
	# undirected graph
	def addEdge(self,src,dst):
		self.graph[src].append(dst)
		self.graph[dst].append(src)

	def Bridges(self,source):
		# mark current node visited
		self.visited[source] = True
		# mark the discovery time
		self.discovered[source] = self.Time
		self.low[source] = self.Time
		self.Time += 1

		# check all unvisited neighbour of current node
		for node in self.graph[source]:
			if not self.visited[node]:
				# update parent
				self.parent[node] = source
				self.Bridges(node)

				# Check if the subtree rooted with node has a connection to 
                # one of the ancestors of source
				self.low[source] = min(self.low[source],self.low[node])

				# first condition 
				# if source have 2 or more children and have no parent 
				if self.discovered[source] < self.low[node]:
					self.cut_edges.append( (source,node) )


			elif self.parent[source] != node:
				# update the earliest ancestor the source node can reach
				# except its own parent
				self.low[source] = min(self.low[source], self.discovered[node])

	def Cut_Edges(self):
		# to record parent of each vertex
		self.parent = [-1]*self.v
		# to record the time when each vertex is discovered
		self.discovered = [float('inf')]*self.v
		# to track the earliest ancestor each node can have back 
		# link to, this  way nodes which have link ancestor greater 
		# earlier than current node can not be disconnected 
		self.low = [float('inf')]*self.v
		# to record which vertex is cut vertex
		self.cut_edges = []
		# visited array
		self.visited = [False]*self.v

		for node in range(self.v):
			if not self.visited[node]:
				self.Bridges(node)

		print( self.cut_edges )

if __name__ == "__main__":
	g1 = Graph(5) 
	g1.addEdge(1, 0) 
	g1.addEdge(0, 2) 
	g1.addEdge(2, 1) 
	g1.addEdge(0, 3) 
	g1.addEdge(3, 4) 
	
	print("\nBridges in first graph ")
	g1.Cut_Edges() 
	
	g2 = Graph(4) 
	g2.addEdge(0, 1) 
	g2.addEdge(1, 2) 
	g2.addEdge(2, 3) 
	print("\nBridges in second graph ")
	g2.Cut_Edges() 
	
	
	g3 = Graph (7) 
	g3.addEdge(0, 1) 
	g3.addEdge(1, 2) 
	g3.addEdge(2, 0) 
	g3.addEdge(1, 3) 
	g3.addEdge(1, 4) 
	g3.addEdge(1, 6) 
	g3.addEdge(3, 5) 
	g3.addEdge(4, 5) 
	print("\nBridges in third graph ")
	g3.Cut_Edges() 