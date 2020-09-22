"""
Given an array, find thc maximum j - i such that A[il > A[j]. 
Input: [34, 8, 10, 3, 2, 80, 30, 33, 1]
Output: 6 (j = 7, i = 1).

T = O(n)
"""

def max_index_difference(lst):
	n = len(lst)
	min_value = [0]*n
	max_value = [0]*n

	min_value[0] = lst[0]
	max_value[-1] = lst[-1]

	# min value at index i starting from 0
	for i in range(1,n):
		min_value[i] = min(min_value[i-1],lst[i])

	# max value at index j starting from n-1
	for j in range(n-2,-1,-1):
		max_value[j] = max(max_value[j+1], lst[j])

	i = j = 0
	max_diff = -1

	while i < n and j < n:
		if min_value[i] < max_value[j]:
			max_diff = max(max_diff,j-i)
			j += 1
		else:
			i += 1
	return max_diff

if __name__ == "__main__":
	lst = [34, 8, 10, 3, 2, 80, 30, 33, 1]
	print( max_index_difference(lst) )
