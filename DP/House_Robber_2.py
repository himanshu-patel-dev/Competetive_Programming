"""
Each house has a certain amount of money stashed. All houses at this place 
are arranged in a circle. That means the first house is the neighbor of the 
last one. Meanwhile, adjacent houses have a security system connected, and 
it will automatically contact the police if two adjacent houses were broken 
into on the same night.

Given a list of non-negative integers nums representing the amount of money 
of each house, return the maximum amount of money you can rob tonight without 
alerting the police.
"""

class Solution:
	def rob(self, nums):
		if len(nums) == 0:
			return 0

		if len(nums) == 1:
			return nums[0]


		# if we select first house then we cant select last
		# if we select last then we cant select first
		# choose max among two and use same logic as for rob 1

		n = len(nums)
		# if we select first element
		# remove first two and last
		dp1 = nums[0] + self.rob_1(nums[2:-1])	
		# if we select last element
		# remove the first element and use rob 1
		# this step is critical do not try to remove first last and sec last
		# as we dont know who is max in last and sec last [2,3,2]
		dp2 = self.rob_1(nums[1:])

		return max(dp1,dp2)

	@staticmethod
	def rob_1(nums):
		dp1,dp2 = 0,0
		# each step choose the max amount we can get based on
		# i-1 and i-2 index 
		for num in nums:
			dp1,dp2 = dp2, max(dp2,dp1+num)
		return dp2

if __name__ == "__main__":
	s = Solution()

	lst = [2,3,2]
	print( s.rob(lst) )

	lst = [1,2,3,1]
	print( s.rob(lst) )

	lst = [0]
	print( s.rob(lst) )