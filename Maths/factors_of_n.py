import math
def factors_of_n(n):
	"""
	return a list (sorted) containing all the factors of n
	time comp = O( sqrt(n) )
	space comp = O(no of factors of n)
	"""
	if n == 1:
		return [1]
	else:
		lst = [1,n]
	for i in range(2, int(math.sqrt(n)) + 1 ):
		if n%i == 0:
			lst.append(i)
			if i != n//i:
				lst.append(n//i)
	return sorted(lst)

if __name__ == "__main__":
	n = 30
	# n = 1
	print( factors_of_n(n) )