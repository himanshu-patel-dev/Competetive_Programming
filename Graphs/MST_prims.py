class Graph:
	def __init__(self,v):
		# storing graph as adj matrix
		self.v = v
		self.graph = [ [0]*self.v for i in range(self.v) ]

	def add_edge(self,u,v,w):
		# add weighted edge in graph
		# undirected graph
		self.graph[u][v] = w
		self.graph[v][u] = w

	def print_graph(self):
		for row in range(self.v):
			print( row, self.graph[row] )

	def print_MST(self,parent):
		for i in range(1,self.v):
			print( f"{parent[i]} -> {i} : {self.graph[i][parent[i]]}" )

	def get_path(self,source,dest,previous):
		path = []
		current = dest
		while current != -1:
			path.append(current)
			current = previous[current]
		print(path[::-1])

	def min_weight_edge(self,dist,visited):
		m = float('inf')
		# serach among the non visited node among
		# all nodes and select the min weight one
		for i in range(self.v):
			if not visited[i] and dist[i] < m:
				m = dist[i]
				min_node = i
		return min_node

	def MST_prims(self):
		""" Time Comp = O(V^2) """
		# weight track all available vertices which can be reached by one of the 
		# vertices in MST with min weight, this weight updates if a lesser wt edge is found 
		weight = [float('inf')]*self.v
		# track all vertices included inside MST
		inMST = [False]*self.v
		# track parent of node in MST, used to const MST
		parent = [-1]*self.v
		
		# initialize the source vertex values
		# let the initial vertex be 0, all vertex will finally be 
		# included thus start from any where result will be same 
		source = 0
		weight[source] = 0


		for node in range(self.v):
			# get the node which is not in MST and have min cost of adding in MST
			# min_node = source in first iteration as dist[source] = 0 initially
			MST_node = self.min_weight_edge(weight,inMST)
			# put this node in MST, so we dont process this node again
			inMST[MST_node] = True

			# look for all the nodes in its neighbour and update weight if any 
			# unvisited node can be reached in lesser cost from this vertiex
			for n in range(self.v):
				if not inMST[n] and self.graph[MST_node][n] > 0 and weight[n] > self.graph[MST_node][n]:
					weight[n] = self.graph[MST_node][n]
					parent[n] = MST_node

		self.print_MST(parent)
		print('Previous Nodes for each node ',parent)
		print('Path from 0 to 3')
		self.get_path(0,2,parent)
		print( "MST SUM: ", sum(weight) )

if __name__ == "__main__":

	g = Graph(5)
	# provide a adj matrix or add each edge by its weight
	g.add_edge(0,1,2)
	g.add_edge(0,3,6)
	g.add_edge(1,3,8) 
	g.add_edge(1,4,5)
	g.add_edge(1,2,3)
	g.add_edge(4,3,9)
	g.add_edge(4,2,7)

	# g.print_graph()

	g.MST_prims()


	print('\n')

	g = Graph(9)
	g.graph = [
			[0, 4, 0, 0, 0, 0, 0, 8, 0	], 
			[4, 0, 8, 0, 0, 0, 0, 11, 0	], 
			[0, 8, 0, 7, 0, 4, 0, 0, 2	], 
			[0, 0, 7, 0, 9, 14, 0, 0, 0	], 
			[0, 0, 0, 9, 0, 10, 0, 0, 0	], 
			[0, 0, 4, 14, 10, 0, 2, 0, 0], 
			[0, 0, 0, 0, 0, 2, 0, 1, 6	], 
			[8, 11, 0, 0, 0, 0, 1, 0, 7	], 
			[0, 0, 2, 0, 0, 0, 6, 7, 0	] 
        ]

	# g.print_graph()

	g.MST_prims()


