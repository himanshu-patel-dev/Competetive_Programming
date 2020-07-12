def  ways_to_climb_n_steps(n):
	"""
	at a time you can climb 1 or 2 steps then in how many case can you climb n stairs.
	"""
	a,b = 1,2
	for i in range(1,n):
		a,b = b,a+b
	return a

if __name__ == "__main__":
	n = 3
	print( ways_to_climb_n_steps(n) )
