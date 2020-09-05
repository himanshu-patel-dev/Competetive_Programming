"""
A string S of lowercase English letters is given. We want to partition 
this string into as many parts as possible so that each letter appears 
in at most one part, and return a list of integers representing the 
size of these parts.

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because 
it splits S into less parts.

"""

from collections import defaultdict
from bisect import bisect_right

class Solution:
	def partitionLabels(self, S):
		# get the last index of each elemetns
		last_index = defaultdict(int)
		for i,c in enumerate(S):
			last_index[c] = i

		# start with index 0 and go till end
		start, n = 0, len(S)
		# keep recording indexes at which a segment terminates
		result = []

		while start < n:
			# based on current ele get the its last index we have 
			# to interate till there compulsory 
			end = last_index[ S[start] ]

			# iterate till end and update end value if any element 
			# in segmnet have greater terminating point
			while start <= end:
				end = max(end, last_index[ S[start] ])
				start += 1
			# reconrd the index+1 of ele at which segment ends
			result.append( start )

		# get length of each segment from index
		length = [ result[0] ]
		for i in range(1,len(result)):
			length.append( result[i] - result[i-1] )

		return length

if __name__ == "__main__":
	s = Solution()

	print( s.partitionLabels("ababcbacadefegdehijhklij") )
