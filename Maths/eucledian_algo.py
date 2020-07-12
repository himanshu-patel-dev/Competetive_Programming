def eucledian_algo(a, b):
	""" returns the gcd for a and b  """
	if a == 0:
		return b
	else:
		return eucledian_algo( b%a , a )

if __name__ == "__main__":
	a,b = 36,60
	print( eucledian_algo(a,b) )