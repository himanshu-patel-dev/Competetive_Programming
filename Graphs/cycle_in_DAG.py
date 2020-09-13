from collections import defaultdict
class Graph:
	def __init__(self,v):
		self.v = v
		self.graph = defaultdict(list)
 
	def addEdge(self,u,v): 
		# add an edge to directed graph
		self.graph[u].append(v)
		

	def DFS(self,source,visited,inStack):
		# a usual DFS function
		# mark current node as visited and in stack
		visited[source] = True
		inStack[source] = True
		
		for node in self.graph[source]:
			if not visited[node]:
				# if any of the descendent return true then 
				# return true, it means some cycle present
				if self.DFS(node,visited,inStack):
					
					return True
			elif inStack[node]:
			# node in recursion stack it means cycle present
				return True

		# remove node from recursion stack
		inStack[source] = False
		return False

	def isCycle(self):
		visited = [False]*self.v
		inStack = [False]*self.v
		cycle = False

		for node in range(self.v):
			if not visited[node]:
				if self.DFS(node,visited,inStack):
					cycle = True
					break

		if cycle:
			print("Cycle Present")
		else:
			print("No Cycle")

if __name__ == "__main__":
	
	g = Graph(4) 
	g.addEdge(0, 1) 
	g.addEdge(0, 2) 
	g.addEdge(1, 2) 
	g.addEdge(2, 0) 
	g.addEdge(2, 3) 
	g.addEdge(3, 3) 
	
	g.isCycle()