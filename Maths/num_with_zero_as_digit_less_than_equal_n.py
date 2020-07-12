def d_or_less_digit_num_with_zero(digits):
	"""
	return num of d or less digits which have at least one zero in them
	"""
	gp1 = 9*( 10**digits - 1)//9 
	gp2 = 9*( 9**digits - 1 )//8
	return gp1 - gp2

def num_with_zero_as_digit_less_than_equal_n(n):
	"""
	return numbers in range 1 to n having zero as a digit
	"""
	n = str(n)
	k = len(n)	# length of number
	total = d_or_less_digit_num_with_zero(k-1)

	remain_num = int(n[1:])+1

	# set to 1 because we consider actual no n to do not any zero digit
	# if wrong then we sub 1 form 'non_zero_in_remaining'
	non_zero_in_remaining = 1	
	for i in range(k):
		if n[i] == '0':
			non_zero_in_remaining -= 1
			break
		else:
			non_zero_in_remaining += ( ord(n[i]) - ord('0') - 1)* ( 9**( k-i-1 ) )
	zeros_num = remain_num - non_zero_in_remaining
	return total + zeros_num

if __name__ == "__main__":
	n = 123
	# n = 107
	# n = 1264
	print( num_with_zero_as_digit_less_than_equal_n(n) )
