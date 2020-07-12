def  fibo(n):
	"""
	time comp = O(n) and space comp = O(1)
	"""
	# f(0) = 0 and f(1) = 1
	a,b = 0,1
	for i in range(1,n):
		a,b = b,a+b
	return a	

if __name__ == "__main__":
	print( fibo(5) )