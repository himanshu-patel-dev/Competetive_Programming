def  least_difference_partition_of_array(lst):
	"""
	partition a array into two such that the diff of two sum is least
	"""
	row = len(lst)+1
	# is sum is even try to look for s//2 else try look for ( s//2 or s//2 + 1)
	# since s//2 is common to both we choose s//2 and for 1 index s = s//2 + 1
	col = (sum(lst)//2) + 1
	dp = [[False for i in range(col)] for j in range(row)]

	# a sum total of zero can be achived form empty set
	for i in range(row):
		dp[i][0] = True
	
	for i in range(1,row):
		for j in range(1,col):
			if j >= lst[i-1]:
				dp[i][j] = dp[i-1][j] or dp[i-1][j-lst[i-1]]
			else:
				dp[i][j] = dp[i-1][j]

	# for p in dp:
	# 	print(p)

	# getting highest sum possible close to s//2
	for i in range(col-1,-1,-1):
		if dp[row-1][i]:
			first_part = i
			break
	second_part = sum(lst) - first_part
	return abs( second_part - first_part )

if __name__ == "__main__":
	# lst = [3,1,4,2,2,1]
	# lst = [1,2,3,5,12]
	lst = [1,2,4]
	print( least_difference_partition_of_array(lst) )
