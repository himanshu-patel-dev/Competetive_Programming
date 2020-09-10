def floyd_warshall_all_pair_shortest_path(matrix):
	"""  
	Shortest Path in between every pair of vertices 
	T = O(n^3)		S = O(n^2)
	"""
	n = len(matrix)

	for k in range(n):
		for r in range(n):
			for c in range(n):
				if r == k or c == k or r == c:
					continue
				else:
					matrix[r][c] = min(matrix[r][c], 
						matrix[r][k] + matrix[k][c]
					)
	return matrix

if __name__ == "__main__":
	matrix = [
		[0,11,1,6],
		[11,0,7,3],
		[1,7,0,2],
		[6,3,2,0],
	]

	for row in floyd_warshall_all_pair_shortest_path(matrix):
		print(row)