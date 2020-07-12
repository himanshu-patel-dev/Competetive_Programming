def grey_code(n):
	"""
	return the grey code for n
	"""
	return n ^ (n>>1)

if __name__ == "__main__":
	n = 5 # 5 = 101
	# ans = 111 = 7
	print( grey_code(n) )