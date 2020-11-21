'''
Let's call any (contiguous) subarray B (of A) a mountain if the following 
properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that 
B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 
Return 0 if there is no mountain.

0 <= A.length <= 10000
0 <= A[i] <= 10000

Can you solve it using only one pass?
Can you solve it in O(1) space?
'''

'''
Solution:

Let us traverse our numbers and keep two variables: state and length, where:

1. state is current state of our mountain: it is 0 in the beginning and 
also means that we can not start our mountain from given index. state equal 
to 1 means, that we are on increasing phase of our mountain and state equal 
2 means, that we are on decreasing phase of our mountain.

2. length is current length of mountain built so far. Now, we need to 
carefully look at our states and see what we need to do in one or another 
situation:

1. If state is equal to 0 or 1 and next element is more than current, 
it means we can continue to build increasing phase of mountain: so, we put 
state equal to 1 and increase length by 1.

2. If state is equal to 2 and next element is more then curren, it means, 
that previous mountain just finished and we are currently buildind next 
mountain, for examle in 0,1,0,2,0: first mountain is 0,1,0 and second is 
0,2,0. In this case we already build 2 elements of new mountain (mountains
have 1 common element), so we put length = 2 and state = 1.

3. If state is equal to 1 or 2 and next element is less than current, 
it means that we are on the decreasing phase of mountain: we put state = 2 
and also increase length by 1. Note, that only here we need to update max_len, 
because our mountain is legible on this stage.

4. Finally, if we have some other option: it is either next element is equal 
to current, or we have state 0 and next element is less than previous, 
we need put our state and length to values as we just started.
'''

class Solution:
	''' T = O(n) and S = O(1) '''
	def longestMountain(self, A):
		state, length = 0, 1
		n, max_len = len(A), 0 

		for i in range(n-1):
			if state in [0,1] and A[i] < A[i+1]:
				state, length = 1, length+1
			elif state == 2 and A[i] < A[i+1]:
				state, length = 1, 2
			elif state in [1,2] and A[i] > A[i+1]:
				state, length = 2, length + 1
				max_len = max(max_len, length)
			else:
				state, length = 0, 1
		return max_len


if __name__ == "__main__":
	s = Solution()

	lst = [2,1,4,7,3,2,5]
	print(s.longestMountain(lst))

	lst = [2,2,2]
	print(s.longestMountain(lst))

	lst = [1,2,1]
	print(s.longestMountain(lst))

	lst = [0,2,2]
	print(s.longestMountain(lst))

	lst = [2,3,3,2,0,2]
	print(s.longestMountain(lst))

