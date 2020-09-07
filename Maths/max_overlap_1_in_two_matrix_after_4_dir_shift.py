"""
Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.  
(A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any 
number of units), and place it on top of the other image.  After, the overlap of this 
translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Input: A = [[1,1,0],
			[0,1,0],
			[0,1,0]]
	   B = [[0,0,0],
			[0,1,1],
			[0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
"""

###  Solution  ###

"""
We filter out those cells with ones in both matrices, 
and then we apply the linear transformation to align the cells.

Now, the key insight is that all the cells in the same overlapping zone 
would share the same linear transformation vector.

We can then use the transformation vector V_ab as a key to group all the non-zero 
cells alignments between two matrices. Each group represents an overlapping zone. 
Naturally, the size of the overlapping zone would be the size of the group as well.
"""
from collections import defaultdict

class Solution:
	def coordinate_of_set_pixel(self,matrix):
		res = []
		n = len(matrix)
		for i in range(n):
			for j in range(n):
				if matrix[i][j]:
					res.append( (i,j) )
		return res

	def largestOverlap(self, A, B):
		set_A = self.coordinate_of_set_pixel(A)
		set_B = self.coordinate_of_set_pixel(B)

		count_same_transformation_vector = defaultdict(int)

		for a_x, a_y in set_A:
			for b_x, b_y in set_B:
				vector = (b_x-a_x, b_y-a_y)
				count_same_transformation_vector[vector] += 1

		result = 0
		for v in count_same_transformation_vector.values():
			result = max(result,v)
	
		return result

if __name__ == "__main__":
	A = [[1,1,0],
		[0,1,0],
		[0,1,0]]
	B = [[0,0,0],
		[0,1,1],
		[0,0,1]]

	s = Solution()
	print( s.largestOverlap(A,B) )
