def kadane(lst):
	"""
	kadane algorithm : return max sum of contiguous segment with indexes
	return : (max_sum, index_start, index_end) zero based index
	"""
	n = len(lst)
	sumSofar = sumEndingHere = 0
	a,b = 0,0	# index of that contiguous segment
	s = 0		# index  that stores the position where new positive seg starts
				# in case this new positive seg is greater than prev than a = s

	for i in range(n):
		sumEndingHere = sumEndingHere + lst[i]
		if sumEndingHere < 0:
			sumEndingHere = 0
			s = i+1
			continue
		if sumSofar < sumEndingHere:
			sumSofar = sumEndingHere
			a = s
			b = i

	if sumSofar == 0:
		m = max(lst)
		a = b = lst.index(m)
		return (m,a,b)
	else:
		return (sumSofar,a,b)

def max_sum_submatrix(matrix):
	"""
	return max sub matrix sum in format
	( (row,col : for top left corner) , (row, col : for bottom right corner), Total_sum)
	"""
	row = len(matrix)
	col = len(matrix[0])
	total_sum = 0
	left_index = right_index = top_index = down_index = 0

	for left in range(col):
		# initializing temp array and updating on every update of right
		temp = [0]*row
		for right in range(left,col):
			
			for i in range(row):
				temp[i] += matrix[i][right]
			
			tup = kadane( temp )	# returns a tuple (max_sum, left_index, right_index)
			if total_sum < tup[0]:
				total_sum = tup[0]
				left_index = left
				right_index = right
				top_index = tup[1]
				down_index = tup[2]
	return ( (top_index,left_index),(down_index,right_index), total_sum )
	# ( (row,col : for top left corner) , (row, col : for bottom right corner), Total_sum)

if __name__ == "__main__":
	matrix = [
		[ 1,  2, -1, -4, -20], 
    	[-8, -3,  4,  2,  1 ],  
    	[ 3,  8, 10,  1,  3 ],  
    	[-4, -1,  1,  7, -6 ]
	]
	result = max_sum_submatrix( matrix )
	print("In zero based index")
	print( "top-left coordinates: ",result[0][0], result[0][1] )
	print( "bottom-right coordinates: ",result[1][0], result[1][1] )
	print( "Max sum : ",result[2] )