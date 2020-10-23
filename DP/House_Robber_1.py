"""
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have security 
system connected and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each 
house, determine the maximum amount of money you can rob tonight without 
alerting the police.
"""
class Solution:
	def rob(self, nums):
		if len(nums) == 0:
			return 0

		if len(nums) == 1:
			return nums[0]
		
		dp1,dp2 = 0,0
		# each step choose the max amount we can get based on
		# i-1 and i-2 index 
		for num in nums:
			dp1,dp2 = dp2, max(dp2,dp1+num)
		return dp2
		
if __name__ == "__main__":
	s = Solution()

	lst = [1,2,3,1]
	print( s.rob(lst) )

	lst = [2,7,9,3,1]
	print( s.rob(lst) )
