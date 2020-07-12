import math
def rightmost_diff_bit(a,b):
	"""
	return number (from right) of the rightmost different bit in bin rep of a and b
	"""
	xor = a ^ b
	c = 1
	while xor & 1 == 0:
		c += 1
		xor = xor >> 1
	return c

if __name__ == "__main__":
	a = 7	# 0111
	b = 11	# 1011
	print( rightmost_diff_bit(a,b) )