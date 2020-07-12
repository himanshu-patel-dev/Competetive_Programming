def binary_to_grey(n):
	"""
	take decimal num not binary string for gray code representation
	return binary rep of grey code
	time comp = O(n)
	"""
	binary = 0
	while n:
		binary = binary ^ n
		n = n>>1
	return binary

if __name__ == "__main__":
	n = 13 # ans = 9
	print( binary_to_grey(n) )