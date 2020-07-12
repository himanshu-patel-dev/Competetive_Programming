import math
def total_bits_set_unset_bits(n):
	"""	return number of bits, no of bits which are one and which are zero """
	bits = math.floor( math.log(n,2) ) + 1
	ones = 0
	while n:
		ones += 1
		n = n & (n-1)
	zeros = bits - ones
	return (bits, ones, zeros)

if __name__ == "__main__":
	n = 11	# 1011
	print( set_unset_bits(n) )