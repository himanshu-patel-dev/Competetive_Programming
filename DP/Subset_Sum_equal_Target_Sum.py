def  Subset_Sum(lst, target):
	"""
	Output 1 noly if target can be met as sum of any of the subset else 0
	"""
	row = len(lst)+1
	col = target+1
	dp = [ [ 0 for i in range(col)] for j in range(row)]

	# If sum is 0, then answer is 1  
	for i in range(row):
		dp[i][0] = 1

	for i in range(1,row):
		for j in range(1,col):
			if j >= lst[i-1]:
				dp[i][j] = max( dp[i-1][j], dp[i-1][j - lst[i-1]] )
			else:
				dp[i][j] = dp[i-1][j]
	# for row in dp:
	# 	print(*row)
	return dp[-1][-1]


# if __name__ == "__main__":
# 	# lst = [3,2,4,19,3,7,13,10,6,11]
# 	# target = 17

# 	# two check if array can be divided such that sum of two part are equal
# 	lst = [5,5,7,7]
# 	target = sum(lst)//2
# 	print( Subset_Sum(lst, target) )
