"""
function dijkstra(G, S)
	for each vertex V in G
		distance[V] <- infinite
		previous[V] <- NULL
		If V != S, add V to Priority Queue Q
	distance[S] <- 0
	
	while Q IS NOT EMPTY
		U <- Extract MIN from Q
		for each unvisited neighbour V of U
			tempDistance <- distance[U] + edge_weight(U, V)
			if tempDistance < distance[V]
				distance[V] <- tempDistance
				previous[V] <- U
	return distance[], previous[]
"""

import heapq

class Dijkstra:
	def __init__(self, n) -> None:
		self.n = n
		# adjacency list of n x n
		self.graph = [[0 for _ in range(n)] for _ in range(n)]

	def print_result(self, distance):
		for i in range(self.n):
			print(f"Vertex : {i} 		- 		Distance {distance[i]}")

	def dijkstra(self, source):
		"""
			source: int - starting vertex from which to measure 
			distance of all other vertices

			T = O(E * V) = O(V^3) - since we are iterating over all n vertices 
			for each edge - V in E*V
			S - O(E) = O(V^2) - to store all edges in queue
		"""
		# distance of all nodes is marked inf
		distance = [float('inf') for _ in range(self.n)]
		# keep track of which all vertices are visited/unvisited
		visited = [False]*self.n
		# marke the source vertex at dist 0 so this would be 
		# picked up first
		distance[source] = 0
		# a min heap to pick the vertex with least dist in log(n)
		pq = [(0, source)]

		while pq:	# max iterations - no of edges - E
			# get the edge with min distance
			# comp of heap pop = Log(E) - we are putting edges not vertices
			curr_dist, curr_node = heapq.heappop(pq)	
			# if the min dist edge take us to a visited vertex 
			# then ignore this edge
			if visited[curr_node]:
				continue
			# if this is unvisited vertex then mark it as visited
			visited[curr_node] = True
			# check for the unvisited nbr of this vertex and relax
			# the edges between curr_node and 
			# loop V times for each edge
			for nbr, nbr_dist in enumerate(self.graph[curr_node]):
				# if nbr is already visited or there exists no edge 
				# from curr_node to nbr then skip this edge
				if visited[nbr] or nbr_dist <= 0 :
					continue
				new_dist = curr_dist + nbr_dist
				# if new dist is lesser than the curr min dist of 
				# nbr node then update distance of nbr node and add 
				# this edge in min heap
				if new_dist < distance[nbr]:
					distance[nbr] = new_dist
					heapq.heappush(pq, (new_dist, nbr))
		
		if not all(visited):
			return -1
		self.print_result(distance)
		return distance


g = Dijkstra(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		   [4, 0, 8, 0, 0, 0, 0, 11, 0],
		   [0, 8, 0, 7, 0, 4, 0, 0, 2],
		   [0, 0, 7, 0, 9, 14, 0, 0, 0],
		   [0, 0, 0, 9, 0, 10, 0, 0, 0],
		   [0, 0, 4, 14, 10, 0, 2, 0, 0],
		   [0, 0, 0, 0, 0, 2, 0, 1, 6],
		   [8, 11, 0, 0, 0, 0, 1, 0, 7],
		   [0, 0, 2, 0, 0, 0, 6, 7, 0]
		   ]
g.dijkstra(0)

"""
Vertex : 0              -               Distance 0
Vertex : 1              -               Distance 4
Vertex : 2              -               Distance 12
Vertex : 3              -               Distance 19
Vertex : 4              -               Distance 21
Vertex : 5              -               Distance 11
Vertex : 6              -               Distance 9
Vertex : 7              -               Distance 8
Vertex : 8              -               Distance 14
"""
