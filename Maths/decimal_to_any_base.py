def decimal_to_any_base(n,base):
	equivalent = {
		10: 'A',
		11: 'B',
		12: 'C',
		13: 'D',
		14: 'E',
		15: 'F'
	}
	result = ""

	while n > 0:
		t = n%base
		if t > 9:
			result += equivalent[t]
		else:
			result += str(t)
		n = n//base
	return result[::-1]
