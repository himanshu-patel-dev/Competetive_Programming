def max_area_histogram(lst):
	stack = []
	max_area = 0
	index = 0
	n = len(lst)
	while index < n:
		if len(stack) == 0 or lst[stack[-1]] <= lst[index]:
			stack.append( index )
			index += 1
		else:
			topIndex = stack.pop()
			if len(stack) == 0:
				area = lst[topIndex] * index
			else:
				area = lst[topIndex] * ( index - stack[-1] - 1)
			max_area = max( max_area, area )
	while len(stack) != 0:
		topIndex = stack.pop()
		if len(stack) == 0:
			area = lst[topIndex] * index
		else:
			area = lst[topIndex] * ( index - stack[-1] - 1) 
		max_area = max( max_area, area )
	return max_area

def max_size_rectangle_of_1_in_matrix( matrix ):
	row = len(matrix)
	col = len(matrix[0])

	# made special matrix which have rows as histograms
	for i in range(1,row):
		for j in range(col):
			if matrix[i][j]:
				matrix[i][j] = 1 + matrix[i-1][j]
	 
	result = max_area_histogram( matrix[0] )
	for i in range(1,row):
		result = max(result, max_area_histogram(matrix[i]) )
	
	# for row in matrix:
	# 	print(row)

	return result

if __name__ == "__main__":
	matrix = [
		[1,0,0,1,1,1],
		[1,0,1,1,0,1],
		[0,1,1,1,1,1],
		[0,0,1,1,1,1]
	]

	print( max_size_rectangle_of_1_in_matrix( matrix ) )