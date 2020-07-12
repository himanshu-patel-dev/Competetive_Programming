import math

def Perfect_square(n):
	sq = int(math.sqrt(n))
	if sq * sq == n:
		return True
	else:
		return False
