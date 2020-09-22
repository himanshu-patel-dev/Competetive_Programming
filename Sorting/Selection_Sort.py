"""
Selection sort
T = O(n^2) .. worst , T = (n^2)...best
S = O(1)
"""

def Selection_sort(lst):
	n = len(lst)
	# make n-1 passes to select n-1 min element
	for i in range(n-1):
		# select min element in array each time
		min_index = i
		for j in range(i+1,n):
			if lst[j] < lst[min_index]:
				min_index = j
		# swap current element with the min element 
		# in array right side to that element
		lst[min_index], lst[i] =  lst[i], lst[min_index]

	return lst
	
if __name__ == "__main__":

	lst = [3,6,4,7,1,9,2]

	print( Selection_sort(lst) )