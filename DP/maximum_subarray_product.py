"""
Given an integer array nums, find the contiguous subarray within an 
array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
	def maxProduct(self, nums):
		n = len(nums)
		dp_max = [0]*n
		dp_min = [0]*n
		dp_min[0] = dp_max[0] = nums[0]

		for i in range(1,n):
			if nums[i] > 0:
				dp_max[i] = max(dp_max[i-1]*nums[i], nums[i])
				dp_min[i] = dp_min[i-1]*nums[i]
			else:
				dp_max[i] = dp_min[i-1]*nums[i]
				dp_min[i] = min(dp_max[i-1]*nums[i],nums[i])

		return max(dp_max)

if __name__ == "__main__":
	
	s = Solution()
	lst = [2,3,-2,4]
	print( s.maxProduct(lst) )

	lst = [-2,0,-1]
	print( s.maxProduct(lst) )

	lst = [3,-1,4]
	print( s.maxProduct(lst) )