def max_route_in_matrix( matrix ):
	"""
	starting from top left reach till bottom left and get max reward possible
	allowed moves = down, right
	"""
	col = len(matrix[0])
	row = len(matrix)

	dp = matrix.copy()

	# initializing first column
	for i in range(1,row):
		dp[i][0] += dp[i-1][0]

	# initializing first row
	for i in range(1,col):
		dp[0][i] += dp[0][i-1]

	# start from 1,1
	for i in range(1,row):
		for j in range(1,col):
			up = dp[i-1][j]
			left = dp[i][j-1]
			dp[i][j] += max(up, left)
	for row in dp:
		print(row)
	
	return dp[-1][-1]


if __name__ == "__main__":
	# reward_matrix = [
	# 	[5,24],
	# 	[15,25],
	# 	[27,40],
	# 	[50,60]
	# ]
	reward_matrix = [
		[1,2,3],
		[1,4,3],
		[9,9,9]
	]

	print( max_route_in_matrix( reward_matrix ) )