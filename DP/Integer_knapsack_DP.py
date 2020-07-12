def Integer_knapsack_DP(capacity, value, weight):
	"""
	same as knap sack but here each item can be used any number of time as a
	whole and not in fraction
	"""
	if capacity < min(weight):
		return 0
	else:
		row = len(weight)+1
		col = capacity + 1
		dp = [ [0 for i in range(col)] for j in range(row)]

		for c in range(col):
			for r in range(row):
				if c >= weight[r-1]:
					dp[r][c] = max( dp[r-1][c], dp[r][c - weight[r-1]] + value[r-1])
				else:
					dp[r][c] = dp[r-1][c]
		# for row in dp:
			# print(row)
		return dp[-1][-1]

for _ in range(int(input())):
	n,c = map(int, input().split())
	value = list(map(int, input().split()))
	weight = list(map(int, input().split()))
	print( Integer_knapsack_DP(c, value, weight) )
