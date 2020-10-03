def merge(first,sec):
	"""
	Given two sorted arrays merge them into one array without extra space
	T = O(m+n)
	S = O(1)
	first array is of size m+n and have m elements
	second array is of size n and have n elements
	"""
	# k = m+n
	k,n = len(first), len(sec)
	m = k-n

	# traverse from back and keep putting largest element to end of lst1
	i,j,k = m-1,n-1,k-1
	while k >= 0:
		# if lst1 have larger value than lst2 or lst2 have finished
		# then put lst1 element at current index under k iterator 
		if j < 0 or i >= 0 and first[i] > sec[j]:
			first[k] = first[i]
			i -= 1
		else:
			first[k] = sec[j]
			j -= 1
		k -= 1
	return first

if __name__ == "__main__":
	lst1 = [1,3,6,8,0,0,0,0,0]
	lst2 = [2,4,5,7,9]

	print( merge(lst1,lst2) )
