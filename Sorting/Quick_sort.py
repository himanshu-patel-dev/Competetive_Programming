"""
Quick sort
T = O(n^2) Worst  
T = O(nlogn) Best  
S = O(1) Auxilary space
"""

def partition(lst,low,high):
	i = low-1

	# choosing last element as pivot
	pivot = lst[high]

	for j in range(low,high):

		# if a element less than pivot then send it to 
		# beginning or to left side of pivot
		if lst[j] < pivot:
			i += 1
			lst[i], lst[j] = lst[j], lst[i]

	# now put the pivot in its place, and ele at 
	# that place to pivot place
	lst[i+1], lst[high] = lst[high], lst[i+1]

	return i+1

def Quick_Sort_Sub(lst,low,high):
	if low >= high:
		return

	# get the partition's pivot point
	# element at pivot is already sorted and 
	# thus only its left and right side 
	# need to be sorted 
	pivot = partition(lst,low,high)

	# sort the left and right side using the same algo
	Quick_Sort_Sub(lst,low,pivot-1)
	Quick_Sort_Sub(lst,pivot+1,high)


def Quick_sort(lst):
	Quick_Sort_Sub(lst,0,len(lst)-1)
	return lst

if __name__ == "__main__":
	lst = [3,6,4,7,1,9,2]
	print( Quick_sort(lst) )

	lst = [10,80,30,90,40,50,70]
	print( Quick_sort(lst) )
