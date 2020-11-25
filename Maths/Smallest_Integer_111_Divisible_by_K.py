'''
Given a positive integer K, you need to find the length of the smallest 
positive integer N such that N is divisible by K, and N only contains 
the digit 1.

Return the length of N. If there is no such N, return -1.

Note: N may not fit in a 64-bit signed integer.

Constraints:
1 <= K <= 105

'''

'''
Solution: LeetCode
https://leetcode.com/problems/smallest-integer-divisible-by-k/solution/


if we compute a formula in loop where rem = 0 initially
	rem = rem*10 + 1
then rem will grow like 1, 11, 111, 1111... and so on

but since N is very large and may not fit in integer range so better go 
with its modulo as N%K give same result as (rem of N with K)%k gives

N%K = ( a*K + rem )%K = ( (a*K)%K + rem%K)%K = (0 + rem)%K = rem
so we grow rem in pattern 1, 11, 111, 1111.. and so on


let K = 7

N		N Mod K		rem 			rem Mod K
1		1			1				1
11		4			(1*10+1)=11		4	
111		6			(4*10+1)=41		6
1111	1			(6*10+1)=61		5		
11111	2			(5*10+1)=51		2

Observe that the rem with N as well as rem of N is same so instead of storing N
sotore its rem and keep inc it in a way to produce pattern 1, 11, 111 ..

Now in rem can vary from 0 to K-1 thus in K steps we can get all possible rem
after this rem keep on repeating thus stop after this and return -1 

'''

class Solution:
	def smallestRepunitDivByK(self, K: int) -> int:
		if K%2 == 0:
			return -1

		rem = 0
		# loop K times
		for len in range(1,K+1):
			rem = (rem*10 + 1)%K

			if rem == 0:
				return len
		return -1

if __name__ == "__main__":
	s = Solution()

	K = 1
	# Output: 1
	print(s.smallestRepunitDivByK(K))

	K = 2
	# Output: -1
	print(s.smallestRepunitDivByK(K))

	K = 3
	# Output: 3
	print(s.smallestRepunitDivByK(K))
