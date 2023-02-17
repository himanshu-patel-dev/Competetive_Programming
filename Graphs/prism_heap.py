from  collections import defaultdict
import heapq

def MST_Prism(graph, sourceVertex):
	visitedVertices = set([sourceVertex])
	MST = defaultdict(set)
	COSTS = 0

	edgesMinHeap = [
		(cost, sourceVertex, destVertex) for destVertex, cost in graph[sourceVertex].items()
	]
	heapq.heapify(edgesMinHeap)

	# this loop is called E times
	while edgesMinHeap:
		cost, frm, to = heapq.heappop(edgesMinHeap)
		if to in visitedVertices:
			continue
		COSTS += cost
		MST[frm].add(to)
		print(f"Edges: from {frm} to {to} cost : {cost}")
		visitedVertices.add(to)

		for next_to, cost in graph[to].items():
			if next_to not in visitedVertices:
				heapq.heappush(edgesMinHeap, (cost, to, next_to) )
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

print(dict(MST_Prism(example_graph, 'A')))

# {'A': set(['B']),
#  'B': set(['C', 'D']),
#  'D': set(['E']),
#  'E': set(['F']),
#  'F': set(['G'])}
