def sliding_window_all_value(array,w):
	n = len(array)
	if n < w or w < 1:
		raise "size of window greater than array or less than 1"
	
	value = sum(array[:w])
	result = [value]
	for i in range(1,n-w+1):
		value += array[i+w-1] - array[i-1]
		result.append(value)
	return result


if __name__ == "__main__":
	# array for calculating sliding window
	array = [1,2,3,4,5]
	# size of sliding window
	w = 4

	print( sliding_window_all_value(array,w) )
