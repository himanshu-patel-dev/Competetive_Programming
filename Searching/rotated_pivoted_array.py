def rotated_pivoted_array(lst,left,right,target):
	""" 
	a sorted array is either rotated to left or right
	now look for a target element and return its index if present else return -1
	T = O(logn) S = O(1)
	"""
	if left > right:
		return -1

	mid = (left+right)//2

	if lst[mid] == target:
		return mid

	# if left array is sorted [1,2,...mid-1] is sorted
	if lst[left] <= lst[mid]:
		if lst[left] <= target and target <= lst[mid]:
			# check if target lies in left half or not
			return rotated_pivoted_array(lst,left,mid-1,target)
		else:
			# else go to right half
			return rotated_pivoted_array(lst,mid+1,right,target)
	 
	# else right is definitely sorted
	else:
		if lst[mid] <= target and target <= lst[right]:
			# check if target lies in right half or not
			return rotated_pivoted_array(lst,mid+1,right,target)
		else:
			return rotated_pivoted_array(lst,left,mid-1,target)

if __name__ == "__main__":
	lst = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
	target = 1
	n = len(lst)
	result = rotated_pivoted_array(lst,0,n-1,target)

	if result == -1:
		print("Not Found")
	else:
		print(f"Found at index {result}")


	lst = [3,1] 
	target = 1
	n = len(lst)
	result = rotated_pivoted_array(lst,0,n-1,target)

	if result == -1:
		print("Not Found")
	else:
		print(f"Found at index {result}")

	
