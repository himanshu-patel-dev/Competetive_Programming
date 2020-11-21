'''
Leetcode: https://leetcode.com/problems/mirror-reflection/

There is a special square room with mirrors on each of the four walls.  
Except for the southwest corner, there are receptors on each of the remaining 
corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner 
first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed 
that the ray will meet a receptor eventually.)

Note:

1 <= p <= 1000
0 <= q <= p
'''

'''
Solution:

Video in Maths (youtube: )
T = O(log(max(p,q)))
S = O(1)
'''

class Solution:
	def mirrorReflection(self, p: int, q: int) -> int:
		if p == 0 or q == 0:
			return 0
		
		from math import gcd
		# try to solve a*p = b*q = lcm of p.q 
		# where a and b are unknown but should be least possible
		lcm = p*q//gcd(p,q)
		
		# the least integer which when multiplied to p give lcm
		a = lcm//p
		# the least integer which when multiplied to q give lcm
		b = lcm//q
		
		# if we try solving eq further
		# a = q//gcd(p,q)
		# b = p//gcd(p,q)
		
		# if no of q required ar even in number then ray finishes at 
		if b%2 == 0:
			return 2
		elif a%2 == 0:
			return 0
		else:
			return 1

if __name__ == "__main__":
	s = Solution()
	print( s.mirrorReflection(2,1) )
