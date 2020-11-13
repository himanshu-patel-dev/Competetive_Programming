"""
Given an array of distinct integers candidates and a target integer 
target, return a list of all unique combinations of candidates where 
the chosen numbers sum to target. You may return the combinations in 
any order.

The same number may be chosen from candidates an unlimited number of 
times. Two combinations are unique if the frequency of at least one of 
the chosen numbers is different.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500


"""
class Solution:
	def combinationSum(self, candidates, target):
		mi = min(candidates)
		n = len(candidates)
		candidates.sort()

		self.result = []
		path = []
		self.backtracking(candidates,0,n,mi,target,path)
		return list(map(list,self.result))

	def backtracking(self,candidates,start,end,mi,target,path):
		if target == 0:
			self.result.append( path.copy() )
			return

		if target < mi:
			return

		for i in range(start,end):
			ele = candidates[i]
			if ele > target:
				return
			self.backtracking(candidates,i,end,mi,target-ele,path+[ele])

if __name__ == "__main__":
	s = Solution()

	lst = [2,3,5]
	target = 8
	print( s.combinationSum(lst,target) )

	lst = [2,3,6,7]
	target = 7
	print( s.combinationSum(lst,target) )

	lst = [2]
	target = 1
	print( s.combinationSum(lst,target) )

	lst = [1]
	target = 1
	print( s.combinationSum(lst,target) )

	lst = [1]
	target = 2
	print( s.combinationSum(lst,target) )