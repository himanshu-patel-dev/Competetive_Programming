def isolate_righmost_bit(n):
	'''
	if n = 1010 then return 0010
	if n = 11100100 then return 00000100
	'''
	return n & (-n)

n = 6
print( isolate_righmost_bit(n) )

n = 10
print( isolate_righmost_bit(n) )
