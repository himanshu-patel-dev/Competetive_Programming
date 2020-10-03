"""
Given an array of integers nums and an integer k, return the number 
of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following 
are true:

0 <= i, j < nums.length
i != j
a <= b
b - a == k

Constraints:
1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107

"""

class Solution:
	def findPairs(self, nums, k):    
		count = 0     
		
		# if k is 0 then ele hit them self while checking in hash
		if k == 0:
			first_seen = set()
			sec_seen = set()
			
			for ele in nums:
				# if same ele is duplicate then inc count by 1
				if ele in first_seen and ele not in sec_seen:
					count += 1
					sec_seen.add(ele)
				first_seen.add(ele)
			return count
		
		# when k != 0
		# remove duplicate elements as they produce duplicate 
		# result which is not required here
		nums = set(nums)   
		
		for ele in nums:
			if ele + k in nums:
				count += 1
		return count

if __name__ == "__main__":
	s = Solution()

	nums = [-1,-2,-3]
	k = 1
	print( s.findPairs(nums,k) )

	nums = [1,2,4,4,3,3,0,9,2,3]
	k = 3
	print( s.findPairs(nums,k) )

	nums = [1,3,1,5,4]
	k = 0
	print( s.findPairs(nums,k) )

	nums = [1,2,3,4,5]
	k = 1
	print( s.findPairs(nums,k) )

	nums = [3,1,4,1,5]
	k = 1
	print( s.findPairs(nums,k) )
