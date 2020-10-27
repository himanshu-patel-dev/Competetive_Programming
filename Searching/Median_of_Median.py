"""
To get kth smallest/largest element in unsorted array 
T = O(n) 
S = O(1)

It is better than quick select as it given lineat time sol in every case
"""

def range_median(lst,start,n):
	""" 
	returns the median between two index of array 
	start = start index 
	n = len of sub array
	"""
	
	temp = sorted([lst[i] for i in range(start,start+n)])
	# return the middle ele in odd len
	# return the right middle in even len
	return temp[ n//2 ]

def partition(lst,start,end,med_median):
	# place the med_median ele at end of array and make it as pivot
	for i in range(start,end+1):
		if lst[i] == med_median:
			lst[end], lst[i] = lst[i], lst[end]
			break
	
	# last ele is med of med and we take it as pivot
	x = lst[end]
	curr = start
	for i in range(start,end):
		if lst[i] <= x:
			lst[curr], lst[i] = lst[i], lst[curr]
			curr += 1
	# place the pivot ele in its place and return its index
	lst[curr], lst[end] = lst[end], lst[curr]
	print(lst)
	return curr


def kth_smallest_sub(lst,start,end,k):
	if k < 1 or k > end-start+1:
		return None
	
	# len of array
	n = end-start+1

	# Divide arr[] in groups of size 5,calculate median of every group 
	# and store it in median[] array.
	median = []  

	# let there are k partition of full array
	m = n//5 
	for i in range(m):
		median.append( range_median(lst, start+i*5, 5) )
	
	# for the last elemetns not in the array
	if n%5 != 0:
		median.append( range_median(lst, start+m*5, n%5) )

	# Find median of all medians using recursive call.  
    # If median[] has only one element, then no need of recursive call 
	if len(median) == 1:
		med_median = median[0]
	else:
		med_median = kth_smallest_sub(median, 0, len(median)-1, len(median)//2)

	# Partition the array around a medOfMed element and get position of pivot   
	pivot = partition(lst,start,end,med_median)

	# if pivot the kth ele
	if pivot-start+1 == k:
		return lst[pivot]
	# if kth ele is in left partition
	elif pivot-start+1 > k:
		return kth_smallest_sub(lst, start, pivot-1, k)
	# if kth ele is in right partition then discard ele in left
	else:
		left_ele = pivot-start+1
		return kth_smallest_sub(lst, pivot+1, end, k-left_ele)

def kth_smallest(lst,k):
	return kth_smallest_sub(lst,0,len(lst)-1,k)

if __name__ == "__main__":
	# [2,4,5,6,8,10,11,26]

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 3
	print( kth_smallest(lst,k) )	# 5

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 7
	print( kth_smallest(lst,k) )	# 11

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 5
	print( kth_smallest(lst,k) )	# 8

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 0
	print( kth_smallest(lst,k) )	# None

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 9
	print( kth_smallest(lst,k) )	# None

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 8
	print( kth_smallest(lst,k) )	# 26


lst = [1,5,3,2,4,9,8,7,6,10,12,11,13,14,15,18,16,19,20,17,23,21,22,25,24,29,30,26,28,27]