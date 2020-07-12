def make_query(M,q):
	"""
	M = matrix on which the query need to be made
	n = size of square matrix
	q = query 
	"""
	x1,y1,x2,y2 = q[0],q[1],q[2],q[3]
	M[x1][y1] += 1
	M[x1][y2+1] -= 1
	M[x2+1][y1] -= 1
	M[x2+1][y2+1] += 1
	return M

def print_matrix(M):
	for row in M:
		print(*row)

def remove_last_col_and_row(M):
	for i in range( len(M) ):
		M[i] = M[i][:-1]
	M.pop()
	return M

def solve(n,q):
	"""
	inc by one all cells in range x1 y1 to x2 y2 
	then output final matrix after certain matrix
	"""
	matrix = [ [0 for i in range(n+1)] for j in range(n+1) ]

	# implement all query one by one
	for k in range(q):
		query = list( map(int, input().split()) )
		matrix = make_query(matrix,query)

	# initialize first row
	for i in range(1,n+1):
		matrix[0][i] += matrix[0][i-1]

	# initialize first col
	for j in range(1,n+1):
		matrix[j][0] += matrix[j-1][0]

	# initialize all other cells
	for i in range(1,n+1):
		for j in range(1,n+1):
			matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]

	matrix = remove_last_col_and_row(matrix)
	print_matrix( matrix )

for _ in range(int(input())):
	n,q = map(int, input().split())
	solve(n,q)
