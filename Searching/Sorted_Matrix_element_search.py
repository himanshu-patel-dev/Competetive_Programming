def matrix_search(matrix,target):
	""" 
	given a mattrix of sorted rows and cols find a given element 
	T = O(row + col)
	S = O(1)
	"""

	row = len(matrix)
	col = len(matrix[0])

	r,c = 0,col-1
	while r<row and c>=0:
		if matrix[r][c] == target:
			return True
		elif matrix[r][c] < target:
			r += 1
		else:
			c -= 1
	return False

if __name__ == "__main__":
	matrix = [
		[1,2,2,2,3,4],
		[1,2,3,3,4,5],
		[3,4,4,4,4,6],
		[4,5,6,7,8,9]
	]

	print( matrix_search(matrix,7) )
	print( matrix_search(matrix,13) )