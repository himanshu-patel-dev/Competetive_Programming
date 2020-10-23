"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
"""

"""
Your algorithm should run in O(n) time and uses constant extra space.

1. check is one is not present then that is the ans
2. In array of len n we can have ans possible in range 1 to n+1 
3. (no less than 1 and not bigger than n+1 if all ele are dist and from 1 to n)
4. convert all ele not in range 1 to n to 1 (as 1 is already present and duplicate do not affect)
5. mark each element present or no based on index (if present mark sign of that index as neg)
6. return first i+1 where ele at index i is not neg
7. if all neg return n+1

"""

class Solution:
	def firstMissingPositive(self, nums):
		n = len(nums)
		
		# if one do not exist return 1
		if 1 not in nums:
			return 1
		
		# make sure every number is in range 1 to n if not 
		# change it to one, since one is already present it 
		# do not matter it some duplicate also occur in array
		mi,mx = 1, n
		nums = [ ele if mi<=ele<=mx else 1 for ele in nums]
		
		# mark each element as present using index from array
		for i in range(n):
			# changing range to 0 to n-1
			index = abs(nums[i])-1
			# mark that element's index as negative, thus 
			# duplicate do not affect answer
			if nums[index] > 0:
				nums[index] = -nums[index]
		
		# if any index found positive means that ele is not present
		for i in range(n):
			if nums[i]>0:
				return i+1
		return n+1

if __name__ == "__main__":
	s = Solution()
	
	lst = [1,2,0]
	print( s.firstMissingPositive(lst) )

	lst = [3,4,-1,1]
	print( s.firstMissingPositive(lst) )
	
	lst = [7,8,9,11,12]
	print( s.firstMissingPositive(lst) )
	