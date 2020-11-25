'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators 
and empty spaces . The integer division should truncate toward zero.
'''

'''
T = O(n)
S = O(1)
LeetCode: https://leetcode.com/problems/basic-calculator-ii/solution/
'''
class Solution:
	def calculate(self, s: str) -> int:
		prevNumber = currNumber = result = 0
		operator = '+'

		if not s:
			return 0

		for i,c in enumerate(s):
			if c.isdigit():
				currNumber = currNumber*10 + int(c)
			
			if not c.isdigit() and c != ' ' or i == len(s)-1:
				if operator == '+':
					result += prevNumber
					prevNumber = currNumber
				elif operator == '-':
					result += prevNumber
					prevNumber = -currNumber
				elif operator == '*':
					prevNumber = prevNumber * currNumber
				else:
					prevNumber = int(prevNumber / currNumber)

				currNumber = 0
				operator = c

		return result+prevNumber

if __name__ == "__main__":
	s = Solution()

	inp = "3+2*2"
	print( s.calculate(inp) )

	inp = "3/2"
	print( s.calculate(inp) )

	inp = " 3+5 / 2 "
	print( s.calculate(inp) )

	inp = "14-3/2"
	print( s.calculate(inp) )