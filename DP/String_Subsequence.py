'''
Given two strings S1 and S2, find the number of times the second string 
occurs in the first string, whether continuous or discontinuous.
'''

class Solution:
	def countWays(self, S1, S2):
		# string S1 in colums and S2 in row
		dp = [ [0]*(len(S1)+1) for j in range(len(S2)+1)]

		# if string S2 is empty then its a valid subsequence 
		# hence mark first row with all 1's
		for i in range(len(S1)+1):
			dp[0][i] = 1


		for r in range(1,len(S2)+1):
			for c in range(1,len(S1)+1):
				# if both char of s1 and s2 are equal then
				# fun(s2,s1) = fun(s2-1,s1-1) + fun(s2,s1-1) 
				# looking for all remaining char of s2 is remaining s1
				# and looking for complete char of s2 in remaining s1
				if S2[r-1] == S1[c-1]:
					dp[r][c] = dp[r-1][c-1] + dp[r][c-1]
				# if not matched then look for all char of s2 in remaining s1
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