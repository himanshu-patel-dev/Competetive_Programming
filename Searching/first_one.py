def position_of_first_one(lst):
	""" 
	return the position of first 1 in very long string of 0000...1111... 
	number of length of string is not known and we need a O(logn) algorithm
	"""
	low, high = 0, 1

	# high = 1,2,4,8,16 and so on .... takes log(n) for getting to segment 
	# which contains a junction bw 0s as and 1s
	while lst[high] == 0:
		low = high
		high = 2*high

	# do a binary search approch to get the position of first 1
	# this also takes log(n) time
	while low <= high:
		mid = (low+high)//2

		# if mid is the index of first 1
		if lst[mid] == 1 and (mid == 0 or lst[mid-1] == 0):
			return mid		

		# first 1 lies to left of mid
		if lst[mid] == 1:
			high = mid -1
		# first 1 lies to right of mid
		else:
			low = mid + 1
	return mid

def position_of_first_zero(lst):
	""" 
	return the position of first 0 in very long string of 1111...0000... 
	number of length of string is not known and we need a O(logn) algorithm
	"""
	low, high = 0, 1

	# high = 1,2,4,8,16 and so on .... takes log(n) for getting to segment 
	# which contains a junction bw 1 as and 0s
	while lst[high] == 1:
		low = high
		high = 2*high

	# do a binary search approch to get the position of first 0
	# this also takes log(n) time
	while low <= high:
		mid = (low+high)//2

		# if mid is the index of first 0
		if lst[mid] == 0 and (mid == 0 or lst[mid-1] == 1):
			return mid		

		# first 0 lies to left of mid
		if lst[mid] == 0:
			high = mid -1
		# first 0 lies to right of mid
		else:
			low = mid + 1
	return -1

if __name__ == "__main__":
	arr = [ 0, 0, 1, 1, 1, 1 ] 
	print( "Index = ", position_of_first_one(arr) )

	arr = [ 1, 1, 1, 1 ] 
	print( "Index = ", position_of_first_one(arr) )

	arr = [1,1,1,1,0,0,0]
	print( "Index = ", position_of_first_zero(arr) )

	arr = [0,0,0,0]
	print( "Index = ", position_of_first_zero(arr) )

	# this will give index out of bound as zero will not be seen and high 
	# will keep growing
	# arr = [ 1, 1, 1, 1 ] 
	# print( "Index = ", position_of_first_zero(arr) )
