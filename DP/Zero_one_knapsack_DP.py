def  Zero_One_knapsack(capacity, weight, value):
	# 2D array of dimension (capacity + 1)x( no of items + 1 )
	row = len(weight) + 1
	col = capacity+1
	dp = [ [0 for i in range(col)] for j in range(row)]
	
	# initializing first row and first col with zeros
	for i in range(col):
		dp[0][i] = 0
	for i in range(row):
		dp[i][0] = 0

	# actual algorithm
	for i in range(1,row):
		for j in range(1,col):
			if weight[i-1] <= j:
				dp[i][j] = max( dp[i-1][j-weight[i-1]] + value[i-1], dp[i-1][j] )
			else:
				dp[i][j] = dp[i-1][j]

	return dp[-1][-1]


if __name__ == "__main__":
	value = [ 60, 100, 120 ]
	weight = [10, 20, 30]
	capacity = 25
	print( Zero_One_knapsack(capacity, weight, value) )
