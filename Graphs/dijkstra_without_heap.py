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

	def get_path(self,source,dest,previous):
		path = []
		current = dest
		while current != -1:
			path.append(current)
			current = previous[current]
		print(path[::-1])

	def min_distance_node(self,dist,visited):
		m = float('inf')
		# serach among the non visited node among
		# all nodes and select the min distance one
		for i in range(self.v):
			if not visited[i] and dist[i] < m:
				m = dist[i]
				min_node = i
		return min_node

	def dijkstra(self,source):
		# distance is measured from source 
		visited = [False]*self.v
		distance = [float('inf')]*self.v
		previous = [-1]*self.v
		
		# initialize the source vertex values
		distance[source] = 0

		for node in range(self.v):
			# get the node at min distance from source
			# min_node = source in first iteration as dist[source] = 0 initially
			min_node = self.min_distance_node(distance,visited)
			# mark this node as visited, so we dont process this node again
			visited[min_node] = True


			# update unvisited neighbour vertices of currently picked vertex 
			# to lesser distance if possible
			for nbr in range(self.v):
				new_dist = distance[min_node] + self.graph[min_node][nbr]
				old_dist = distance[nbr]
	
				# update the dist nbr node is not visited and edge between min_node 
				# and nbr exist and new dist is better than old
				if not visited[nbr] and self.graph[min_node][nbr] > 0 and old_dist > new_dist:
					distance[nbr] = new_dist
					previous[nbr] = min_node

		print('Distance from source to all nodes',distance)
		print('Previous Nodes for each node ',previous)
		print('Path from 0 to 3')
		self.get_path(0,3,previous)

if __name__ == "__main__":

	g = Graph(5)
	# provide a adj matrix or add each edge by its weight
	g.add_edge(0,1,6)
	g.add_edge(0,3,1)
	g.add_edge(1,3,2) 
	g.add_edge(1,4,2)
	g.add_edge(1,2,5)
	g.add_edge(4,3,1)
	g.add_edge(4,2,5)

	# g.print_graph()

	g.dijkstra(0)


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

	g.dijkstra(0)


