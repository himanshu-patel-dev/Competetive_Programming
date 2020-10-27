"""
To get kth smallest/largest element in unsorted array 
Quickselect uses pivot subroutine of quick sort 
T = O(n*n) 
S = O(1)

T = avg = O(n)
T = best = O(1)
"""

def pivot(lst,start,end):
	# pick the last ele
	ele = lst[end]

	i = start	# point to first ele of list
	# iterate over all ele except the last
	for j in range(start,end):
		if lst[j] <= ele:
			lst[i], lst[j] = lst[j], lst[i]
			i += 1
	
	lst[i], lst[end] = lst[end], lst[i]
	# return the pivot index where the pivot ele is placed
	return i

def quickselect_sub(lst,start,end,k):
	# print(lst,start,end,k)
	# if k is less than 1 or more than total len of array then return none
	if k < 1 or k > end-start+1:
		return None

	pivot_index = pivot(lst,start,end)
	# current pivot ele is the kth ele
	if pivot_index-start+1 == k:
		return lst[pivot_index]
	# ele in first half are more than required ( > k )
	# cut lose the sec half and still looking for k ele
	elif pivot_index-start+1 > k:
		return quickselect_sub(lst,start,pivot_index-1,k)
	# else cut lose the first half and look for less than k ele
	else:
		ele_discard = pivot_index-start+1
		return quickselect_sub(lst,pivot_index+1,end,k-ele_discard ) 


def quickselect(lst,k):
	return quickselect_sub(lst,0,len(lst)-1,k)

if __name__ == "__main__":
	# [2,4,5,6,8,10,11,26]

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 3
	print( quickselect(lst,k) )

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 7
	print( quickselect(lst,k) )

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 5
	print( quickselect(lst,k) )

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 0
	print( quickselect(lst,k) )

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 9
	print( quickselect(lst,k) )

	lst = [10, 4, 5, 8, 6, 11, 26, 2]
	k = 8
	print( quickselect(lst,k) )