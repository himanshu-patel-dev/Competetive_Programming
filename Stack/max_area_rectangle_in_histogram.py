def max_area_histogram(lst):
	"""
	return the max area rectangle possible in a histogram represented in list
	"""
	stack = []
	max_area = 0
	current_index = 0
	n = len(lst)

	# iteratet over all elements
	while current_index < n:
		# if next element is greater than top element push it on stack 
		if len(stack) == 0 or lst[stack[-1]] <= lst[current_index]:
			stack.append( current_index )
			current_index += 1

		# else keep poping element from stack till we get an element 
		# whose hight is less than current 
		else:
			height = lst[ stack.pop() ]
			if len(stack) == 0:
				width = current_index
			else:
				# width is calculated as the elements btw current_index and stack[-1]
				# elements btw two index i and j are j-i-1 (excluding i and j)
				# including i and j we write j-i+1
				width = current_index - stack[-1] - 1
			area = height * width
			max_area = max( max_area, area )
	
	# do the same with elements left out in stack
	while len(stack) != 0:
		height = lst[ stack.pop() ]
		if len(stack) == 0:
			width = current_index
		else:
			width = current_index - stack[-1] - 1
		area = height * width
		max_area = max( max_area, area )

	return max_area

if __name__ == "__main__":
	lst = [6, 2, 5, 4, 5, 1, 6]	# ans = 12
	# lst = [2,1,2,3,1]				# ans = 5
	print( max_area_histogram(lst) )