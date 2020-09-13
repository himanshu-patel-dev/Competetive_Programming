def interpolationSearch(lst,target):
	""" search on sorted array T = O(log(log(n))) """
	n = len(lst)
	low, high = 0,n-1

	while low <= high and lst[low] <= target and target <= lst[high]:
		# to prevent zero divison error
		if low == high:
			if lst[low] == target:
				return low
			return -1

		pos = low + ((high-low)*(target-lst[low]))//(lst[high] - lst[low])
		print('Checking at index: ',pos)

		if lst[pos] == target:
			return pos
		elif lst[pos] < target:
			low = pos + 1
		else:
			high = pos - 1

	return -1

if __name__ == "__main__":
	# sorted array
	lst = [10,12,13,16,18,19,20,21,22,23,24,33,35,42,47 ]
	target = 13
	index = interpolationSearch(lst,target) 
	if index == -1:
		print("ele not found")
	else:
		print("ele found at index: ",index)


	print('')

	lst = [1,3,4,7,13,14,17,18,19,27,34,39,43,48]
	target = 15
	index = interpolationSearch(lst,target) 
	if index == -1:
		print("ele not found")
	else:
		print("ele found at index: ",index)