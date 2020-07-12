import math
def i_bit_from_left(n,i):
	"""
	return the i_bit_from_left
	"""
	bits = math.floor( math.log(n,2) ) + 1
	n = n>>(bits-i)

	if n & 1 == 0:
		return 0
	else:
		return 1

if __name__ == "__main__":
	n = 47	# 47 = 101111 
	i = 2	# ans = 0
	print( i_bit_from_left(n,i) )