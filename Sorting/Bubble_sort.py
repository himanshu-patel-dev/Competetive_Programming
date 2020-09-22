"""
Bubble sort
T = O(n^2) ..worst, T = O(n)...best
S = O(1)
"""

def Bubble_sort(lst):
	n = len(lst)
	# make n-1 passes to bubble max ele to top in each pass
	for i in range(n-1):
		swapped = False
		# run from 0 to n-1, n-2, n-3, ... 1
		# in one such pass we get the max ele in not sorted 
		# array and bubble it till the end where it need to be paced 
		for j in range(0,n-i-1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
				swapped = True
		# if no ele is swaped means array get sorted
		if not swapped:
			break

	return lst
	
if __name__ == "__main__":
	lst = [3,6,4,7,1,9,2]

	print( Bubble_sort(lst) )