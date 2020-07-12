import math
def ones_complement(n):
	"""	return number of bits, no of bits which are one and which are zero """
	bits = math.floor( math.log(n,2) ) + 1
	xor = (1<<bits)-1
	return xor ^ n

def twos_complement(n):
	return ones_complement(n) + 1

if __name__ == "__main__":
	n = 11	# 1011 
	# ones 0100 = 4
	# two 0101 = 5
	print( 'Ones: ',ones_complement(n) )
	print('Twos: ',twos_complement(n))