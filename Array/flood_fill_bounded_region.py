def Fill_Bounded_Region(matrix):
	row,col = len(matrix), len(matrix[0])
	
	# check on all boundary points of row
	for r in range(row):
		Mark(matrix,r,0)
		Mark(matrix,r,col-1)

	for c in range(col):
		Mark(matrix,0,c)
		Mark(matrix,row-1,c)

	for i in range(row):
		for j in range(col):
			if matrix[i][j] == '$':
				matrix[i][j] = 'o'
			else:
				matrix[i][j] = 'x'

def Mark(matrix,row,col):
	stack = [ (row,col) ]

	while stack:
		r,c = stack.pop()

		# if its x then move on
		if matrix[r][c] != 'o':
			continue

		# if its a 'o' then flood fill all other cell of 'o' adj to it
		# mark them with diff symbol, these cell will remain 'o' in end rest 
		# all will get converted to 'x'
		matrix[r][c] = '$'
		
		if r > 0:
			stack.append( (r-1,c) )
		if r < len(matrix)-1:
			stack.append( (r+1,c) )
		if c > 0:
			stack.append( (r,c-1) )
		if c < len(matrix[0])-1:
			stack.append( (r,c+1) )

if __name__ == "__main__":
	"""
		fill the region bounded by x, like here three 'o' get converted to 'x' 
	"""
	matrix = [
		['x','x','x','x'],
		['x','o','o','x'],
		['x','x','o','x'],
		['x','o','x','x']
	]

	Fill_Bounded_Region(matrix)

	for row in matrix:
		print(row)