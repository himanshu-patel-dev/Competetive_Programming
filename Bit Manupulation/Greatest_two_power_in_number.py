import math
def Greatest_two_power_in_number(n):
	"""
	return Greatest of two power in number
	"""
	return 2**math.floor( math.log(n,2) )

if __name__ == "__main__":
	n = 9
	print( Greatest_two_power_in_number(n) )