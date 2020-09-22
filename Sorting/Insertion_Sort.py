"""
Insertion sort
T = O(n^2) Worst  T = O(n) Best  S = O(1)
"""

def Insertion_sort(lst):
	n = len(lst)
	for i in range(1,n):
		# save the current element to temp as it might be overwritten by
		# left side element on right sigfting, which happend before we 
		# place current element into correct position
		temp = lst[i]
		pos = i
		# continue to right shift element till we get to position where 
		# current temp value can be plced, note the array to left of 'pos'
		# is already sorted 
		while pos > 0  and lst[pos-1] > temp:
			lst[pos] = lst[pos-1]
			pos -= 1

		lst[pos] = temp

	return lst

if __name__ == "__main__":
	lst = [3,6,4,7,1,9,2]
	print( Insertion_sort(lst) )
