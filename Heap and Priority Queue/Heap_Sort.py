def heapify(lst,n,i):
	"""  
	T = O(logn)
	S = O(logn)
	n = size of lst
	i = index from where to start heapify down 
	(bring small ele as down as required)
	""" 

	left = 2*i + 1
	right = 2*i + 2
	largest = i		# considering the current element as largest element 

	if left < n and lst[left] > lst[largest]:
		largest = left

	if right < n and lst[right] > lst[largest]:
		largest = right

	# if root itself is largest then return else
	# recursive call to make hepify rest of the lst
	if largest == i:
		return

	# swap the value of larges with root (i)
	lst[largest], lst[i] = lst[i], lst[largest]

	heapify(lst,n,largest)

def heap_sort(lst):
	"""
	T = O(nlogn)
	S = O(logn)	for recursion
	"""
	n = len(lst)

	# in a tree leaf nodes cant be heapify down further
	# only internal node can be hapify

	# in a complete tree of n nodes there are 0 to n//2 -1 
	# internal nodes
	for i in range(n//2-1,-1,-1):
		heapify(lst,n,i)

	# after creating a not sort element of heap

	# 1. swap largest first ele to end of array
	# 2. dec size of arr by 1, n = n-1
	# 3. call heapify for first ele swapped just now
	# 4. repeat till n > 1

	for last in range(n-1,0,-1):
		# swap first and last
		lst[last], lst[0] = lst[0], lst[last]

		# hepify first element
		heapify(lst,last,0)

	return lst

if __name__ == "__main__":
	lst = [ 12, 11, 13, 5, 6, 7]
	heap_sort(lst)
	print("Sorted Array fromm heap sort :", lst )