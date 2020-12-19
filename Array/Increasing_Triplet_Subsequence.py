'''
Given an integer array nums, return true if there exists a triple of 
indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
 
Follow up: Could you implement a solution that runs in O(n) time complexity 
and O(1) space complexity?
'''

class Solution:
	'''
		T = O(3n) = O(n)
		S = O(2n) = O(n)
	'''
	def increasingTriplet(self, nums):
		if len(nums) < 3:
			return False
		
		n = len(nums)		
		min_lst = [float('inf')]*n
		max_lst = [float('-inf')]*n
		
		# take first ele as min and last as max
		mi, mx = nums[0], nums[n-1]
		
		for i in range(1, n):
			# fill min_lst such that each ele show the 
			# min ele available in its left
			min_lst[i] = mi 
			# fill max_lst such that each index show the 
			# max ele to its right
			max_lst[n-1-i] = mx
			
			mi = min(mi, nums[i])
			mx = max(mx, nums[n-1-i])
			
		# if at any index min ele is less than current and max 
		# is more than current return true
		for i in range(1,n-1):
			if min_lst[i] < nums[i] < max_lst[i]:
				return True
		return False

class Solution:
	'''
		T = O(n)
		S = O(1)
	'''
	def increasingTriplet(self, nums):
		if len(nums) < 3:
			return False
		
		n = len(nums)
		
		left, mid = float('inf'), float('inf')
		
		for ele in nums:
			
			if ele <= left: left = ele      # if ele <= left then dec left further
			elif ele <= mid: mid = ele      # if ele <= mid but strictly greater than left update mid
			else: return True               # if ele is more than mid then we got triplet return True
			
		return False

if __name__ == "__main__":
	s = Solution()

	print(s.increasingTriplet([1,2,3,4,5]))		# true
	print(s.increasingTriplet([5,4,3,2,1]))		# false
	print(s.increasingTriplet([2,1,5,0,4,6]))	# true
