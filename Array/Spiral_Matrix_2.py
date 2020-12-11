'''
Given a positive integer n, generate an n x n matrix filled 
with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
'''

class Solution:
	def generateMatrix(self, n):
		matrix = [ [0]*n for i in range(n) ]
		
		counter = 1
		row_min, row_max = 0, n-1
		col_min, col_max = 0, n-1
		
		while row_min <= row_max:

			# upper row in spiral
			for c_u in range(col_min, col_max+1):
				matrix[row_min][c_u] = counter
				counter += 1

			# # right most col in spiral
			for r_r in range(row_min+1, row_max):
				matrix[r_r][col_max] = counter
				counter += 1

			# # lower row in spiral
			for c_l in range(col_max, col_min,-1):
				matrix[row_max][c_l] = counter
				counter += 1

			# # left most row in spiral 
			for r in range(col_max,col_min,-1):
			    matrix[r][col_min] = counter
			    counter += 1
				
			row_min, row_max = row_min+1, row_max-1
			col_min, col_max = col_min+1, col_max-1
			
		return matrix

if __name__ == "__main__":
	s = Solution()

	for r in s.generateMatrix(3):
		print(r)


	for r in s.generateMatrix(4):
		print(r)

	for r in s.generateMatrix(5):
		print(r)
