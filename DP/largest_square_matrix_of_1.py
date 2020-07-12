def largest_square_matrix_of_1( matrix ):
	"""
	return size of largest square matrix of 1
	"""
	col = len(matrix[0])
	row = len(matrix)
	dp = matrix.copy()

	# start from 1,1
	for i in range(1,row):
		for j in range(1,col):
			up = dp[i-1][j]
			left = dp[i][j-1]
			diag = dp[i-1][j-1]
			current = dp[i][j]
			if up and left and diag and current:
				dp[i][j] += min(up, left, diag)
	
	# for row in dp:
	# 	print(row)
	
	# getting max of matrix
	m = -float('inf')
	for row in dp:
		m = max(m, max(row) )
	return m

if __name__ == "__main__":
	matrix = [
		[0,1,1,0,1],
		[1,1,0,1,0],
		[0,1,1,1,0],
		[1,1,1,1,0],
		[1,1,1,1,1],
		[0,0,0,0,0]
	]

	print( largest_square_matrix_of_1( matrix ) )