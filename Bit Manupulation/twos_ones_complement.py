import math
def ones_complement(n):
	"""	return number of bits, no of bits which are one and which are zero """
	bits = math.floor( math.log(n,2) ) + 1
	xor = (1<<bits)-1
	return xor ^ n

def twos_complement(n):
	return ones_complement(n) + 1

def Ones_Complement(N):
	" Ones comp string method "
	binary = bin(N)[2:]
	flip = {'1':'0', '0':'1'}
	one_comp = ''.join([ flip[bit] for bit in binary])
	return int(one_comp,2)

if __name__ == "__main__":
	n = 11	# 1011 
	# ones 0100 = 4
	# two 0101 = 5
	print( 'Ones: ',ones_complement(n) )
	print('Twos: ',twos_complement(n))
	print( 'Ones Comp', Ones_Complement(5) )