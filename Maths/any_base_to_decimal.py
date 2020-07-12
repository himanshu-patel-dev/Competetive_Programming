def value(a):
	if '0' <= a and a <= '9':
		return ord(a) - ord('0')
	else:	# for hexadeciaml
		return ord(a) - ord('A') + 10

def any_base_to_decimal(string, base):
	decimal = 0
	n = len(string)
	weight = 1
	for i in range(n-1,-1,-1):
		digit = value(string[i])
		# if digit greater than radix
		if digit >= base:
			return -1

		decimal += digit * weight
		weight = weight * base
	return decimal

if __name__ == "__main__":
	base = 16
	string = '11A'
	print( any_base_to_decimal(string, base) )