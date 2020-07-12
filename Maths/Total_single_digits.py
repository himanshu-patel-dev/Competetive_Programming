def Total_single_digits(n):
	"""
	it returns the num of single digits required to 
	write all num from 1 to n
	"""
	digit = len(str(n))-1
	result = (n - 10**(digit) + 1) * (digit+1)
	for i in range(1,digit+1):
		result += 9*(10**(i-1)) * i
	return result

for _ in range(int(input())):
	n = int(input())
	print( Total_single_digits(n) )
