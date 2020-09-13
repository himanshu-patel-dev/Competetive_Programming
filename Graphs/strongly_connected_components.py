from collections import defaultdict
class Graph:
	def __init__(self,v):
		self.v = v
		self.graph = defaultdict(list)
		self.graph_transpose = defaultdict(list)
 
	def addEdge(self,u,v): 
		# add an edge to directed graph
		self.graph[u].append(v) 
		# add an reversed edge to transpose graph
		self.graph_transpose[v].append(u)
		

	def DFS(self,source,visited,component):
		# a usual DFS function
		visited[source] = True
		# adding a vertex to current component
		component.append(source)

		for node in self.graph_transpose[source]:
			if not visited[node]:
				self.DFS(node,visited,component)

	def DFS_stackfill(self,source,visited,stack):
		visited[source] = True

		for node in self.graph[source]:
			if not visited[node]:
				self.DFS_stackfill(node,visited,stack)
		# add vertex to stack when back tracking
		stack.append(source)

	def SCC(self):	# get strongly conn components
		# to recond node in eacch component
		stack = []
		visited = [False]*self.v
		# fill vertices in stack accordin to finishing 
		# time of each connected component

		# traversal of original graph
		for v in range(self.v):
			if not visited[v]:
				self.DFS_stackfill(v,visited,stack)

		visited = [False]*self.v
		# traversal on transpose graph till stack become empty
		while stack:
			vertex = stack.pop()
			if not visited[vertex]:
				component = []
				self.DFS(vertex,visited,component)
				print(component)

if __name__ == "__main__":
	g = Graph(5) 
	g.addEdge(1, 0) 
	g.addEdge(0, 2) 
	g.addEdge(2, 1) 
	g.addEdge(0, 3) 
	g.addEdge(3, 4) 

	g.SCC()

	print('\n')

	g = Graph(9) 
	g.addEdge(3, 0) 
	g.addEdge(0, 1) 
	g.addEdge(1, 2) 
	g.addEdge(2, 3) 
	g.addEdge(2, 4)
	g.addEdge(4, 5)
	g.addEdge(5, 6)
	g.addEdge(6, 4)
	g.addEdge(7, 6)
	g.addEdge(7, 8) 

	g.SCC()