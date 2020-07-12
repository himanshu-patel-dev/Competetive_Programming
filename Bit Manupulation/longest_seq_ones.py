def longest_seq_ones(n):
	"""
	return the longest sequence of ones
	"""
	c = 0
	while n:
		n = n & (n>>1)
		c += 1
	return c

if __name__ == "__main__":
	n = 47	# 47 = 101111 ans = 4
	print( longest_seq_ones(n) )