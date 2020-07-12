def extended_eucledian_algo(a,b):
	s1 = 1
	s2 = 0
	t1 = 0
	t2 = 1
	r1 = a
	r2 = b

	while r2 != 0:
		q = r1//r2
		s1,s2 = s2, s1 - s2*q
		t1,t2 = t2, t1 - t2*q
		r1,r2 = r2, r1%r2
	return (r1,s1,t1)

if __name__ == "__main__":
	# a,b = 36,60
	a,b = 123211,1432
	print( extended_eucledian_algo(a,b) )