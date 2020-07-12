import math
def binary_bits_in_num(n):
	"""
	return number of bits in number
	"""
	return math.floor( math.log(n,2) ) + 1

if __name__ == "__main__":
	n = 5
	print( binary_bits_in_num(n) )