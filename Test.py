class Solution:
	def countWays(self, S1, S2):
		dp = [ [0]*(len(S1)+1) for j in range(len(S2)+1)]

		for i in range(len(S1)+1):
			dp[0][i] = 1

		for r in range(1,len(S2)+1):
			for c in range(1,len(S1)+1):
				if S2[r-1] == S1[c-1]:
					dp[r][c] = dp[r-1][c-1] + dp[r][c-1]
				else:
					dp[r][c] = dp[r][c-1]

		# for row in dp:
		# 	print(row)

		return dp[len(S2)][len(S1)]

if __name__ == "__main__":
	s = Solution()

	s1 = 'geeksforgeeks'
	s2 = 'gks'

	print(s.countWays(s1,s2))