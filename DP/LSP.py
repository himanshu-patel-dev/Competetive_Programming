def LSP(string):
	""" Longest Pallindrome Subsequence"""
	n = len(string)
	dp = [ [0 for i in range(n)] for j in range(n)]
	
	# initialize diagonal entries 
	# every letter can produce 1 len pallindrome
	for i in range(n):
		dp[i][i] = 1

	for k in range(1,n):
		for i in range(n-k):
			j = i+k
			if string[i] == string[j]:
				dp[i][j] = 2 + dp[i+1][j-1]
			else:
				dp[i][j] = max( dp[i+1][j], dp[i][j-1] )
	
	# for row in dp:
	# 	print(*row)
	return dp[0][-1]

if __name__ == "__main__":
	string = "ABCDBA"	# ans = 5
	print( LSP(string) )