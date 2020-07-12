import math
def sum_of_factorial_of_digits(n):
	s = 0
	while n:
		s += math.factorial( n%10 )
		n = n//10
	return s

if __name__ == "__main__":
	n = 132	# 1 + 6 + 2 = 9
	print( sum_of_factorial_of_digits(n) )