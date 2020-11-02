def median(lst):
	""" given list must be sorted """
	n = len(lst)
	if n%2 != 0:
		return lst[n//2]
	else:
		return (lst[n//2]+lst[n//2-1])/2

def merge_median(lst1,lst2):
	# print(lst1,lst2)
	n = len(lst1)

	if n == 0:
		return None

	if n == 1:
		return (lst1[0]+lst2[0])/2

	if n == 2:
		return ( max( lst1[0],lst2[0] ) + min( lst1[1], lst2[1] ) )/2

	m1 = median(lst1)
	m2 = median(lst2)

	if m1 == m2:
		return m1
	elif m1 > m2:
		if n%2 == 0:
			return merge_median( lst1[:n//2+1], lst2[n//2-1:] )
		else:
			return merge_median( lst1[:n//2+1], lst2[n//2:] )
	else:
		if n%2 == 0:
			return merge_median( lst1[n//2-1:], lst2[:n//2+1] )
		else:
			return merge_median( lst1[n//2:], lst2[:n//2+1] )


if __name__ == "__main__":
	lst1 = [1,12,15,26,38]
	lst2 = [2,13,17,30,45]
	print( merge_median(lst1,lst2) )

	lst1 = [1, 2, 3, 6]
	lst2 = [4, 6, 8, 10]
	print( merge_median(lst1,lst2) )