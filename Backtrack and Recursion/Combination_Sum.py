"""
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should 
be a unique set of numbers.

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

"""
T = O( 9!*k/(9-k)! )
at first step we have 9 choice, then 8 then 7 and so on, in worst case if 
n = 99...(9 times) then we have to try all nPk permutation
for each permutation we copy k elements to result thus nPk * k
"""

class Solution:
	def combinationSum3(self, k, n):
		# to record all the combinations 
		result = []

		# a recursive function to backtrack and for each input comb try out 
		# all possible comnination starting from start
		def backtrack(n,comb,start):
			if n == 0 and len(comb) == k:
				# combination satisfy requirement
				result.append(comb.copy())
				return
				
			if n < 0 and len(comb) == k:
				# scope exceeded, backtrack
				return
			
			# iterrate from start+1 to 9
			for i in range(start,9):
				num = i+1
				# append each num to current combination and proceed
				# after choosing num as current char we can choose starting
				# from start+1 to 9 for next combination
				comb.append(num)
				backtrack(n-num,comb,num)
				# pop the current element from comb so that after return another
				# element can take its position
				comb.pop()
				
		backtrack(n,[],0)
		return result