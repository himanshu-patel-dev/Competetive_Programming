"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves 
at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. Two 
asteroids moving in the same direction will never meet.
"""

class Solution:
	def asteroidCollision(self, asteroids):
		stack = []

		for ele in asteroids:
			
			eleLeft = True

			# both are of different sign and ele moves to 
			# left and stack[-1] to right then only coll occur
			while stack and ele < 0 < stack[-1]:

				# in stack have lesser magnitude than ele
				if stack[-1] < -ele:
					stack.pop()
					continue

				#  both have same mag then both exp
				if stack[-1] == -ele:
					stack.pop()
				
				# skip the ele from entering into stack as its 
				# either get destroyed or both get destroyed
				eleLeft = False
				break
	
			if eleLeft:
				stack.append(ele)

		# return result as stack
		return stack


if __name__ == "__main__":
	s = Solution()

	lst = [5,10,-5]
	print( s.asteroidCollision(lst) )

	lst = [8,-8]
	print( s.asteroidCollision(lst) )

	lst = [10,2,-5]
	print( s.asteroidCollision(lst) )

	lst = [-2,-1,1,2]
	print( s.asteroidCollision(lst) )