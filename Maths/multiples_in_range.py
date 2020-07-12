def multiples_in_range(a,b,n):
	if a%n == 0:
		return b//n - a//n + 1
	else:
		return b//n - a//n

if __name__ == "__main__":
	a,b,m = 7,42,5
	print( multiples_in_range(a,b,m) )