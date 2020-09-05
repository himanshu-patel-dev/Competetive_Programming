class Graph:
	def __init__(self,v):
		# storing graph as adj matrix
		self.v = v
		self.graph = set()

	def add_edge(self,u,v,w):
		# add weighted edge in graph
		# directed graph
		self.graph.add( (u,v,w) )

	def get_path(self,source,dest,previous):
		path = []
		current = dest
		while current != -1:
			path.append(current)
			current = previous[current]
		print(path[::-1])

	def bellman_ford(self,source):
		# distance is measured from source 
		distance = [float('inf')]*self.v
		previous = [-1]*self.v
		
		# initialize the source vertex values
		distance[source] = 0

		# iterate for v-1 time, any graph with v edges can be covered in path of 
		# atmost len v-1, in vth iteration if any vertex distance further get reduced 
		# it means that vertex is under -ve edge cycle or is affcted by -ve wgt cycle
		# mark then by -inf
		
		# for v-1 iteration
		for path_len in range(self.v-1):
			# for each edge in graph 
			for u,v,w in self.graph:
				# relax edge u to v if lesser dist is found
				if distance[u] + w < distance[v]:
					distance[v] = distance[u] + w
					previous[v] = u

		# last vth iteration
		# vertex which get reduced further are in -ve wgt cycle
		for u,v,w in self.graph:
			if distance[u] + w < distance[v]:
				distance[v] = float['-inf']

		print(distance)
		print(previous)

		self.get_path(0,3,previous)

if __name__ == "__main__":

	g = Graph(5)
	# provide a adj matrix or add each edge by its weight
	g.add_edge(0, 1, -1)  
	g.add_edge(0, 2, 4)  
	g.add_edge(1, 2, 3)  
	g.add_edge(1, 3, 2)  
	g.add_edge(1, 4, 2)  
	g.add_edge(3, 2, 5)  
	g.add_edge(3, 1, 1)  
	g.add_edge(4, 3, -3)

	g.bellman_ford(0)


	print('\n')
