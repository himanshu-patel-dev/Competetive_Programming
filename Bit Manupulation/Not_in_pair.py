def Not_in_pair(lst):
	"""
	all numbers in lst are in pair except one identify which one
	"""
	alone = 0
	for i in lst:
		alone = alone ^ i
	return alone

if __name__ == "__main__":
	lst = [1,1,2,2,3,3,4]
	print( Not_in_pair(lst) )