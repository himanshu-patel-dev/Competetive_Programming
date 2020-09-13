def BS_iterative(lst,target):
	low, high = 0, len(lst)-1

	while low <= high:
		mid = (low + high)//2
		if lst[mid] == target:
			return True
		elif lst[mid] < target:
			low = mid+1
		else:
			high = mid-1
	return False

def BS_recursive(lst,target,low,high):
	if low > high:
		return False

	mid = (low+high)//2

	if lst[mid] == target:
		return True
	elif lst[mid] < target:
		return BS_recursive(lst,target,mid+1,high)
	else:
		return BS_recursive(lst,target,low,mid-1)

def first_occurance(lst,target):
	""" return first occurance of an target in sorted array lst T = O(logn) """
	if not lst:
		return -1
	low, high = 0, len(lst)-1
	lastFoundIndex = -1

	while low <= high:
		mid = (low + high)//2
		if lst[mid] == target:
			lastFoundIndex = mid
			high = mid-1
		elif lst[mid] < target:
			low = mid+1
		else:
			high = mid-1
	return lastFoundIndex

def last_occurance(lst,target):
	""" return last occurance of an target in sorted array lst T = O(logn) """
	if not lst:
		return -1
	low, high = 0, len(lst)-1
	lastFoundIndex = -1

	while low <= high:
		mid = (low + high)//2
		if lst[mid] == target:
			lastFoundIndex = mid
			low = mid+1
		elif lst[mid] < target:
			low = mid+1
		else:
			high = mid-1
	return lastFoundIndex

def count_occurance(lst,target):
	""" return number of occurance of target in sorted array lst T = O(logn) """
	first = first_occurance(lst,target)
	last = last_occurance(lst,target)
	return last-first+1

if __name__ == "__main__":
	
	lst = [1,2,3,5,6]
	print( BS_iterative(lst,4) )
	print( BS_iterative(lst,6) )
	print( BS_iterative(lst,1) )
	print( BS_iterative(lst,0) )

	print()

	print( BS_recursive(lst,4,0,5) )
	print( BS_recursive(lst,6,0,5) )
	print( BS_recursive(lst,1,0,5) )
	print( BS_recursive(lst,0,0,5) )

	print()

	lst = [1,2,3,3,3,3,4,5,6,6,6,7]
	print("First Occurnace: ", first_occurance(lst,3) )
	print("First Occurnace: ", first_occurance(lst,6) )

	print("Last Occurance: ", last_occurance(lst,3) )
	print("Last Occurance: ", last_occurance(lst,6) )

	print("Count: ", count_occurance(lst,3) )
	print("Count: ", count_occurance(lst,6) )


