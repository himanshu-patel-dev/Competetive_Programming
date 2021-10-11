"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j 
such that |nums[i] - nums[j]| == k.
 
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
"""

from typing import *
from collections import Counter

class Solution:
	def countKDifference(self, nums: List[int], k: int) -> int:
		"""
			T = O(n)
			S = O(n)
		"""
		# collect freq of all the nums in list
		freq = Counter(nums)
		# check if for a num it's complement exists, if it's there then add the 
		# freq of complement in total sum
		return sum([ freq[num+k] for num in nums])
