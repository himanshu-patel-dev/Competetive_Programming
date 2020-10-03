"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all 
the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: 
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly 
less than k.

Constraints:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""

class Solution:
	def numSubarrayProductLessThanK(self, nums, k):
		total = 1	# to hold the current product 
		result = 0	# to hold the result
		last = 0	# to hold the index of last ele of window
		for curr in range(len(nums)):
			# inc the product
			total *= nums[curr]
			# dec the product till it is less than k
			while last <= curr and total >= k:
				total = total//nums[last]
				last += 1
			# add the ans to result, note if current ele>=k then is add 0
			result += (curr-last+1)
			# print(total,result)
		# give result
		return result

if __name__ == "__main__":
	s = Solution()

	lst = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
	k = 19
	print( s.numSubarrayProductLessThanK(lst,k) )

	lst = [10, 5, 2, 6] 
	k = 100
	print( s.numSubarrayProductLessThanK(lst,k) )
