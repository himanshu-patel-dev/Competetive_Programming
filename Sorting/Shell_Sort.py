"""
Shell sort
T = O() Worst  T = O() Best  S = O()
"""

def Shell_sort(lst):
	n = len(lst)
	gap = n//2

	# loop till gap is not zero
	while gap:
		# starting from gap make a linear traversal to right then
		# insertion wort each element with gap in consideration 
		for i in range(gap,n):
			# save the value
			temp = lst[i]
			pos = i

			# insertion sort with gap
			while pos >= gap and lst[pos-gap] > temp:
				lst[pos] = lst[pos-gap]
				pos -= gap
			# put current element in correct position
			lst[pos] = temp
		
		# reduce the gap to half
		gap = gap//2

	return lst

if __name__ == "__main__":
	lst = [3,6,4,7,1,9,2]
	print( Shell_sort(lst) )
