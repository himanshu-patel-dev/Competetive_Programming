import math
def all_prime_factors_with_powers(n):
	"""
	get all prime factors of n with their power in lst, 
	it is good for one time use for multiple queries go for sieve of erathos
	format : ( prime factor, their power )
	time comp = O( sqrt(n) )
	"""
	lst = []
	for i in range(2, int(math.sqrt(n))+1 ):
		prime_power = 1
		if n%i == 0:
			while n%i == 0:
				n = n//i
				prime_power += 1
			lst.append( (i,prime_power) )
	
	# at this if a number is more than 1 than it is prime
	if n > 1:
		lst.append( (n, 1) )
	return lst

if __name__ == "__main__":
	n = 15	# 15 = 3^1 * 5^1
	print( all_prime_factors_with_powers(n) )