def max_span(lst):
	"""
	for each index it gives the number of consecutive elements to its 
	left which are less than current element before we get first element
	greater than current element
	"""
	n = len(lst)
	result = [0]*n
	# for current element it holds the index prior to the 
	# current elemnt that are grater than current element 
	bigger_than = []

	for i in range(n):
		# until there is an element on stack which is 
		# smaller than current pop it out
		while bigger_than and lst[ bigger_than[-1] ] < lst[i]:
			bigger_than.pop()
		
		# if stack is not empty last element of it is greater 
		# than current take its index else else take -1 as index
		if bigger_than:
			j = bigger_than[-1]
		else:
			j = -1
		
		# for current element store the max span possible
		result[i] = i-j
		bigger_than.append(i)
	return result


if __name__ == "__main__":
	lst = [6,3,4,5,2]
	print( max_span(lst) )

	lst = [1,2,3,4,5]
	print( max_span(lst) )

	lst = [5,4,3,2,1]
	print( max_span(lst) )