import math
import bisect
def sieve_of_erathosthenes(n):
	# consider all numbers to be prime, later set false to those who aren't
	sieve = [True]*(n+1) 	# for 1 indexed 
	sieve[0] = False
	sieve[1] = False

	for i in range(2, int(math.sqrt(n)) + 1 ):
		
		if sieve[i]:
			for j in range(i*i,n+1,i):
				sieve[j] = False
	return sieve

if __name__ == "__main__":
	sieve_dimension = 10000
	# dimensions = n+1 (1 indexed)
	sieve = sieve_of_erathosthenes( sieve_dimension )
	primes = []
	for i in range(sieve_dimension+1):
		if sieve[i]:
			primes.append( i )
	# print(primes)
	# print(len(primes))

	# range under 1 to n in which we want all primes
	n = 501
	print( primes[: bisect.bisect(primes,n) ] )
