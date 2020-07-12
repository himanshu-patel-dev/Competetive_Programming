def Replace_digit_in_number(n, toReplace, byReplace):
	""" select any digit to be replace in a number by any other digit """
	result = n
	decimalPlace = 1
	if n == 0:
		return byReplace
	add = 0

	while n > 0:
		if n%10 == toReplace:
			add += byReplace*decimalPlace

		n = n//10
		decimalPlace *= 10
	
	result += add
	return result