from collections import defaultdict
import heapq

def MST_Kruskal(graph, source):
	edges = []
	for src in graph:
		for dest, cost in graph[src].items():
			edges.append((cost, src, dest))
	heapq.heapify(edges)
	DSU = [i for i in range(len(graph))]
	MST = defaultdict(set)
	COSTS = 0
	
	def find(DSU, x):
		if DSU[x] != x:
			DSU[x] = find(DSU, DSU[x])
		return DSU[x]
	
	def union(x,y,DSU):
		rootx, rooty = find(DSU, x), find(DSU, y)
		if rootx == rooty:
			return False
		DSU[rootx] = rooty
		return True

	while edges:
		edge = heapq.heappop(edges)
		frm, to = edge[1], edge[2]
		if union(NodeToNum[src], NodeToNum[to], DSU):
			print(f"Edges: from {frm} to {to} cost : {edge[0]}")
			COSTS += edge[0]
			MST[frm].add(to)
	print(COSTS)
	return MST

NodeToNum = {
	'A': 0,
	'B': 1,
	'C': 2,
	'D': 3,
	'E': 4,
	'F': 5,
	'G': 6
}

example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

print(dict(MST_Kruskal(example_graph, 'A')))

# {'A': set(['B']),
#  'B': set(['C', 'D']),
#  'D': set(['E']),
#  'E': set(['F']),
#  'F': set(['G'])}
