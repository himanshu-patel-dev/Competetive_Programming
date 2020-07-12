def max_area_histogram(lst):
	"""
	return the max area rectangle possible in a histogram represented in list
	"""
	stack = []
	max_area = 0
	index = 0
	n = len(lst)

	# iteratet over all elements
	while index < n:
		# if next element is greatr than top element push it on stack 
		if len(stack) == 0 or lst[stack[-1]] <= lst[index]:
			stack.append( index )
			index += 1

		# else keep poping element from stack till we get an element 
		# whose hight is less than current 
		else:
			topIndex = stack.pop()
			if len(stack) == 0:
				area = lst[topIndex] * index
			else:
				# dont use the formula ( lst[topIndex] * ( index - topIndex) )
				# because it do not consider the elements in between stack[-1] and stack[-2]
				# as elements in bw these two would have been poped if they were grater than
				# height of stack[-1], below formula consider this fact
				area = lst[topIndex] * ( index - stack[-1] - 1)
			max_area = max( max_area, area )
	
	# do the same with elements left out in stack
	while len(stack) != 0:
		topIndex = stack.pop()
		if len(stack) == 0:
			area = lst[topIndex] * index
		else:
			area = lst[topIndex] * ( index - stack[-1] - 1) 
		max_area = max( max_area, area )

	return max_area

if __name__ == "__main__":
	lst = [6, 2, 5, 4, 5, 1, 6]	# ans = 12
	# lst = [2,1,2,3,1]				# ans = 5
	print( max_area_histogram(lst) )