def toggle_in_range(n,r,l):
	"""
	it toggles the bits in bin rep of n from rightmost r bit to rightmost l bit 
	(both inclusive)
	"""
	r = (1<<r)-1
	l = (1<<(l-1))-1
	xor = r ^ l
	return n ^ xor

if __name__ == "__main__":
	n = 15
	l = 2
	r = 3
	# 15 = 1111 to 1001 = 9
	print( toggle_in_range(n,r,l) )