def toggle(n,k):
	''' returns the n after toggling its kth bit from right '''
	return n & ~(1<<(k-1))

if __name__ == "__main__":
	n = 15
	k = 1
	print( toggle(n,k) )

	n = 15
	k = 2
	print( toggle(n,k) )
	
	n = 15
	k = 3
	print( toggle(n,k) )
	