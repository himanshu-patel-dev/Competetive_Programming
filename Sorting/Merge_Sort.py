"""
Merge sort
T = O(nlogn) Worst  
T = O(nlogn) Best  
S = O(n)	auxilary space
"""

def Merge_sort(lst):
	n = len(lst)

	if n <= 1:
		return lst

	mid = n//2
	# sort the left half
	left = Merge_sort(lst[:mid])
	# sort the right half
	right = Merge_sort(lst[mid:])

	# merge both
	i = j = k = 0
	a,b = len(left), len(right)
	while i < a and j < b:
		if left[i] < right[j]:
			lst[k] = left[i]
			i += 1
		else:
			lst[k] = right[j]
			j += 1
		k += 1

	# merge remaining left array to list
	while i < a:
		lst[k] = left[i]
		i += 1
		k += 1

	# merge remaining right array to list
	while j < b:
		lst[k] = right[j]
		j += 1
		k += 1

	return lst

if __name__ == "__main__":
	lst = [3,6,4,7,1,9,2]
	print( Merge_sort(lst) )
