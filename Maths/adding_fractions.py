import math
def adding_fractions(num1, den1, num2, den2):
	"""
	adding two fractions and return a tuple (num , den)
	"""
	lcm = den1 * den2 // math.gcd(den1 , den2)
	num1 = num1 * ( lcm// den1 )
	num2 = num2 * ( lcm//den2 )
	# final result not in proper form
	num = num1 + num2
	den = lcm
	# print( (num,den) )
	common = math.gcd(num, den)
	num = num//common
	den = den//common

	return (num, den)

if __name__ == "__main__":
	num1 = 1; den1 = 6; num2 = 1; den2 = 2
	print( adding_fractions( num1, den1, num2, den2 ) ) 