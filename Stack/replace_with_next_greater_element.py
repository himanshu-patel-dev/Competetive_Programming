def repalce_with_next_greater(lst):
	""" 
	replace every element with nearest greater element to its right 
	"""
	# this holds for current element how many element 
	# to its left are there which are larger than current
	stack = [] 
	n = len(lst)
	for i in range(n):
		# make current element as target this will replace all 
		# its left elements smaller than it (and surely also closer to it 
		# than other larger right elements)
		NextGreater = lst[i]
	
		while stack and lst[ stack[-1] ] < NextGreater:
			lst[ stack.pop() ] = NextGreater
		
		# if stack is empty means all its left element already 
		# got satisfatiable	right nearest larger element
		# just push current ele and continue

		stack.append(i) 

	# update the rightmost elements with infinity 
	# as there are no more right greater elements
	# to the elements left in stack
	""" comment out this code if you want  """
	NextGreater = float('inf')				
	while stack:
		lst[ stack.pop() ] = NextGreater

	return lst

if __name__ == "__main__":
	# lst = [6,12,4,1,111,2,2,10]
	# print( repalce_with_next_greater(lst) )

	lst = [6,12,4,1,111,2,2,1]
	print( repalce_with_next_greater(lst) )
