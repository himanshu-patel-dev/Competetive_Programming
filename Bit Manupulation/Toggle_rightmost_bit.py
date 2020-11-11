def toggle_rightmost(n):
	''' returns the n after toggling its rightmost bit '''
	return n & (n-1)

if __name__ == "__main__":
	n = 15
	print( toggle_rightmost(n) )

	n = 11
	print( toggle_rightmost(n) )
	
	n = 3
	print( toggle_rightmost(n) )
	