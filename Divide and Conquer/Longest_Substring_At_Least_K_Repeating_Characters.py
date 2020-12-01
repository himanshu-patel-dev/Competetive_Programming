'''
Given a string s and an integer k, return the length of the longest substring of s 
such that the frequency of each character in this substring is less than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is 
repeated 3 times.

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''

'''
LeetCode: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/
YouTube: https://www.youtube.com/watch?v=bHZkCAcj3dc&ab_channel=KnowledgeCenter

T = O(n^2)	# if each time we are able to remove just one char from ends of string
			# so total n call. in each call we scan whole string thus n
			# final = n^2
S = O(n)	# rec call
'''

class Solution:
	def longestSubstring(self, s: str, k: int) -> int:
		from collections import Counter
		n = len(s)
		
		# if k is more than n or k = 0 then no such substring exist
		if n < k or k == 0:
			return 0
		# if k=1 then each char is a valid substring thus complete string is selected
		if k == 1:
			return n
		
		# count freq of all char in string s
		count = Counter(s)
		
		# find index i where first char with less than k freq occur 
		i = 0
		while i<n and count[s[i]] >= k: i += 1
		
		if i >= n-1: return i   # it can return n as well n-1
		
		# take substring before i index and make a rec call to same function
		res1 = self.longestSubstring(s[:i],k)
		
		# skip those char which have less than k count from front of second substring
		while i<n and count[s[i]] < k: i+= 1
		
		# make rec call to same fun with second substring
		res2 = self.longestSubstring(s[i:],k) if i<n else 0
		
		# return max of two len
		return max(res1,res2)

if __name__ == "__main__":
	s = Solution()

	string = 'aaabb'
	k = 3
	print(s.longestSubstring(string,k))

	string = 'ababbc'
	k = 2
	print(s.longestSubstring(string,k))