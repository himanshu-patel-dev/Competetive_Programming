def  Max_Contiguous_Sum(lst):
	"""
	kadane algorithm : return max sum of contiguous segment with indexes
	return : (max_sum, index_start, index_end) zero based index
	"""
	n = len(lst)
	sumSofar = sumEndingHere = 0
	a,b = 0,0	# index of that contiguous segment
	s = 0		# index  that stores the position where new positive seg starts
				# in case this new positive seg is greater than prev than a = s

	for i in range(n):
		sumEndingHere = sumEndingHere + lst[i]
		if sumEndingHere < 0:
			sumEndingHere = 0
			s = i+1
			continue
		if sumSofar < sumEndingHere:
			sumSofar = sumEndingHere
			a = s
			b = i

	if sumSofar == 0:
		m = max(lst)
		a = b = lst.index(m)
		return (m,a,b)
	else:
		return (sumSofar,a,b)

if __name__ == "__main__":
	# lst = [-2, 3, -16, 100, -4, 5]
	lst = [-5,6,4,-50,-3,100,2,4]
	# lst = [-5,-50,-3,-100,-2,-4] 	# for all negative
	print( Max_Contiguous_Sum(lst) )