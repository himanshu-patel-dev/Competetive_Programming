def max_repetetion_element(lst):
	""" 
	works only if:
	1. All elements are in range 0 to n-1
	2. All elements need to be pos (0 to n-1) as -ve element have 
	different modulo
	"""
	n = len(lst)

	# for each element at lst[i] go to index lst[i] 
	# and increase value by n
	for i in range(n):
		lst[ lst[i]%n ] += n
	print(lst)

	mx = -1
	ele = None
	for i in range(n):
		if lst[i]//n > mx:
			mx = lst[i]//n
			ele = i

	print(f'{ele} repeated {mx} times')

lst = [1,2,3,4,5,2,3,2,4,5,2]
max_repetetion_element(lst)
