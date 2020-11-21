'''
Given an array of digits, you can write numbers using each digits[i] as many 
times as we want.  For example, if digits = ['1','3','5'], we may write numbers 
such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than 
or equal to a given integer n.

Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
1 <= n <= 109
'''

'''
Solution:

Now, say we are to write a valid K digit number from left to right. 
For example, N = 2345, K = 4, and D = '1', '2', ..., '9'. Let's consider 
what happens when we write the first digit.

If the first digit we write is less than the first digit of N, then we could 
write any numbers after, for a total of len(D)^{K-1} valid numbers from this 
one-digit prefix. In our example, if we start with 1, we could write any of the 
numbers 1111 to 1999 from this prefix.

If the first digit we write is the same, then we require that the next digit we 
write is equal to or lower than the next digit in N. In our example (with N = 2345), 
if we start with 2, the next digit we write must be 3 or less.

We can't write a larger digit, because if we started with eg. 3, then even a number 
of 3000 is definitely larger than N.

Let dp[i] be the number of ways to write a valid number if N became N[i], 
N[i+1], .... For example, if N = 2345, then dp[0] would be the number of valid 
numbers at most 2345, dp[1] would be the ones at most 345, dp[2] would be the ones 
at most 45, and dp[3] would be the ones at most 5.

Then, by our reasoning above, 
dp[i] = (number of d in D with d < S[i]) * ((D.length) ** (K-i-1)), 
plus dp[i+1] if S[i] is in D.

In this way we are able to do get dp[0] which gives total number possible we consider
first digit of N i.e. N[0] then second digit N[1] and so on...

but in the end we add dp[0] with

extra = sum(len(D) ** i for i in range(1, K))

which shows that if dp[0] numbers are possible with K digit then there are some more
numbers available with less than K digits (from 1 to K-1) thus loop runs in 'extra'
from 1 to K-1.
'''

class Solution:
	def atMostNGivenDigitSet(self, D, N):
		S = str(N)
		K = len(S)
		dp = [0] * K + [1]
		# dp[i] = total number of valid integers if N was "N[i:]"

		for i in range(K-1, -1, -1):
			# Compute dp[i]

			for d in D:
				if d < S[i]:
					dp[i] += len(D) ** (K-i-1)
				elif d == S[i]:
					dp[i] += dp[i+1]

		return dp[0] + sum(len(D) ** i for i in range(1, K))

if __name__ == "__main__":
	s = Solution()
	
	lst = ["1","3","5","7"]
	n = 100
	print(s.atMostNGivenDigitSet(lst,n))

	lst = ["1","4","9"]
	n = 1000000000
	print(s.atMostNGivenDigitSet(lst,n))

	lst = ['7']
	n = 8
	print(s.atMostNGivenDigitSet(lst,n))

	lst = ['1','2','3','4','5','6','7','8','9']
	n = 2345
	print(s.atMostNGivenDigitSet(lst,n))

	lst = ['1','7']
	n = 200
	print(s.atMostNGivenDigitSet(lst,n))
