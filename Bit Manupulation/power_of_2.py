def power2(n):
	return n & (n-1) == 0

if __name__ == "__main__":
	n = 4
	print( power2(n) )

	n = 8
	print( power2(n) )

	n = 5
	print( power2(n) )
