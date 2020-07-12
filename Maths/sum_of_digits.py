def sum_of_digits(n):
	s = 0
	while n:
		s += n%10
		n = n//10
	return s

if __name__ == "__main__":
	n = 1324
	print( sum_of_digits(n) )