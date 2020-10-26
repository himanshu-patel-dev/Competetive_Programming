"""
Given an array of n integers nums, a 132 pattern is a subsequence of three 
integers nums[i], nums[j] and nums[k] such that 
i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.


n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109

"""

"""
Leetcode: https://leetcode.com/problems/132-pattern/solution/

for this type of problem of three pointer try fixing the middle out of three

1. Get i:
Precalculate the array min_value which have min value 
seen from 0 to j for each index j, thus for each nums[j] we can have nums[i] as
min possible value in left of j (i<j)
Note: nums[i] = min_value[j]

2. Get j
for j we  iterate the array from back and keep checking

3. Get k
Note: nums[k] = stack top

for each j we need k such that nums[k] < nums[j] and nums[k] > nums[i]
for this we maintain a stack which have reverse sorted elements [10,6,5,5,2,1]
to the right of nums[j]
(we dont need to sort it get sorted automatically as per algo)

when we see stack top is less than or equal to min_value[j] then we keep poping 
form stack as these are value less than or equal to nums[i] and hence is of no use

as soon we get a value of stack top as greater than nums[i] we check if its less
than nums[j] if not we push the current ele to stack and proceed to next ele

else we found a match and return true
"""

class Solution:
	def find132pattern(self, nums):
		n = len(nums)
		
		if n < 3:
			return False
		
		# get the min value in 0 to i range of nums in min_value
		min_value = [0]*n
		min_value[0] = nums[0]
		for i in range(1,n):
			min_value[i] = min( min_value[i-1], nums[i] )
		
		stack = [] 
		for j in range(n-1,0,-1):
			if nums[j] <= min_value[j]:
				continue
				
			while stack and stack[-1] <= min_value[j]:
				stack.pop()
				
			if stack and stack[-1] < nums[j]:
				return True
			
			stack.append(nums[j])
		
		return False
		
if __name__ == "__main__":
	s = Solution()

	lst = [1,2,3,4]
	print( s.find132pattern(lst) )

	lst = [3,1,4,2]
	print( s.find132pattern(lst) )

	lst = [-1,3,2,0]
	print( s.find132pattern(lst) )