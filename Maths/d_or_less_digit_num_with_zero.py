def d_or_less_digit_num_with_zero(digits):
	"""
	return num of d or less digits which have at least one zero in them
	"""
	gp1 = 9*( 10**digits - 1)//9 
	gp2 = 9*( 9**digits - 1 )//8
	return gp1 - gp2

if __name__ == "__main__":
	digits = 2
	print( d_or_less_digit_num_with_zero(digits) )	
	
	digits = 3
	print( d_or_less_digit_num_with_zero(digits) )	