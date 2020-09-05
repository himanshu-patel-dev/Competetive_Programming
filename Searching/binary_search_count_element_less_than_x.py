from bisect import bisect_left, bisect_right

def count_less_than_equal(lst,ele):
	""" 
	provide a sorted list and get the no 
	of element less than equal to ele 
	"""
	return bisect_right(lst,ele)


def count_greater_than_equal(lst,ele):
	""" 
	provide a sorted list and get the no 
	of element greater than equal to ele 
	"""
	return len(lst) - bisect_left(lst,ele)
	
if __name__ == "__main__":
	n = 7
	ele = 10
	lst = [1,2,8,10,10,11,12,19,20]

	# give a sorted list as input
	lst.sort()
	print(lst)
	print( count_less_than_equal(lst,ele) )
	print( count_greater_than_equal(lst,ele) )