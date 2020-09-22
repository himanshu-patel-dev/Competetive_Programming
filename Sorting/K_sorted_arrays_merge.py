def merge_two_sorted_array(lst1,lst2):
	i,j,k,n1,n2 = 0,0,0,len(lst1), len(lst2)
	temp = [0]*(n1+n2)
	while i<n1 and j<n2:
		if lst1 < lst2:
			temp[k] = lst1[i]
			i += 1
			k += 1
		else:
			temp[k] = lst2[j]
			k += 1
			j += 1

	while i<n1:
		temp[k] = lst1[i]
		i += 1
		k += 1

	while j<n2:
		temp[k] = lst2[j]
		j += 1
		k += 1
			
	return temp


def sorted_arrays_merge_sub(lst,low,high):
	# only one array and its sorted return that array
	if low == high:
		return lst[low]

	# only two arrays to merge
	# merge them together and return the result 
	if abs(high-low) == 1:
		return merge_two_sorted_array(lst[low],lst[high])
	
	# more than two arrays make a recursive call to get two sorted arrays
	mid = (low+high)//2
	left = sorted_arrays_merge_sub(lst,low,mid)
	right = sorted_arrays_merge_sub(lst,mid+1,high)
	return merge_two_sorted_array(left,right)


def sorted_arrays_merge(lst):
	"""
	All arrays are of equal length
	T = O(n*k*log(k))
	S = O(n*k)
	n -> no of elements in each array 	k -> no of arrays to merge
	"""

	low, high = 0, len(lst)-1
	return sorted_arrays_merge_sub(lst,low,high)


if __name__ == "__main__":
	lst = [
		[1,2,3,4,5],
		[7,8,9,10,11],
		[12,13,14,15,16,17],
		[100,101,102,103,104],
		[50,51,52,53,54]
	]

	print( sorted_arrays_merge(lst) )