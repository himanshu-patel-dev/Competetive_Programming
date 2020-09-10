class Graph:
	def __init__(self,v):
		# storing graph as adj matrix
		from collections import defaultdict
		self.v = v
		self.graph = defaultdict(list)

	def add_edge(self,u,v):
		# add weighted edge in graph
		# directed graph
		self.graph[u].append(v)

	def find_path(self,source,dest,visited,path,paths):
		# if source is same as dest
		if source == dest:
			path.append(source)
			paths.append(path.copy())
			path.pop()
			return

		# maek source vertex as visited and recure for neighbout vertices
		visited[source] = True 
		path.append(source)

		# for every neighbour vertices check if it can reach dest
		for node in self.graph[source]:
			if not visited[node]:
				self.find_path(node,dest,visited,path,paths)
		
		# remove current node from path while back tracking and maek 
		# current node as unvisited
		path.pop()
		visited[source] = False


	def find_all_path(self,source,dest):
		""" T = O(E) as we are going through all edges """

		# returns all path between source to dest as list of paths
		# each path is a list of source to dest

		paths = []
		path = []
		visited = [False]*self.v
		self.find_path(source,dest,visited,path,paths)
		return paths

if __name__ == "__main__":

	g = Graph(4)
	# provide a adj matrix or add each edge by its weight
	g.add_edge(0, 1)  
	g.add_edge(0, 3)  
	g.add_edge(0, 2)  
	g.add_edge(1, 3)  
	g.add_edge(2, 0)
	g.add_edge(2, 1)  

	print( g.find_all_path(2,3) )
