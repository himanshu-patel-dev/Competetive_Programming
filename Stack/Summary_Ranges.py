"""
You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in 
the array exactly. That is, each element of nums is covered by exactly one 
of the ranges, and there is no integer x such that x is in one of the ranges 
but not in nums.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

"""

class Solution:
	def summaryRanges(self, nums):
		if not nums:
			return []

		stack = []
		res = []

		for ele in nums:
			# if stack is empty just put the current ele and continue
			if not stack:
				stack.append(ele)
				continue

			# if its not empty compare the top most ele from incoming ele
			# if both consecutive them push to stack and continue
			if stack[-1] + 1 == ele:
				stack.append(ele)
				continue

			# if not consecutive then push the stack content till now to result lst
			if len(stack) > 1:
				res.append( f"{stack[0]}->{stack[-1]}" )
			else:
			# len of stack == 1
				res.append( f"{stack[0]}" )
			stack = [ele]

		if len(stack) > 1:
			res.append( f"{stack[0]}->{stack[-1]}" )
		else:
		# len of stack == 1
			res.append( f"{stack[0]}" )

		return res

if __name__ == "__main__":
	s = Solution()

	nums = [0,1,2,4,5,7]
	print( s.summaryRanges(nums) )

	nums = [0,2,3,4,6,8,9]
	print( s.summaryRanges(nums) )

	nums = []
	print( s.summaryRanges(nums) )

	nums = [-1]
	print( s.summaryRanges(nums) )

	nums = [0]
	print( s.summaryRanges(nums) )
