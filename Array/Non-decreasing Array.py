'''
Given an array nums with n integers, your task is to check if it could become 
non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for 
every i (0-based) such that (0 <= i <= n - 2).

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
'''

class Solution:
	'''
		T = O(n)
		S = O(1)

		Whenever an anamoly occur then we can either decrease the current element
		to match the next element and array remain non-dec
		Else we can increase the next ele to match the current element

		Quest: when to do what?
		dec current element when prev and next ele (wrt current ele) are non-dec
		(first <= third) else increase the next element upcoming element. 
	'''
	def checkPossibility(self, nums):
		count = 0
		n = len(nums)
		
		for i in range(n-1): 
			# if anomaly occures at index i and i+1
			if nums[i] > nums[i+1]:
				
				# if we can decrease i and make nums non-dec
				if i == 0 or nums[i-1] <= nums[i+1]:
					nums[i] = nums[i+1]
		
				# else we can increase i+1 and make nums non-dec
				else:
					nums[i+1] = nums[i]
				count += 1
				
		return count <= 1

if __name__ == "__main__":
	s = Solution()

	nums = [4,2,3]
	print(s.checkPossibility(nums))

	nums = [4,2,1]
	print(s.checkPossibility(nums))
