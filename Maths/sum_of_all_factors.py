import math
def sum_of_all_factors(n):
	"""
	return the sum of factors of n
	or get all prime factors of n with their power with slight modification
	"""
	
	result = 1
	for i in range(2, int(math.sqrt(n))+1 ):
		prime_sum = 1
		prime_power = 1
		while n%i == 0:
			prime_sum += i**(prime_power)
			n = n//i
			prime_power += 1
		result = result * prime_sum
	
	# at this if a number is more than 1 than it is prime
	if n > 1:
		result = result * (1 + n)

	return result

if __name__ == "__main__":
	n = 15	# [1, 30, 2, 15, 3, 10, 5, 6] -> sum = 72
	print( sum_of_all_factors(n) )