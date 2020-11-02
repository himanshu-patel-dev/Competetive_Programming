def median(A, B):
	m, n = len(A), len(B)
	if m > n:
		A, B, m, n = B, A, n, m
	if n == 0:
		raise ValueError

	imin, imax, half_len = 0, m, (m + n + 1) // 2
	while imin <= imax:
		i = (imin + imax) // 2
		j = half_len - i
		
		if i < m and B[j-1] > A[i]:
			# i is too small, must increase it
			imin = i + 1
		elif i > 0 and A[i-1] > B[j]:
			# i is too big, must decrease it
			imax = i - 1
		else:
			# i is perfect

			if i == 0: max_of_left = B[j-1]
			elif j == 0: max_of_left = A[i-1]
			else: max_of_left = max(A[i-1], B[j-1])

			if (m + n) % 2 == 1:
				return max_of_left

			if i == m: min_of_right = B[j]
			elif j == n: min_of_right = A[i]
			else: min_of_right = min(A[i], B[j])

			return (max_of_left + min_of_right) / 2.0


if __name__ == "__main__":
	lst1 = [1,12,15,26,38]
	lst2 = [2,13,17,30,45]
	print( median(lst1,lst2) )

	lst1 = [1, 2, 3, 6]
	lst2 = [4, 6, 8, 10]
	print( median(lst1,lst2) )

	lst1 = [1,12,15,26,38]
	lst2 = [2,13,17,30,45,50]
	print( median(lst1,lst2) )

	lst1 = [1,3]
	lst2 = [2]
	print( median(lst1,lst2) )

	lst1 = [1,2]
	lst2 = [3,4]
	print( median(lst1,lst2) )

	lst1 = [0,0]
	lst2 = [0,0]
	print( median(lst1,lst2) )

	lst1 = []
	lst2 = [1]
	print( median(lst1,lst2) )