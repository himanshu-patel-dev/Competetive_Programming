'''
Given an array A of integers, for each integer A[i] we need to choose either 
x = -K or x = K, and add x to A[i] (only once).
After this process, we have some array B.
Return the smallest possible difference between the maximum value of B and the 
minimum value of B.

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
'''

class Solution:
	def smallestRangeII(self, A, K):
		A.sort()
		mi, mx = A[0], A[-1]
		res = mx-mi
		
		for i in range(len(A)-1):
			a,b = A[i], A[i+1]
			res = min(res, max( mx-K, a+K ) - min( mi+K, b-K) )
		
		return res
