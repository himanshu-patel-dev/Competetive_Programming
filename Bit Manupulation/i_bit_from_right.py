def i_bit_from_right(n,i):
	"""
	return the i_bit_from_right
	"""
	if (1<<(i-1)) & n == 0:
		return 0
	else:
		return 1

if __name__ == "__main__":
	n = 47	# 47 = 101111 
	i = 5	# ans = 0
	print( i_bit_from_right(n,i) )