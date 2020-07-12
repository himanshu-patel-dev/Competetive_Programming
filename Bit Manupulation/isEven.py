def isEven(n):
	"""
	return True if even else False
	"""
	if n&1 == 0:
		return True
	else:
		return False

if __name__ == "__main__":
	n = 5
	print( isEven(n) )