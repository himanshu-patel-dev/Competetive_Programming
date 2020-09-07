class Graph:
	def __init__(self,v):
		# storing graph as adj matrix
		self.v = v
		self.graph = []

	def add_edge(self,u,v,w):
		# add weighted edge in graph
		# undirected graph
		self.graph.append( [u,v,w] )

	def print_mst(self,mst):
		s = 0
		for edge in mst:
			print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
			s += edge[2]
		print("Sum of MST: ",s)

	def find(self,node):
		# get the root of the node
		root = node
		while root != self.parent[root]:
			root = self.parent[root]
		
		# make all the nodes in path to root to directly point to root
		while node != self.parent[node]:
			node, self.parent[node] = self.parent[node], root

		return root

	def union(self,x,y):
		rootx = self.find(x)
		rooty = self.find(y)

		# already in same set
		if rootx == rooty:
			return

		if self.rank[rootx] > self.rank[rooty]:
			self.rank[rootx] += self.rank[rooty]
			self.parent[rooty] = rootx
		else:
			self.rank[rooty] += self.rank[rootx]
			self.parent[rootx] = rooty


	def kruskal(self):
		# initialize the array in which to keep the edges of MST
		MST = []

		# sort all edges with weight in increasing order
		self.graph = sorted( self.graph, key = lambda x: x[2] )

		# to keep count of edges in mst
		mst_edge = 0
		# create the paernt and rank/size list
		self.parent = [i for i in range(self.v)]
		self.rank = [1 for i in range(self.v)]

		# iterate over all edges of graph
		for i in range(self.v):
			u,v,w = self.graph[i]

			# if both end lies in same set then skip this 
			# edge else a cycle will form
			if self.find(u) == self.find(v):
				continue
			
			# add the edge in mst edges
			self.union(u,v)
			# add edge to mst
			MST.append( (u,v,w) )
			mst_edge += 1
			# for v vertices in tree we only need v-1 edges 
			# as soon we get v-1 edges stop
			if mst_edge == self.v-1:
				break

		self.print_mst(MST)

if __name__ == "__main__":

	g = Graph(4) 
	g.add_edge(0, 1, 10) 
	g.add_edge(0, 2, 6) 
	g.add_edge(0, 3, 5) 
	g.add_edge(1, 3, 15) 
	g.add_edge(2, 3, 4) 
  
	g.kruskal() 
