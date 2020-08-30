""" Topological Sort for directed graph """
from collections import defaultdict

class Graph:
	def __init__(self):
		self.g = defaultdict(list)

	# considering undirectional graph
	def addEdge(self,u,v):
		self.g[u].append(v)

	def topological_sub(self,node,sequence,visited):
		""" t sort for only 'start' vertex passed """
		visited[node] = True
		
		# visit all children of start node before adding it to sequence
		# later we reverse this sequence
		for nbr in self.g[node]:
			if not visited[nbr]:
				visited[nbr] = True
				self.topological_sub(nbr,sequence,visited)
		
		# append start vertex to sequence after all its child are added
		sequence.append(node)

	def TopologicalSort_complete(self,vertex):
		""" t sort for complete graph """
		sequence = []
		visited = [False]*vertex
		for v in range(vertex):
			if not visited[v]:
				self.topological_sub(v,sequence,visited)
		# reverse the sequence to get top sort
		return sequence[::-1]
		   

if __name__ == "__main__":
	graph = Graph()

	graph.addEdge(0,1)
	graph.addEdge(0,2)
	graph.addEdge(1,2)
	graph.addEdge(1,3)
	graph.addEdge(2,7)

	graph.addEdge(4,5)
	graph.addEdge(4,6)

	# to display the adjacency list
	# for v in range(8): 
	# 	print(v,'->',graph.g[v])

	vertex = 8
	print( graph.TopologicalSort_complete(vertex) )