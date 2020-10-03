"""
Given a non-empty string s and a dictionary wordDict containing a list 
of non-empty words, determine if s can be segmented into a space-separated 
sequence of one or more dictionary words.

The same word in the dictionary may be reused multiple times in the 
segmentation. You may assume the dictionary does not contain duplicate 
words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as 
"apple pen apple".

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
# slow solution 140ms
class Solution1:
	""" T = O(n^3) n = len of string s """
	def wordBreak(self, s, wordDict):
		# make it set for easy lookup
		wordDict = set(wordDict)

		n = len(s)

		# each index (i,j) of dp denoted whether s[i,j] is a substring 
		# which can be made by using elements from dict or not
		dp = [[False for i in range(n)] for j in range(n)]

		# i denotes the size of segment of the string s we are dealing 
		# with and this fill the dp matrix diagonally
		for i in range(1,n+1):
			# no of row to visit based on size of i
			# i=1 then j=n, i=2 then j=n-1 when i=n then j=1
			for j in range(n-i+1):
				row,col = j,j+i-1
				# if substring is present is dict mark is as possible 
				# and continue
				if s[row:col+1] in wordDict:
					dp[row][col] = True
					continue
				
				# check for all break points bwtewwn i to j
				# k = i to j-1

				for k in range(row,col):
					if dp[row][k] and dp[k+1][col]:
						dp[row][col] = True
						valid = True
						break
		# for row in dp:
		# 	print(row)
		return dp[0][n-1]


# faster solution 36ms
class Solution2:
	""" T = O(n^3) n = len of string s """
	def wordBreak(self,s,wordDict):
		n = len(s)
		found = [False]*(n+1)
		found[0] = True
		wordDict = set(wordDict)

		for i in range(1,n+1):
			for j in range(i):
				if found[j] and s[j:i] in wordDict:
					found[i] = True
					break
		return found[-1]


if __name__ == "__main__":
	obj = Solution2()

	s = 'leetcode'
	lst = ["leet", "code"]
	print(obj.wordBreak(s,lst))

	s = "applepenapple" 
	lst = ["apple", "pen"]
	print(obj.wordBreak(s,lst))

	s = "catsandog" 
	lst = ["cats", "dog", "sand", "and", "cat"]
	print(obj.wordBreak(s,lst))
