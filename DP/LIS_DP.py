def  LIS(lst):
	"""	
	Longest Increasing Subsequence (give string of max sub sequence)
	Time Comp = O(n^2)
	Space Comp = O()
	"""
	n = len(lst)
	dp = [1]*n

	# we start from index 1 because index zero can have max value 1
	# each index represent the max LIS length till that position
	for i in range(1,n):
		for j in range(i):
			if lst[j] < lst[i]:
				dp[i] = max( dp[i], dp[j]+1 )
	# print(dp)

	# use this return to get LIS length 
	# return max(dp)

	# below code is to get the LIS sequence
	result = []
	index = 1
	for i in range(n):
		if dp[i] == index:
			result.append( lst[i] )
			index += 1

	return result

if __name__ == "__main__":
	# lst = [10, 22, 9, 33, 21, 50, 41, 60]
	# max len = 5 (10 22 33 50 60) (10 22 33 41 60)
	lst = [10, 22, 9, 33, 21, 50, 11]
	print( LIS(lst) )