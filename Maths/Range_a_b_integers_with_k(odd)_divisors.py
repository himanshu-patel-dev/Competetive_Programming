import math

def factors_of_n(n):
	""" 
	return count of factors of n 
	time comp = O(sqrt(n)) 
	"""
	count = 2
	for i in range(2, int(math.sqrt(n)) + 1 ):
		if n%i == 0:
			count += 1
			if i != n//i:
				count += 1
	return count

def perfect_sq_in_range(a,b):
	"""
	return two numbers whose square lies in range a and b inclusive
	time comp = O(1)
	"""
	a_sqrt = math.ceil( math.sqrt(a) )
	b_sqrt = math.floor( math.sqrt(b) )
	return (a_sqrt,  b_sqrt)

def solve(a,b,k):
	a_sq, b_sq = perfect_sq_in_range(a,b)
	count_perfect_sq_k_factors = 0
	for i in range(a_sq, b_sq+1):
		factors = factors_of_n(i*i)
		if factors == k:
			count_perfect_sq_k_factors += 1
	return count_perfect_sq_k_factors

if __name__ == "__main__":
	""" 
	return no of integers in range a to b such that they have k (odd) no of factors
	"""
	# a,b,k = 2,49,3 
	# Between 2 and 49 there are four numbers with three divisors 4 (Divisors 1, 2, 4), 
	# 9 (Divisors 1, 3, 9), 25 (Divisors 1, 5, 25} and 49 (1, 7 and 49)
	
	# between 1 and 100 there are 36 (1, 2, 3, 4, 6, 9, 12, 18, 36)
	# and 100 (1, 2, 4, 5, 10, 20, 25, 50, 100) having exactly 9 divisors
	a,b,k = 1,100,9
	print( solve(a,b,k) )
