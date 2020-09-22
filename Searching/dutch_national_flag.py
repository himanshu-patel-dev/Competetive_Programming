"""
problem: dutch_national_flag

given a array of only 1 and 2 and 0 sort the array in single pass.
"""

def dutch_flag(lst):
	n = len(lst)
	low = mid = 0
	high = n-1

	while mid <= high:
		if lst[mid] == 0:
			lst[mid], lst[low] = lst[low], lst[mid]
			low += 1
			mid += 1
		elif lst[mid] == 1:
			mid += 1
		else:
			lst[mid], lst[high] = lst[high], lst[mid]
			high -= 1
	return lst

if __name__ == "__main__":
	lst = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
	print( dutch_flag(lst) )
