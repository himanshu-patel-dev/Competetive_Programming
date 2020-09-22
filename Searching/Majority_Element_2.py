"""
Given an integer array of size n, find all elements that appear more 
than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

"""

"""
Solution:
T = O(n) and S = O(1)

There can be at most one majority element which is more than ⌊n/2⌋ times.
There can be at most two majority elements which are more than ⌊n/3⌋ times.
There can be at most three majority elements which are more than ⌊n/4⌋ times.

1. If the current element is equal to one of the potential candidate, the count for 
that candidate is increased while leaving the count of the other candidate as it is.

2. If the counter reaches zero, the candidate associated with that counter will 
be replaced with the next element if the next element is not equal to the other 
candidate as well.

3. Both counters are decremented only when the current element is different from 
both candidates.

"""

class Solution:
	def majorityElement(self, nums):
		count1, count2, candidate1, candidate2 = 0,0,None,None

		# pass one
		for ele in nums:
			if ele == candidate1:
				count1 += 1
			elif ele == candidate2:
				count2 += 1
			elif count1 == 0:
				candidate1 = ele
				count1 += 1
			elif count2 == 0:
				candidate2 = ele
				count2 += 1
			else:
				count1 -= 1
				count2 -= 1
		
		# pass two
		result = []
		n = len(nums)
		for ele in [candidate1,candidate2]:
			if nums.count(ele) > n//3:
				result.append(ele)
		
		return result

if __name__ == "__main__":
	s = Solution()

	lst = [1,1,1,3,3,2,2,2]
	print( s.majorityElement(lst) )

	lst = [3,2,3]
	print( s.majorityElement(lst) )