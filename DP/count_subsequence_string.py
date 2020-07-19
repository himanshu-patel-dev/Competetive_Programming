import re
def count_subsequence_string(a,b):
	"""
	it return count of string b in a as subsequence
	"""
	n = len(a)
	m = len(b)

	dp = [ [0 for i in range(m+1)] for j in range(n+1)]

	# initializing the first column it means
	# an empty string is always available as subsequence
	for i in range(n+1):
		dp[i][0] = 1

	for i in range(1,n+1):
		for j in range(1,m+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j]
	
	# for row in dp:
	# 	print(row)
	
	return dp[-1][-1]

if __name__ == "__main__":
	a = "abadcb"
	b = "ab"
	print( count_subsequence_string(a,b) )