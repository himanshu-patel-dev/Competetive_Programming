def Even_odd_sum(n):
	""" return sum of even and odd num in range 1 to n """
	if n&1 == 0:
		e = n//2
		o = n//2
	else:
		e = n//2
		o = n//2 + 1

	odd_sum = o*o
	even_sum = e*(e+1)

	return (odd_sum, even_sum)


if __name__ == "__main__":
	for _ in range(int(input())):
		n = int(input())
		t = Even_odd_sum(n)
		print( t[0], t[1] )