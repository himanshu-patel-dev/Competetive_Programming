'''
You are given an array of integers nums, there is a sliding window of 
size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding 
window moves right by one position.

Return the max sliding window.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:
Input: nums = [9,11], k = 2
Output: [11]

Example 5:
Input: nums = [4,-2], k = 2
Output: [4]
'''

'''
T = O(N) each ele is push or poped only once
S = O(N)
'''

from collections import deque
class Solution:
	def maxSlidingWindow(self, nums, k):
		q = deque()		# it contains index of ele from nums with max ele of window at front
		res = []		# it is the result we return

		for i in range(len(nums)):
			# if ele at front of q is out of window of k elements
			if q and i-q[0] == k:
				q.popleft()

			# remove all ele from q which are smaller than curr ele
			while q and nums[q[-1]] < nums[i]:
				q.pop()

			# append curr ele's index to q
			q.append(i)

			# add front of q to result if window is larger than or equal to k
			if i >= k-1:
				res.append( nums[q[0]] )			

		return res

if __name__ == "__main__":
	s = Solution()

	nums = [1,3,-1,-3,5,3,6,7]
	k = 3
	print( s.maxSlidingWindow(nums,k) )

	nums = [1]
	k = 1
	print( s.maxSlidingWindow(nums,k) )

	nums = [1,-1]
	k = 1
	print( s.maxSlidingWindow(nums,k) )

	nums = [9,11]
	k = 2
	print( s.maxSlidingWindow(nums,k) )

	nums = [4,2]
	k = 2
	print( s.maxSlidingWindow(nums,k) )
