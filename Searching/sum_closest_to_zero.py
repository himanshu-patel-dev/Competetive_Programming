def sum_close_to_zero(lst):
	""" 
	given a list output the sum closest to 0 which can be achived as 
	sum of two elements 
	"""
	n = len(lst)
	lst.sort()

	l,h = 0,n-1
	result = float('inf')

	while  l<h:
		curr_sum = lst[l]+lst[h]
		result = min(result, abs(curr_sum))

		if curr_sum > 0:
			h -= 1
		else:
			l += 1
	print(result)

if __name__ == "__main__":
	lst = [1, 60, -10, 70, -80, 85]
	sum_close_to_zero(lst)