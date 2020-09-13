def find_elements(lst):
	xor = 0
	n = len(lst)

	# 2 ele are repeated then n-2 are unique
	# iterate over all unique value present from 1 to n
	for i in range(1,n-1):
		xor = xor ^ i 

	# xor contain combined xor of all ele from 1 to n
	# now it with all ele present in lst
	for i in range(n):
		xor = xor ^ lst[i]

	# now xor have final xor of a and b as repeating element
	# print(xor)

	a = b = 0
	# the bit which is different in a and b is a set bit in xor of both
	right_most_setbit = xor & ~(xor-1)

	# a contain xor of all ele in lst and in range 1 to n who have bit set 
	# at same location as in right_most_setbit, similary b containg xor those 
	# element xor which do not have this bit set

	for num in range(1,n-1):
		if right_most_setbit & num:
			a = a ^ num
		else:
			b = b ^ num

	for i in range(n):
		if lst[i] & right_most_setbit:
			a = a ^ lst[i]
		else:
			b = b ^ lst[i]

	print(a,b)

if __name__ == "__main__":
	# only 2 and 3 are repeated twice and no other
	lst = [1,2,3,4,5,2,3]
	find_elements(lst)

	# only 1 and 5 repeates
	lst = [1,2,3,4,5,6,7,1,5]
	find_elements(lst)