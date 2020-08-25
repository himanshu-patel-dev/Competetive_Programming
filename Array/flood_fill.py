"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) 
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.

"""

class Solution:
	def orangesRotting(self, matrix: List[List[int]]) -> int:
		""" return min no of steps required to convert all fresh to rotten or -1 """
		from collections import deque
		fresh_count = 0
		rotten = deque()	# queue to maintain rotten oranges
		time = 0			# time taken for all fresh to rotten conversion
		row, col = len(matrix), len(matrix[0])
		for i in range(row):
			for j in range(col):
				# store index of all rotten oranges
				if matrix[i][j] == 2:
					rotten.append( (i,j,0) )
				# count no of fresh, this need to be zero in end
				if matrix[i][j] == 1:
					fresh_count += 1
		
		while rotten:
			# get from beggining the rotten ones, added newly rotten to end
			i,j,time = rotten.popleft()
			for p,q in [ (i+1,j), (i-1,j), (i,j-1), (i,j+1) ]:
				if 0 <= p < row and 0 <= q < col and matrix[p][q] == 1:
					matrix[p][q] = 2
					fresh_count -= 1
					# newly rotten add to end, last one will have max time attribute
					rotten.append( (p,q,time+1) )
		
		if fresh_count > 0:
			return -1
		else:
			return time
				
if __name__ == "__main__":
	grid = [[2,1,1],[1,1,0],[0,1,1]]
	s = Solution()
	print( s.orangesRotting(grid) )

	# The orange in the bottom left corner (row 2, column 0) is never rotten
	grid = [[2,1,1],[0,1,1],[1,0,1]]
	print( s.orangesRotting(grid) )

	# Since there are already no fresh oranges at minute 0
	grid = [[0,2]]
	print( s.orangesRotting(grid) )
