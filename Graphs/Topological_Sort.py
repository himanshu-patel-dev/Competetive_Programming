""" Topological Sort for directed graph """
from collections import defaultdict

class Graph:
	def __init__(self,v):
		self.g = defaultdict(list)
		self.v = v

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

	def TopologicalSort_complete(self):
		""" t sort for complete graph """
		""" 
		Given graph should not have cycle check using cycle in DAG algo
		"""
		sequence = []
		visited = [False]*self.v
		for v in range(self.v):
			if not visited[v]:
				self.topological_sub(v,sequence,visited)
		# reverse the sequence to get top sort
		return sequence[::-1]
		   

if __name__ == "__main__":
	graph = Graph(8)

	graph.addEdge(0,1)
	graph.addEdge(0,2)
	graph.addEdge(1,2)
	graph.addEdge(1,3)
	graph.addEdge(2,7)

	graph.addEdge(4,5)
	graph.addEdge(4,6)

	print( graph.TopologicalSort_complete() )
