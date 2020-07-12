def d_digit_no_with_zero(digits):
	"""
	return no of d digits which have at least one zero in them
	"""
	digits -= 1
	return 9*( 10**digits - 9**digits)

if __name__ == "__main__":
	digits = 2
	print( d_digit_no_with_zero(digits) )	
	
	digits = 3
	print( d_digit_no_with_zero(digits) )	