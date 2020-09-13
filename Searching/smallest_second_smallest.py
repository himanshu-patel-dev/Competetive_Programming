def second_smallest(lst):
	""" 
	return the smallest and second smallest element 
	T = O(n) single pass
	if there are multiple minmum ele algo avoid them and return different 
	second min element
	"""
	first = second = float('inf')
	for ele in lst:
		if ele < first:
			second, first = first, ele
		elif ele < second and ele > first:
			second = ele
	print( (first,second) )

if __name__ == "__main__":
	lst = [2,4,1,2,6,7,3,2,1]
	second_smallest(lst)

	lst = [2,4,1,6,7,3]
	second_smallest(lst)
