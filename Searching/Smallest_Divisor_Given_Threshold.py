'''
Given an array of integers nums and an integer threshold, we will choose a 
positive integer divisor and divide all the array by it and sum the result 
of the division. Find the smallest divisor such that the result mentioned 
above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal 
to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6

Examples:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 
5 the sum will be 5 (1+1+1+2).


Input: nums = [2,3,5,7,11], threshold = 11
Output: 3


Input: nums = [19], threshold = 5
Output: 4
'''

'''
Solution: T = O( nlogm ) 

n-> Total no of ele in list 
m-> range of min to max in given list

n -> 10^6
m -> 10^4
T = O( 10^4 * log(10^6)) = O( 10^4 * 20 ) = 2 * 10^5

S = O(n) to store all ele after divide and return sum
'''

class Solution:
	def smallestDivisor(self, nums, threshold):
		# min should be floored divison so that min value is not zero
		mi = ( sum(nums) + threshold - 1 )//threshold
		# if max is not as pre constraints
		mx = max(nums)
		valid_divisor = []

		# make a binary search in range to select valid divisor
		while mi <= mx:
			mid = (mi+mx)//2
			

			res = self.floorDivison(nums,mid)
			if res > threshold:
				# inc the divisor so that floorDivison is within threshold
				mi = mid+1
			else:
				# dec the divisor so that floorDivison is within threshold
				valid_divisor.append(mid)
				mx = mid-1
		# return min of valid divisor
		return min(valid_divisor)

	@staticmethod
	def floorDivison(nums,divisor):
		return sum([(ele + divisor - 1)//divisor  for ele in nums])

if __name__ == "__main__":
	s = Solution()

	lst = [1,2,5,9]
	t = 6
	print( s.smallestDivisor(lst, t) )

	lst = [2,3,5,7,11]
	t = 11
	print( s.smallestDivisor(lst, t) )

	lst = [19]
	t = 5
	print( s.smallestDivisor(lst, t) )
