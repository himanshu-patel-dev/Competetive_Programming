def two_equal_subset(lst):
	""" 
	output 1 if elements can be partitioned 
	into two set with equal sum 
	"""
	n = len(lst)
	s = sum(lst)

	if s%2 != 0:
		return 0
	
	dp = [0]*(s//2 + 1)
	# first element is sum=0 which can be possibly attain in null subset
	dp[0] = 1		
	s = s//2

	# iterating for each element in lst
	for i in range(n):
		# traversing from back to avoid counting one 
		# element twice (already used element is set 1) 
		for j in range(s,-1,-1):
			if j+lst[i] > s:
				continue
			elif dp[j]:
				dp[j + lst[i]] = 1
	# print(dp)
	return dp[s]

if __name__ == "__main__":
	lst = [2,3,5,10]
	print( two_equal_subset(lst) )
