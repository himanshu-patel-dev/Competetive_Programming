def power(n,k):
	if k == 0 or n == 1:
		return 1

	if k == 1:
		return n

	# so that -1//2 -> -1 but we want -1/2 = 0
	x = power(n, int(k/2) )

	# if k is even return x^2
	if k%2 == 0:
		return x*x

	# else return x^2 * n
	if k > 0:
		return x*x*n
	return x*x/n

if __name__ == "__main__":
	n,p = 2, 5
	print( power(n,p) )

	n,p = 2, -2
	print( power(n,p) )
	
	n,p = 2, -4
	print( power(n,p) )
